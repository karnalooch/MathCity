"""Run real Luau scripts against lightweight Roblox service doubles.
Usage: python tests/run.py PATH_TO_LUAU
"""
from pathlib import Path
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
sources = []
for path in (root / "src").rglob("*.luau"):
    sources.append(f'SOURCES["{path.stem}"] = [====[\n{path.read_text(encoding="utf-8-sig")}\n]====]')
program = "local SOURCES = {}\n" + "\n".join(sources)
program += "\n" + (root / "tests/regression.luau").read_text(encoding="utf-8")
with tempfile.TemporaryDirectory(prefix="math-roblox-tests-") as temporary:
    script = Path(temporary) / "regression.luau"
    script.write_text(program, encoding="utf-8")
    result = subprocess.run([sys.argv[1], str(script)], check=False)
    sys.exit(result.returncode)
