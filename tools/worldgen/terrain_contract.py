"""Lossless H00 serialization; never generates a landscape or substitutes for Houdini.

Only the native builder calls export_terrain in production. Pure-Python tests exercise
the file contract with synthetic arrays and do not constitute a Houdini/Studio test.
PNG rows are -Z to +Z and columns -X to +X. Studio orientation remains a measured gate.
Palette: https://github.com/Roblox/creator-docs/blob/main/content/en-us/parts/terrain.md
"""
from __future__ import annotations

import hashlib
import json
import math
import struct
import zlib
from collections import Counter
from pathlib import Path


MATERIAL_PALETTE = {
    "grass": (106, 127, 63),
    "ground": (102, 92, 59),
    "sand": (143, 126, 95),
    "rock": (102, 108, 111),
    "asphalt": (115, 123, 107),
}
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def finite_number(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label}: expected number")
    if not math.isfinite(value):
        raise ValueError(f"{label}: must be finite")
    return float(value)


def validate_recipe(recipe):
    """Return the fixed import transform. Do not derive vertical range from data."""
    if recipe.get("schema_version") != 1:
        raise ValueError("unsupported recipe schema_version")
    dimensions = recipe.get("resolution")
    if not isinstance(dimensions, list) or len(dimensions) != 2:
        raise ValueError("resolution must be [width, height]")
    for value in dimensions:
        if isinstance(value, bool) or not isinstance(value, int) or not 4 <= value <= 4096:
            raise ValueError("resolution must contain integers between 4 and 4096")
    spp = finite_number(recipe.get("studs_per_pixel"), "studs_per_pixel")
    if spp != 4:
        raise ValueError("native Roblox heightmap contract requires 4 studs per pixel")
    mps = finite_number(recipe.get("meters_per_stud"), "meters_per_stud")
    if not 0 < mps <= 10:
        raise ValueError("meters_per_stud outside supported range")
    height_range = recipe.get("height_range_studs")
    if not isinstance(height_range, list) or len(height_range) != 2:
        raise ValueError("height_range_studs must contain fixed lower/upper bounds")
    lo, hi = [finite_number(x, "height_range_studs") for x in height_range]
    if lo >= hi or any(x % 4 != 0 for x in (lo, hi)):
        raise ValueError("height bounds must increase and align to 4-stud voxels")
    center = recipe.get("region_center_xz_studs", [0, 0])
    if not isinstance(center, list) or len(center) != 2:
        raise ValueError("region_center_xz_studs must have two elements")
    cx, cz = [finite_number(x, "region_center_xz_studs") for x in center]
    if cx % 4 != 0 or cz % 4 != 0:
        raise ValueError("region center must align to 4-stud voxels")
    return {
        "position_studs": [cx, (lo + hi) / 2, cz],
        "size_studs": [dimensions[0] * spp, hi - lo, dimensions[1] * spp],
        "height_range_studs": [lo, hi],
        "height_range_m": [lo * mps, hi * mps],
        "grid_spacing_m": spp * mps,
        "studs_per_pixel": spp,
        "meters_per_stud": mps,
        "native_import_precision": "NOT_VERIFIED_IN_STUDIO",
    }


def quantize_height(height_m, recipe):
    mps = recipe["meters_per_stud"]
    lo, hi = [x * mps for x in recipe["height_range_studs"]]
    height_m = finite_number(height_m, "height sample")
    # Native HF samples are float32. Permit only endpoint representation error,
    # not an arbitrary epsilon or a changed normalization range.
    lo_f32 = struct.unpack("<f", struct.pack("<f", lo))[0]
    hi_f32 = struct.unpack("<f", struct.pack("<f", hi))[0]
    if not min(lo, lo_f32) <= height_m <= max(hi, hi_f32):
        raise ValueError(f"height {height_m} outside fixed range [{lo}, {hi}]; no auto-remap")
    height_m = max(lo, min(hi, height_m))
    return int(math.floor((height_m - lo) * 65535 / (hi - lo) + 0.5))


def sample_position(column, row, height_m, recipe):
    width, depth = recipe["resolution"]
    cx, cz = recipe.get("region_center_xz_studs", [0, 0])
    spp = recipe["studs_per_pixel"]
    return [cx + (column + 0.5 - width / 2) * spp,
            height_m / recipe["meters_per_stud"],
            cz + (row + 0.5 - depth / 2) * spp]


def _chunk(kind, data):
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))


def encode_png(width, height, bit_depth, color_type, row_bytes):
    """Canonical unfiltered PNG, without colour-management or gamma chunks."""
    if (bit_depth, color_type) not in ((16, 0), (8, 0), (8, 2)):
        raise ValueError("unsupported canonical PNG format")
    channels = 3 if color_type == 2 else 1
    stride = width * channels * (bit_depth // 8)
    if len(row_bytes) != height or any(len(row) != stride for row in row_bytes):
        raise ValueError("invalid PNG row dimensions")
    ihdr = struct.pack(">IIBBBBB", width, height, bit_depth, color_type, 0, 0, 0)
    pixels = b"".join(b"\0" + row for row in row_bytes)
    return PNG_SIGNATURE + _chunk(b"IHDR", ihdr) + _chunk(b"IDAT", zlib.compress(pixels, 9)) + _chunk(b"IEND", b"")


def read_png(path):
    """Validate/decode only our canonical output; reject transformed/edited images."""
    data = Path(path).read_bytes()
    if data[:8] != PNG_SIGNATURE:
        raise ValueError("invalid PNG signature")
    offset, header, compressed, seen = 8, None, bytearray(), []
    while offset < len(data):
        if offset + 12 > len(data):
            raise ValueError("truncated PNG chunk")
        size = struct.unpack_from(">I", data, offset)[0]
        end = offset + size + 12
        if end > len(data):
            raise ValueError("truncated PNG chunk payload")
        kind = data[offset + 4:offset + 8]
        payload = data[offset + 8:offset + 8 + size]
        crc = struct.unpack_from(">I", data, offset + 8 + size)[0]
        if zlib.crc32(kind + payload) != crc:
            raise ValueError("PNG CRC mismatch")
        seen.append(kind)
        if kind == b"IHDR":
            if len(seen) != 1 or size != 13:
                raise ValueError("invalid PNG IHDR")
            header = struct.unpack(">IIBBBBB", payload)
        elif kind == b"IDAT":
            compressed.extend(payload)
        elif kind == b"IEND":
            if size or end != len(data):
                raise ValueError("invalid PNG end/trailing data")
            break
        else:
            raise ValueError(f"noncanonical PNG chunk: {kind!r}")
        offset = end
    if not header or seen != [b"IHDR", b"IDAT", b"IEND"]:
        raise ValueError("noncanonical PNG structure")
    width, height, depth, color_type, compression, filtering, interlace = header
    if not (4 <= width <= 4096 and 4 <= height <= 4096):
        raise ValueError("invalid PNG resolution")
    if (depth, color_type) not in ((16, 0), (8, 0), (8, 2)) or any((compression, filtering, interlace)):
        raise ValueError("unsupported PNG encoding")
    stride = width * (3 if color_type == 2 else 1) * (depth // 8)
    expected_size = height * (stride + 1)
    decoder = zlib.decompressobj()
    raw = decoder.decompress(bytes(compressed), expected_size + 1)
    if len(raw) != expected_size or not decoder.eof or decoder.unused_data:
        raise ValueError("invalid PNG decompressed size/stream")
    rows = []
    for row in range(height):
        start = row * (stride + 1)
        if raw[start] != 0:
            raise ValueError("noncanonical PNG filter")
        rows.append(raw[start + 1:start + 1 + stride])
    return {"width": width, "height": height, "bit_depth": depth,
            "color_type": color_type, "rows": rows}


def file_record(path, root):
    path, root = Path(path), Path(root)
    data = path.read_bytes()
    return {"path": path.relative_to(root).as_posix(), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def checked_artifact(root, record):
    root = Path(root).resolve()
    path = (root / record["path"]).resolve()
    try:
        path.relative_to(root)
    except ValueError as exc:
        raise ValueError("artifact escapes run directory") from exc
    actual = file_record(path, root)
    if actual != record:
        raise ValueError(f"artifact checksum/length/path mismatch: {record['path']}")
    return path


def studio_probe_source(probes, settings, source_samples_sha256):
    """Emit a READ-ONLY Edit-mode probe; native image import happens in Terrain Editor."""
    expected = {"probes": probes, "height_range_studs": settings["height_range_studs"],
                "height_tolerance_studs": 4.0, "materials": list(MATERIAL_PALETTE),
                "source_samples_sha256": source_samples_sha256}
    data = json.dumps(expected, separators=(",", ":"), allow_nan=False)
    return '''-- MathCity H00: READ ONLY. Run in Edit mode of the explicitly selected test studio_id.
-- This checks samples after native Terrain Editor import. It never imports, writes or publishes.
local HttpService = game:GetService("HttpService")
local RunService = game:GetService("RunService")
local Workspace = game:GetService("Workspace")
assert(RunService:IsStudio(), "H00 probe requires Studio")
assert(not RunService:IsRunning(), "Stop Play and run this probe in Edit mode")
assert(game.PlaceId == 0, "Use a new unpublished local H00 test place")
local expected = HttpService:JSONDecode([=[''' + data + ''']=])
local params = RaycastParams.new()
params.FilterType = Enum.RaycastFilterType.Include
params.FilterDescendantsInstances = {Workspace.Terrain}
params.IgnoreWater = true
local upper = expected.height_range_studs[2] + 32
local lower = expected.height_range_studs[1] - 32
local rows, heightFailures, materialFailures, coverage = {}, 0, 0, {}
for _, probe in ipairs(expected.probes) do
    local p = probe.position_studs
    local hit = Workspace:Raycast(Vector3.new(p[1], upper, p[3]), Vector3.new(0, lower - upper, 0), params)
    local row = {pixel = probe.pixel, expected_y = p[2], expected_material = probe.material}
    if not hit then
        row.height_status = "FAIL_MISSING_TERRAIN"
        heightFailures += 1
    else
        row.actual_y = hit.Position.Y
        row.height_error_studs = math.abs(hit.Position.Y - p[2])
        row.actual_material = string.lower(hit.Material.Name)
        row.height_status = row.height_error_studs <= expected.height_tolerance_studs and "PASS" or "FAIL"
        if row.height_status ~= "PASS" then heightFailures += 1 end
        if probe.check_material then
            coverage[probe.material] = true
            row.material_status = row.actual_material == probe.material and "PASS" or "FAIL"
            if row.material_status ~= "PASS" then materialFailures += 1 end
        else
            row.material_status = "NOT_CHECKED_BOUNDARY_PIXEL"
        end
    end
    table.insert(rows, row)
end
local missing = {}
for _, material in ipairs(expected.materials) do
    if not coverage[material] then table.insert(missing, material) end
end
local report = {
    packet_id = "H00", scope = "read-only sampled height/material import check",
    source_samples_sha256 = expected.source_samples_sha256,
    place_name = game.Name, place_id = game.PlaceId, recorded_utc = DateTime.now():ToIsoDate(),
    height_tolerance_studs = expected.height_tolerance_studs,
    HEIGHT_PROBE = heightFailures == 0 and "PASS" or "FAIL",
    MATERIAL_PROBE = materialFailures > 0 and "FAIL" or (#missing > 0 and "INCOMPLETE" or "PASS"),
    missing_material_coverage = missing, results = rows,
    VISUAL_REVIEW = "NOT_RUN", PLAYTEST = "NOT_RUN", DEVICE_PASS = "NOT_RUN",
}
print(HttpService:JSONEncode(report))
return report
'''


def export_terrain(output_dir, recipe, heights_m, material_keys, masks):
    """Write bytes from cooked Houdini arrays; returns metadata for manifest.json."""
    settings = validate_recipe(recipe)
    width, depth = recipe["resolution"]
    if set(masks) != set(MATERIAL_PALETTE):
        raise ValueError("exactly five material masks required")
    for name, values in [("height", heights_m), ("material", material_keys), *masks.items()]:
        if len(values) != depth or any(len(row) != width for row in values):
            raise ValueError(f"{name}: array shape mismatch")
    terrain_dir = Path(output_dir) / "terrain"
    if terrain_dir.exists():
        raise ValueError("terrain output already exists; use a new run directory")
    if (Path(output_dir) / "verify_import.command.luau").exists():
        raise ValueError("Studio probe already exists; use a new run directory")
    heights, encoded_heights, color_rows = [], [], []
    mask_rows = {key: [] for key in MATERIAL_PALETTE}
    counts = Counter()
    raw_samples = bytearray()
    for z in range(depth):
        row_heights, row_colors = bytearray(), bytearray()
        row_masks = {key: bytearray() for key in MATERIAL_PALETTE}
        for x in range(width):
            value = finite_number(heights_m[z][x], "height sample")
            raw = struct.pack("<f", value)
            value = struct.unpack("<f", raw)[0]
            q = quantize_height(value, recipe)
            key = material_keys[z][x]
            if key not in MATERIAL_PALETTE:
                raise ValueError(f"unknown material key: {key}")
            weights = {name: finite_number(grid[z][x], name) for name, grid in masks.items()}
            if any(w < 0 or w > 1 for w in weights.values()) or abs(sum(weights.values()) - 1) > 1e-5:
                raise ValueError("material masks must form a partition of unity")
            if any(abs(w - (1 if name == key else 0)) > 1e-5 for name, w in weights.items()):
                raise ValueError("H00 material masks must be one-hot and agree with colormap")
            heights.append(value)
            raw_samples.extend(raw)
            row_heights.extend(struct.pack(">H", q))
            row_colors.extend(MATERIAL_PALETTE[key])
            counts[key] += 1
            for name, weight in weights.items():
                row_masks[name].append(round(weight * 255))
        encoded_heights.append(bytes(row_heights))
        color_rows.append(bytes(row_colors))
        for key in mask_rows:
            mask_rows[key].append(bytes(row_masks[key]))
    if set(counts) != set(MATERIAL_PALETTE):
        raise ValueError("all five H00 material classes must be present")
    span_studs = (max(heights) - min(heights)) / recipe["meters_per_stud"]
    if span_studs < 16:
        raise ValueError("H00 terrain relief below 16 studs; flat output rejected")
    terrain_dir.mkdir(parents=True)
    (terrain_dir / "masks").mkdir()
    outputs = {
        "heightmap": (terrain_dir / "heightmap.png", encode_png(width, depth, 16, 0, encoded_heights)),
        "colormap": (terrain_dir / "colormap.png", encode_png(width, depth, 8, 2, color_rows)),
        "height_samples": (terrain_dir / "height_samples.f32", bytes(raw_samples)),
    }
    records = {}
    for name, (path, data) in outputs.items():
        path.write_bytes(data)
        records[name] = file_record(path, output_dir)
    records["masks"] = {}
    for key, rows in mask_rows.items():
        path = terrain_dir / "masks" / f"{key}.png"
        path.write_bytes(encode_png(width, depth, 8, 0, rows))
        records["masks"][key] = file_record(path, output_dir)
    # Grid plus per-material samples; all native sample heights remain available in f32.
    locations = {(x, z) for x in (width // 8, width // 2, 7 * width // 8)
                 for z in (depth // 8, depth // 2, 7 * depth // 8)}
    def interior(x, z, key):
        return (0 < x < width - 1 and 0 < z < depth - 1
                and all(material_keys[rz][cx] == key for rz in range(z - 1, z + 2)
                        for cx in range(x - 1, x + 2)))

    for key in MATERIAL_PALETTE:
        candidates = [(x, z) for z in range(depth) for x in range(width) if material_keys[z][x] == key]
        found = next(((x, z) for x, z in candidates if interior(x, z, key)), candidates[0])
        locations.add(found)
    probes = []
    for x, z in sorted(locations, key=lambda p: (p[1], p[0])):
        value = heights[z * width + x]
        probes.append({"pixel": [x, z], "position_studs": sample_position(x, z, value, recipe),
                       "height_m": value, "encoded_u16": quantize_height(value, recipe),
                       "material": material_keys[z][x],
                       "check_material": interior(x, z, material_keys[z][x])})
    probe_path = Path(output_dir) / "verify_import.command.luau"
    if probe_path.exists():
        raise ValueError("Studio probe already exists; use a new run directory")
    probe_path.write_text(studio_probe_source(probes, settings, records["height_samples"]["sha256"]), encoding="utf-8")
    records["studio_probe"] = file_record(probe_path, output_dir)
    return {
        **records, "probes": probes, "import_settings": settings,
        "orientation": {"columns": "negative_X_to_positive_X", "rows": "negative_Z_to_positive_Z",
                        "samples": "pixel_centers", "studio_confirmation": "NOT_RUN"},
        "source_samples_sha256": records["height_samples"]["sha256"],
        "stats": {"sample_count": width * depth, "min_height_m": min(heights),
                  "max_height_m": max(heights), "relief_studs": span_studs,
                  "material_pixel_counts": dict(counts)},
    }
