#requires -Version 5.1
<#
P00/H00: inspect installed tools, then optionally cook an isolated Houdini spike.
Default is inspection only. No installation, map edit, Studio launch or publish.
Example: .\tools\worldgen\Invoke-MathCityH00.ps1 -Cook
#>
[CmdletBinding(DefaultParameterSetName = 'Audit')]
param(
    [string]$RepoRoot = (Split-Path -Parent (Split-Path -Parent $PSScriptRoot)),
    [string]$WorkRoot = 'D:\MathCity\work',
    [string]$HythonPath,
    [string]$BlenderPath,
    [string]$UnrealEditorPath,
    [string]$MaterialForgePath,
    [Parameter(ParameterSetName = 'Audit')][switch]$PreflightOnly,
    [Parameter(Mandatory = $true, ParameterSetName = 'Cook')][switch]$Cook,
    [ValidateRange(30, 3600)][int]$InspectionTimeoutSeconds = 120,
    [ValidateRange(60, 7200)][int]$CookTimeoutSeconds = 900
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
if ($env:OS -ne 'Windows_NT') { throw 'BLOCKED_PLATFORM: run this entrypoint on the existing Windows workstation.' }

function Write-Json([string]$Path, $Value) {
    $json = $Value | ConvertTo-Json -Depth 30
    [IO.File]::WriteAllText($Path, $json + [Environment]::NewLine, (New-Object Text.UTF8Encoding($false)))
}
function Invoke-Git([string[]]$GitArguments) {
    $result = @(& git -C $script:RepoRoot @GitArguments 2>&1)
    if ($LASTEXITCODE -ne 0) { throw "BLOCKED_GIT: git $($GitArguments -join ' ') failed: $($result -join ' ')" }
    return ($result -join "`n").Trim()
}
function Test-Inside([string]$Path, [string]$Root) {
    $p = [IO.Path]::GetFullPath($Path).TrimEnd('\')
    $r = [IO.Path]::GetFullPath($Root).TrimEnd('\')
    return $p.Equals($r, [StringComparison]::OrdinalIgnoreCase) -or $p.StartsWith($r + '\', [StringComparison]::OrdinalIgnoreCase)
}
function Find-Executable([string]$Explicit, [string]$Command, [string[]]$Candidates) {
    if ($Explicit) {
        if (-not (Test-Path -LiteralPath $Explicit -PathType Leaf)) { throw "BLOCKED_TOOL_PATH: $Explicit does not exist." }
        return (Resolve-Path -LiteralPath $Explicit).Path
    }
    foreach ($candidate in $Candidates) {
        if (Test-Path -LiteralPath $candidate -PathType Leaf) { return (Resolve-Path -LiteralPath $candidate).Path }
    }
    $found = Get-Command $Command -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($found) { return $found.Source }
    return $null
}
function Describe-File([string]$Path) {
    if (-not $Path) { return @{ status = 'NOT_DETECTED' } }
    $item = Get-Item -LiteralPath $Path
    $version = $null
    if (-not $item.PSIsContainer) { $version = $item.VersionInfo.FileVersion }
    return @{ status = 'PATH_DETECTED_ONLY'; path = $item.FullName; file_version = $version; launched = $false }
}
function Quote-Argument([string]$Value) {
    # Windows CRT quoting: double backslashes preceding a quote or closing quote.
    $quoted = [regex]::Replace($Value, '(\\*)"', '$1$1\"')
    $quoted = [regex]::Replace($quoted, '(\\+)$', '$1$1')
    return '"' + $quoted + '"'
}
function Invoke-HythonStage([string]$Name, [string[]]$StageArguments, [int]$TimeoutSeconds) {
    $stdout = Join-Path $script:RunDir ($Name + '.stdout.log')
    $stderr = Join-Path $script:RunDir ($Name + '.stderr.log')
    $arguments = ($StageArguments | ForEach-Object { Quote-Argument $_ }) -join ' '
    $start = [DateTime]::UtcNow
    $oldTemp = [Environment]::GetEnvironmentVariable('HOUDINI_TEMP_DIR', 'Process')
    try {
        [Environment]::SetEnvironmentVariable('HOUDINI_TEMP_DIR', (Join-Path $script:RunDir 'tmp'), 'Process')
        $process = Start-Process -FilePath $script:HythonPath -ArgumentList $arguments -WorkingDirectory $script:RunDir -RedirectStandardOutput $stdout -RedirectStandardError $stderr -PassThru -NoNewWindow
        $null = $process.Handle
    } finally {
        [Environment]::SetEnvironmentVariable('HOUDINI_TEMP_DIR', $oldTemp, 'Process')
    }
    $timedOut = -not $process.WaitForExit($TimeoutSeconds * 1000)
    if ($timedOut) {
        # Only the exact process started above; never stop other Houdini sessions.
        if (-not $process.HasExited) { $process.Kill() }
        [void]$process.WaitForExit(5000)
    } else { $process.WaitForExit() }
    $exitCode = if ($timedOut) { $null } else { $process.ExitCode }
    $stage = [ordered]@{
        name = $Name; started_utc = $start.ToString('o'); finished_utc = [DateTime]::UtcNow.ToString('o')
        timed_out = $timedOut; exit_code = $exitCode; stdout_log = $stdout; stderr_log = $stderr
        arguments = $StageArguments
    }
    $script:Report.stages += $stage
    Write-Json (Join-Path $script:RunDir 'run_report.json') $script:Report
    if ($timedOut) { throw "BLOCKED_TIMEOUT: $Name exceeded $TimeoutSeconds seconds. See $stderr" }
    if ($exitCode -ne 0) { throw "BLOCKED_STAGE: $Name exited $exitCode. See $stderr" }
}

$RepoRoot = (Resolve-Path -LiteralPath $RepoRoot).Path
$gitRoot = Invoke-Git @('rev-parse', '--show-toplevel')
if (-not [IO.Path]::GetFullPath($gitRoot).Equals($RepoRoot, [StringComparison]::OrdinalIgnoreCase)) { throw 'BLOCKED_REPO: RepoRoot must be the MathCity checkout root.' }
$origin = Invoke-Git @('remote', 'get-url', 'origin')
if ($origin -notmatch '^(https://github\.com/|git@github\.com:)karnalooch/MathCity(?:\.git)?/?$') { throw 'BLOCKED_REPO: origin is not karnalooch/MathCity.' }
$baseHead = Invoke-Git @('rev-parse', 'HEAD')
$branch = Invoke-Git @('branch', '--show-current')
if (-not $branch -or $branch -in @('main', 'master')) { throw 'BLOCKED_BRANCH: use a named feature branch, preserving all local changes.' }
$dirty = Invoke-Git @('status', '--porcelain')
if ($dirty) { throw 'BLOCKED_DIRTY_WORKTREE: preserve local edits and use a clean feature checkout. No reset/stash was performed.' }
$mapPath = Join-Path $RepoRoot 'MathCity.rbxl'
if (-not (Test-Path -LiteralPath $mapPath -PathType Leaf)) { throw 'BLOCKED_BASELINE: MathCity.rbxl is missing.' }
$baseMapBlob = Invoke-Git @('rev-parse', 'HEAD:MathCity.rbxl')
$workMapBlob = Invoke-Git @('hash-object', '--', $mapPath)
if ($baseMapBlob -ne $workMapBlob) { throw 'BLOCKED_BASELINE: map differs from the tracked HEAD blob.' }
$baseMapSha256 = (Get-FileHash -LiteralPath $mapPath -Algorithm SHA256).Hash.ToLowerInvariant()

if ($WorkRoot -notmatch '^[A-Za-z]:[\\/]') { throw 'BLOCKED_WORK_ROOT: use an absolute local-drive output path.' }
$WorkRoot = [IO.Path]::GetFullPath($WorkRoot)
if (Test-Inside $WorkRoot $RepoRoot) { throw 'BLOCKED_WORK_ROOT: generated files must be outside the checkout.' }
foreach ($protectedRoot in @('D:\yacs', 'D:\gem\YetAnotherCyclingSim', 'D:\gem\YACS-ci-main', 'G:\gem\YetAnotherCyclingSim')) {
    if (Test-Inside $WorkRoot $protectedRoot) { throw 'BLOCKED_WORK_ROOT: output may not be inside the YACS workshop.' }
}
$parent = $WorkRoot
while ($parent) {
    if (Test-Path -LiteralPath (Join-Path $parent '.git')) { throw 'BLOCKED_WORK_ROOT: output may not be inside any Git checkout.' }
    $next = Split-Path -Parent $parent
    if ($next -eq $parent) { break }
    $parent = $next
}
$runName = 'H00_' + [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssfffZ') + '_' + [Guid]::NewGuid().ToString('N').Substring(0, 8)
$RunDir = Join-Path $WorkRoot $runName
[void](New-Item -ItemType Directory -Path $RunDir)
[void](New-Item -ItemType Directory -Path (Join-Path $RunDir 'tmp'))
$Report = [ordered]@{
    schema_version = 1; packet_id = 'P00_H00'; started_utc = [DateTime]::UtcNow.ToString('o')
    status = 'PREFLIGHT_RUNNING'; repo_root = $RepoRoot; run_directory = $RunDir
    base_head = $baseHead; branch = $branch; base_map_blob = $baseMapBlob; base_map_sha256 = $baseMapSha256
    code_tree = (Invoke-Git @('rev-parse', 'HEAD:src')); stages = @(); tools = @{}
    cook_status = 'NOT_RUN'; reopen_status = 'NOT_RUN'; export_status = 'NOT_RUN'; studio_status = 'NOT_RUN'
    mcp_status = 'NOT_CONNECTED_BY_THIS_SCRIPT'; device_status = 'NOT_RUN'; client_16_status = 'NOT_RUN'
    base_map_preserved = $null
}
$failure = $null
try {
    $hythonCandidates = @('D:\yacs\tools\houdini-22.0.466\bin\hython.exe')
    foreach ($root in @('D:\yacs\tools', 'D:\Program Files\Side Effects Software', (Join-Path $env:ProgramFiles 'Side Effects Software'))) {
        if (Test-Path -LiteralPath $root -PathType Container) {
            $hythonCandidates += @(Get-ChildItem -LiteralPath $root -Directory | Where-Object { $_.Name -match '^houdini' } | Sort-Object Name -Descending | ForEach-Object { Join-Path $_.FullName 'bin\hython.exe' })
        }
    }
    $HythonPath = Find-Executable $HythonPath 'hython.exe' $hythonCandidates
    $Report.tools.houdini = Describe-File $HythonPath
    $blenderCandidates = @()
    foreach ($root in @('D:\yacs\tools', 'D:\Program Files\Blender Foundation', (Join-Path $env:ProgramFiles 'Blender Foundation'))) {
        if (Test-Path -LiteralPath $root -PathType Container) {
            $blenderCandidates += @(Get-ChildItem -LiteralPath $root -Directory | Where-Object { $_.Name -match '^blender' } | ForEach-Object { Join-Path $_.FullName 'blender.exe' })
        }
    }
    $BlenderPath = Find-Executable $BlenderPath 'blender.exe' $blenderCandidates
    $UnrealEditorPath = Find-Executable $UnrealEditorPath 'UnrealEditor.exe' @('D:\Epic Games\UE_5.8\Engine\Binaries\Win64\UnrealEditor.exe', 'D:\Epic Games\UE\_5.8\Engine\Binaries\Win64\UnrealEditor.exe')
    $Report.tools.blender = Describe-File $BlenderPath
    $Report.tools.unreal_editor = Describe-File $UnrealEditorPath
    if ($MaterialForgePath -and -not (Test-Path -LiteralPath $MaterialForgePath)) { throw 'BLOCKED_TOOL_PATH: explicit MaterialForgePath is missing.' }
    if (-not $MaterialForgePath) {
        foreach ($candidate in @('D:\yacs\project\Plugins\MaterialForge', 'D:\yacs\project\Plugins\MaterialForger', 'D:\yacs\tools\MaterialForge', 'D:\gem\YACS-ci-main\Plugins\MaterialForge')) {
            if (Test-Path -LiteralPath $candidate) { $MaterialForgePath = $candidate; break }
        }
    }
    if ($MaterialForgePath) { $Report.tools.material_forge = Describe-File $MaterialForgePath } else {
        $Report.tools.material_forge = @{ status = 'NOT_DETECTED'; note = 'Supply -MaterialForgePath for an existing executable/plugin directory. H00 does not need it.' }
    }
    $mcpPath = if ($env:LOCALAPPDATA) { Join-Path $env:LOCALAPPDATA 'Roblox\mcp.bat' } else { $null }
    $Report.tools.roblox_mcp = if ($mcpPath -and (Test-Path -LiteralPath $mcpPath -PathType Leaf)) { Describe-File $mcpPath } else { @{ status = 'NOT_DETECTED' } }
    if (-not $HythonPath) { throw 'BLOCKED_HOUDINI_NOT_FOUND: supply the verified existing -HythonPath; do not install another copy.' }
    $inspect = Join-Path $PSScriptRoot 'inspect_houdini.py'
    $inventoryPath = Join-Path $RunDir 'houdini_environment.json'
    Invoke-HythonStage 'inspect' @($inspect, '--output', $inventoryPath) $InspectionTimeoutSeconds
    if (-not (Test-Path -LiteralPath $inventoryPath -PathType Leaf)) { throw 'BLOCKED_INVENTORY: hython produced no environment report.' }
    $inventory = Get-Content -LiteralPath $inventoryPath -Raw | ConvertFrom-Json
    if ($inventory.status -ne 'HOUDINI_INSPECTED') { throw 'BLOCKED_INVENTORY: environment report is not HOUDINI_INSPECTED.' }
    $Report.tools.houdini.runtime_version = $inventory.houdini_version
    $Report.tools.houdini.license_category = $inventory.license_category
    $Report.tools.houdini.labs_status = $inventory.labs.status
    $Report.status = 'PREFLIGHT_INSPECTED'
    if ($Cook) {
        $config = Join-Path $RepoRoot 'worldgen\h00\recipe.json'
        $builder = Join-Path $PSScriptRoot 'build_h00.py'
        $validator = Join-Path $PSScriptRoot 'validate_h00.py'
        foreach ($requiredFile in @($config, $builder, $validator)) {
            if (-not (Test-Path -LiteralPath $requiredFile -PathType Leaf)) { throw "BLOCKED_ENTRYPOINT_MISSING: $requiredFile" }
        }
        $Report.cook_status = 'RUNNING'
        Invoke-HythonStage 'build' @($builder, '--config', $config, '--output', $RunDir) $CookTimeoutSeconds
        if (-not (Test-Path -LiteralPath (Join-Path $RunDir 'manifest.json') -PathType Leaf)) { throw 'BLOCKED_EXPORT: builder exited without manifest.json.' }
        $Report.cook_status = 'PROCESS_EXITED_ZERO'
        $Report.reopen_status = 'RUNNING'
        Invoke-HythonStage 'reopen' @($builder, '--verify-run', $RunDir) $CookTimeoutSeconds
        if (-not (Test-Path -LiteralPath (Join-Path $RunDir 'reopen_verification.json') -PathType Leaf)) { throw 'BLOCKED_REOPEN: verification exited without reopen_verification.json.' }
        $Report.reopen_status = 'PROCESS_EXITED_ZERO'
        Invoke-HythonStage 'validate' @($validator, '--run-dir', $RunDir) $InspectionTimeoutSeconds
        $Report.export_status = 'VALIDATOR_EXITED_ZERO'
        $Report.status = 'EXPORT_CHECKED_STUDIO_NOT_RUN'
    }
} catch {
    $failure = $_.Exception.Message
    $Report.status = 'BLOCKED'
    $Report.error = $failure
    if ($Report.cook_status -eq 'RUNNING') { $Report.cook_status = 'FAILED_OR_TIMED_OUT' }
    if ($Report.reopen_status -eq 'RUNNING') { $Report.reopen_status = 'FAILED_OR_TIMED_OUT' }
} finally {
    try {
        $finalMapSha256 = (Get-FileHash -LiteralPath $mapPath -Algorithm SHA256).Hash.ToLowerInvariant()
        $Report.final_map_sha256 = $finalMapSha256
        $Report.final_head = Invoke-Git @('rev-parse', 'HEAD')
        $Report.final_worktree_status = Invoke-Git @('status', '--porcelain')
        $Report.base_map_preserved = $finalMapSha256 -eq $baseMapSha256
        if (-not $Report.base_map_preserved -or $Report.final_head -ne $baseHead -or $Report.final_worktree_status) {
            $failure = 'BLOCKED_BASELINE_CHANGED: map/HEAD/worktree changed during run; inspect concurrent work without reverting it.'
            $Report.status = 'BLOCKED'; $Report.error = $failure
        }
    } catch {
        $failure = 'BLOCKED_FINAL_BASELINE_CHECK: ' + $_.Exception.Message
        $Report.status = 'BLOCKED'; $Report.error = $failure
    }
    $Report.finished_utc = [DateTime]::UtcNow.ToString('o')
    Write-Json (Join-Path $RunDir 'run_report.json') $Report
}
Write-Output "Report: $(Join-Path $RunDir 'run_report.json')"
Write-Output $Report.status
if ($failure) { throw $failure }
