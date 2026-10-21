"""Validate H00 files exhaustively. FILE_PASS is never a Roblox/runtime PASS."""
from __future__ import annotations

import argparse
import json
import math
import struct
import sys
import zlib
from datetime import datetime, timezone
from pathlib import Path

from terrain_contract import (MATERIAL_PALETTE, checked_artifact, quantize_height,
                              read_png, sample_position, validate_recipe)


def validate_exports(run_dir, manifest):
    recipe, exports = manifest["recipe"], manifest["exports"]
    settings = validate_recipe(recipe)
    checked_artifact(run_dir, exports["studio_probe"])
    if exports["import_settings"] != settings:
        raise ValueError("import transform differs from recipe")
    width, depth = recipe["resolution"]
    heightmap = read_png(checked_artifact(run_dir, exports["heightmap"]))
    colormap = read_png(checked_artifact(run_dir, exports["colormap"]))
    samples = checked_artifact(run_dir, exports["height_samples"]).read_bytes()
    if len(samples) != width * depth * 4:
        raise ValueError("raw height sample count mismatch")
    if exports["source_samples_sha256"] != exports["height_samples"]["sha256"]:
        raise ValueError("native source sample digest mismatch")
    if set(exports["masks"]) != set(MATERIAL_PALETTE):
        raise ValueError("five masks required")
    masks = {key: read_png(checked_artifact(run_dir, record)) for key, record in exports["masks"].items()}
    for name, image, fmt in [("heightmap", heightmap, (16, 0)), ("colormap", colormap, (8, 2)),
                             *[(key, image, (8, 0)) for key, image in masks.items()]]:
        if (image["width"], image["height"], image["bit_depth"], image["color_type"]) != (width, depth, *fmt):
            raise ValueError(f"{name}: dimensions/channel depth mismatch")
    reverse_palette = {bytes(rgb): key for key, rgb in MATERIAL_PALETTE.items()}
    counts = {key: 0 for key in MATERIAL_PALETTE}
    heights = [value[0] for value in struct.iter_unpack("<f", samples)]
    worst_error = 0.0
    lo, hi = recipe["height_range_studs"]
    mps = recipe["meters_per_stud"]
    for z in range(depth):
        for x in range(width):
            native = heights[z * width + x]
            encoded = struct.unpack_from(">H", heightmap["rows"][z], x * 2)[0]
            if encoded != quantize_height(native, recipe):
                raise ValueError(f"heightmap/sample mismatch at pixel ({x}, {z})")
            error = abs(lo + encoded / 65535 * (hi - lo) - native / mps)
            worst_error = max(worst_error, error)
            rgb = colormap["rows"][z][x * 3:x * 3 + 3]
            if rgb not in reverse_palette:
                raise ValueError(f"non-importer RGB {tuple(rgb)} at pixel ({x}, {z})")
            key = reverse_palette[rgb]
            counts[key] += 1
            for name, image in masks.items():
                if image["rows"][z][x] != (255 if key == name else 0):
                    raise ValueError(f"mask/colormap mismatch: {name} at ({x}, {z})")
    if not all(counts.values()):
        raise ValueError("one or more material classes absent")
    if worst_error > (hi - lo) / 65535 / 2 + 1e-9:
        raise ValueError("quantization error exceeds half a 16-bit step")
    if (max(heights) - min(heights)) / mps < 16:
        raise ValueError("flat/insufficient-relief H00")
    stats = exports["stats"]
    if stats["material_pixel_counts"] != counts or stats["sample_count"] != width * depth:
        raise ValueError("manifest sample/material statistics mismatch")
    for field, actual in [("min_height_m", min(heights)), ("max_height_m", max(heights)),
                          ("relief_studs", (max(heights) - min(heights)) / mps)]:
        if not math.isclose(stats[field], actual, abs_tol=1e-9, rel_tol=1e-9):
            raise ValueError(f"manifest {field} mismatch")
    seen = set()
    for probe in exports["probes"]:
        x, z = probe["pixel"]
        if isinstance(x, bool) or isinstance(z, bool) or not isinstance(x, int) or not isinstance(z, int):
            raise ValueError("probe coordinates must be integer pixels")
        if not (0 <= x < width and 0 <= z < depth) or (x, z) in seen:
            raise ValueError("invalid/duplicate probe")
        seen.add((x, z))
        native = heights[z * width + x]
        expected = sample_position(x, z, native, recipe)
        if probe["position_studs"] != expected or probe["height_m"] != native:
            raise ValueError("probe coordinates/heights disagree with native data")
        if probe["encoded_u16"] != quantize_height(native, recipe):
            raise ValueError("probe integer height mismatch")
        rgb = colormap["rows"][z][x * 3:x * 3 + 3]
        if probe["material"] != reverse_palette[rgb]:
            raise ValueError("probe material mismatch")
    if len(seen) < 9:
        raise ValueError("insufficient asymmetric/grid probes")
    return {"sample_count": width * depth, "material_pixel_counts": counts,
            "max_height_quantization_error_studs": worst_error,
            "probe_count": len(seen), "import_settings": settings}


def validate_run(run_dir):
    manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1 or manifest.get("packet_id") != "H00":
        raise ValueError("not an H00 manifest")
    provenance, native = manifest["provenance"], manifest["native"]
    if provenance.get("generator") != "Houdini" or not provenance.get("source_files"):
        raise ValueError("missing native Houdini provenance")
    if not native.get("houdini_version") or not native.get("license_category"):
        raise ValueError("missing actual Houdini version/license category")
    if manifest["statuses"].get("HOUDINI_COOK") != "PASS":
        raise ValueError("native cook did not finish successfully")
    for key in ("hip_file", "cache_file"):
        checked_artifact(run_dir, native[key])
    if Path(native["hip_file"]["path"]).suffix not in (".hip", ".hiplc", ".hipnc"):
        raise ValueError("invalid HIP artifact extension")
    result = validate_exports(run_dir, manifest)
    reopen = json.loads((run_dir / "reopen_verification.json").read_text(encoding="utf-8"))
    if (reopen.get("status") != "PASS" or reopen.get("differences") != []
            or reopen.get("hip_sha256") != native["hip_file"]["sha256"]
            or reopen.get("sample_count") != result["sample_count"]
            or reopen.get("same_houdini_version") is not True
            or reopen.get("houdini_version") != native["houdini_version"]):
        raise ValueError("fresh native reopen evidence is missing, failed, or belongs to another HIP/version")
    result["native_reopen_evidence"] = "PASS_FOR_THIS_HIP_AND_INSTALLATION"
    result["houdini_version"] = native["houdini_version"]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    output = run_dir / "file_verification.json"
    if not run_dir.is_dir():
        parser.error("run directory does not exist")
    if output.exists():
        parser.error("verification already exists; preserve the first result")
    report = {"schema_version": 1, "packet_id": "H00", "recorded_utc": datetime.now(timezone.utc).isoformat(),
              "scope": "PNG bytes, all native exported height samples, masks, metadata and checksums",
              "STUDIO_PASS": "NOT_RUN", "DEVICE_PASS": "NOT_RUN", "16_CLIENT_PASS": "NOT_RUN"}
    try:
        report["checks"] = validate_run(run_dir)
        report["FILE_PASS"] = "PASS"
        code = 0
    except (ValueError, KeyError, TypeError, OSError, struct.error, zlib.error) as exc:
        report["FILE_PASS"] = "FAIL"
        report["error"] = str(exc)
        code = 1
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return code


if __name__ == "__main__":
    sys.exit(main())
