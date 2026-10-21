"""Build H00 with native Houdini HeightField/Erode; never synthesize a fallback.

Run with the existing licensed hython, in a fresh process. The complete Python
SOP source and recipe are embedded in the saved HIP so native recooking does
not depend on this checkout. PNGs serialize the cooked native volumes through
terrain_contract; this is not a claim that HeightField Output was executed.

Sources: SideFX HOM Volume/Geometry; SOP heightfield and heightfield_erode;
native HeightField/Output presets in SideFXLabs d7cfd09854a0939a912dbd05fcec7a51d8a9975d.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import struct
import sys
import traceback

from terrain_contract import (MATERIAL_PALETTE, checked_artifact, export_terrain,
                              file_record, read_png, validate_recipe)


def write_new_json(path, value):
    with Path(path).open("x", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write("\n")


def validate_features(recipe):
    """Reject malformed controls before creating any scene or output directory."""
    seed = recipe["seed"]
    if isinstance(seed, bool) or not isinstance(seed, int) or not 0 <= seed < 2**31:
        raise ValueError("seed must be an integer in [0, 2^31)")
    features = recipe["features"]
    for name in ("hill", "valley", "basin"):
        f = features[name]
        if len(f["center_xz_m"]) != 2 or len(f["radius_xz_m"]) != 2 or min(f["radius_xz_m"]) <= 0:
            raise ValueError("invalid feature extent: " + name)
    pad, road = features["pad"], features["road"]
    if len(pad["center_xz_m"]) != 2 or len(pad["half_size_xz_m"]) != 2 or min(pad["half_size_xz_m"]) <= 0:
        raise ValueError("invalid pad extent")
    if min(pad["blend_m"], road["half_width_m"], road["blend_m"]) <= 0 or abs(road["grade"]) > 0.2:
        raise ValueError("invalid H00 road/pad controls")
    def numbers(value):
        if isinstance(value, dict):
            for item in value.values():
                numbers(item)
        elif isinstance(value, list):
            for item in value:
                numbers(item)
        elif isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value):
            raise ValueError("feature controls must be finite numbers")
    numbers(features)


# Native inventory: Houdini 22.0.466, run H00_20261020T220649684Z_82216fe0.
# Semantic role labels preserve the manifest contract; UI labels are not an API.
ERODE_NODE_TYPE = "heightfield_erode::3.0"
ERODE_CONTROLS = (
    ("Freeze", "dofreeze", "parmTemplateType.Toggle"),
    ("Freeze at Frame", "freezeframe", "parmTemplateType.Int"),
    ("Start Frame", "startframe", "parmTemplateType.Int"),
    ("Random Seed", "seed", "parmTemplateType.Float"),
    ("Erosion Feature Size", "erosionscale", "parmTemplateType.Float"),
)


def resolve_erode_contract(node):
    """Validate all five native controls before changing any parameter."""
    errors, resolved = [], {}
    if node.type().name() != ERODE_NODE_TYPE:
        errors.append(f"node type {node.type().name()!r}; expected {ERODE_NODE_TYPE!r}")
    for role, name, expected_type in ERODE_CONTROLS:
        parm_tuple = node.parmTuple(name)
        if parm_tuple is None:
            errors.append(f"{role}: missing {name}")
            continue
        template = parm_tuple.parmTemplate()
        if template.numComponents() != 1 or len(parm_tuple) != 1:
            errors.append(f"{role}: {name} must be scalar; template={template.numComponents()}, tuple={len(parm_tuple)}")
        actual_type = str(template.type())
        if actual_type != expected_type:
            errors.append(f"{role}: {name} type {actual_type}; expected {expected_type}")
        if node.parm(name) is None:
            errors.append(f"{role}: missing scalar parameter {name}")
        resolved[role] = name
    if errors:
        raise RuntimeError("BLOCKED_NODE_SCHEMA: " + "; ".join(errors))
    return resolved


def configure_erode(node, recipe):
    """Apply the observed native contract and verify every effective value."""
    resolved = resolve_erode_contract(node)
    expected = {
        "Freeze": 1,
        "Freeze at Frame": recipe["erosion"]["freeze_frame"],
        "Start Frame": recipe["erosion"]["start_frame"],
        "Random Seed": recipe["seed"],
        "Erosion Feature Size": recipe["erosion"]["feature_size_m"],
    }
    for role, value in expected.items():
        parm = node.parm(resolved[role])
        parm.deleteAllKeyframes()
        parm.set(value)
    for role, expression in {
        "Freeze at Frame": "RECIPE['erosion']['freeze_frame']",
        "Start Frame": "RECIPE['erosion']['start_frame']",
        "Random Seed": "RECIPE['seed']",
        "Erosion Feature Size": "RECIPE['erosion']['feature_size_m']",
    }.items():
        bind_recipe(node.parm(resolved[role]), expression)
    errors, readback = [], {}
    for role, value in expected.items():
        actual = node.parm(resolved[role]).eval()
        readback[role] = actual
        valid = isinstance(actual, (int, float)) and math.isfinite(actual)
        if valid and role == "Erosion Feature Size":
            valid = math.isclose(actual, value, rel_tol=0.0, abs_tol=1e-6)
        elif valid:
            # Seed is a native Float, but represents an integer: ±1 is a different
            # simulation. Never use relative tolerance for seed or frame controls.
            valid = actual == value
        if not valid:
            errors.append(f"{resolved[role]} expected {value!r}, read {actual!r}")
    if errors:
        raise RuntimeError("BLOCKED_EROSION_READBACK: " + "; ".join(errors))
    return resolved, readback


def set_known(node, name, value):
    parm = node.parmTuple(name) if isinstance(value, tuple) else node.parm(name)
    if parm is None:
        raise RuntimeError(f"BLOCKED_NODE_SCHEMA: {node.type().name()} missing {name}")
    if not isinstance(value, tuple) and isinstance(value, str):
        choices = parm.parmTemplate().menuItems() if hasattr(parm.parmTemplate(), "menuItems") else ()
        if choices and value not in choices:
            raise RuntimeError(f"BLOCKED_NODE_SCHEMA: {name} has no token {value!r}")
    if isinstance(value, tuple):
        for component in parm:
            component.deleteAllKeyframes()
    else:
        parm.deleteAllKeyframes()
    parm.set(value)


def parameter_snapshot(node):
    values = {}
    for parm in node.parms():
        try:
            value = parm.eval()
            if isinstance(value, (str, int, float)):
                values[parm.name()] = {"label": parm.parmTemplate().label(), "value": value}
        except Exception:
            continue  # Non-value parameters are not needed to reproduce a cook.
    return values


def bind_recipe(parm, expression):
    """Keep native settings tied to the same editable embedded recipe as SOPs."""
    import hou
    prefix = "__import__('json').loads(hou.pwd().parent().evalParm('recipe_json'))"
    parm.setExpression(expression.replace("RECIPE", prefix), language=hou.exprLanguage.Python)


def check_cook(node):
    node.cook(force=True)
    if node.errors():
        raise RuntimeError(f"BLOCKED_COOK: {node.path()}: {node.errors()}")
    return node.geometry()


def extract(node, recipe, sop):
    geo = check_cook(node)
    height = sop.named_volume(geo, "height")
    positions, lookup = sop.world_grid(height, recipe)
    values = height.allVoxels()
    heights = [[values[i] for i in row] for row in lookup]
    masks = {}
    for key in MATERIAL_PALETTE:
        layer = sop.named_volume(geo, key)
        layer_positions, _ = sop.world_grid(layer, recipe)
        if layer_positions != positions:
            raise RuntimeError("BLOCKED_MASK_TRANSFORM: " + key)
        data = layer.allVoxels()
        masks[key] = [[data[i] for i in row] for row in lookup]
    width, depth = recipe["resolution"]
    materials = [[max(MATERIAL_PALETTE, key=lambda k: masks[k][r][c])
                  for c in range(width)] for r in range(depth)]
    return heights, materials, masks


def output_preset(parent, source, recipe):
    """Save an inspected native export preset; deliberately do not press Execute."""
    result = {"execution_status": "NOT_RUN", "purpose": "native HeightField Output reference preset"}
    import hou
    if "heightfield_output" not in hou.sopNodeTypeCategory().nodeTypes():
        result["configuration_status"] = "BLOCKED_NODE_UNAVAILABLE"
        return result
    node = parent.createNode("heightfield_output", "HF_OUTPUT_REFERENCE_NOT_RUN", exact_type_name=True)
    node.setInput(0, source)
    result["node"] = node.path()
    lo, hi = [x * recipe["meters_per_stud"] for x in recipe["height_range_studs"]]
    preset = {
        "output": "$HIP/native_reference/heightmap.png", "out_type": "packed",
        "out_format": "single", "output_type": "i16", "specify_res": 1,
        "resolution": tuple(recipe["resolution"]), "trange": 0, "tile_output": 0,
        "xflip": 0, "yflip": 0, "flop": 0, "fill_red_channel": 1,
        "red_channel": "height", "red_out_range": "manual",
        "red_from_range": (lo, hi), "red_to_range": (0.0, 1.0),
        "fill_green_channel": 0, "fill_blue_channel": 0,
    }
    missing = []
    for name, value in preset.items():
        try:
            set_known(node, name, value)
        except Exception as exc:
            missing.append(str(exc))
    result["configuration_status"] = "SCHEMA_MATCHED" if not missing else "BLOCKED_NODE_SCHEMA"
    result["schema_errors"] = missing
    result["parameters"] = parameter_snapshot(node)
    result["orientation_status"] = "NOT_CALIBRATED"
    node.setComment("REFERENCE ONLY: not executed; format/orientation must be compared against canonical exports.")
    return result


def build(config_path, output):
    import hou
    import h00_sop as sop
    repo = Path(__file__).resolve().parents[2]
    output = output.resolve()
    if output == repo or repo in output.parents:
        raise RuntimeError("BLOCKED_OUTPUT_IN_REPO: use a separate work directory")
    if any("yacs" in part.lower() or "yetanothercyclingsim" in part.lower() for part in output.parts):
        raise RuntimeError("BLOCKED_OUTPUT_IN_YACS: choose a separate MathCity work directory")
    if output.drive.upper() == "C:":
        raise RuntimeError("BLOCKED_OUTPUT_SYSTEM_DRIVE: use the separate work drive")
    if any(output.glob("MathCity_H00_Terrain.*")) or any((output / x).exists() for x in ("manifest.json", "terrain", "h00.bgeo.sc")):
        raise RuntimeError("BLOCKED_OUTPUT_EXISTS: choose a new run directory")
    recipe = json.loads(config_path.read_text(encoding="utf-8-sig"))
    validate_recipe(recipe)
    validate_features(recipe)
    if recipe["resolution"][0] != recipe["resolution"][1]:
        raise RuntimeError("BLOCKED_RECIPE: this H00 native preset requires a square grid")
    erosion = recipe["erosion"]
    if erosion["node_type"] != "heightfield_erode::3.0":
        raise RuntimeError("BLOCKED_RECIPE: only the inspected Erode 3.0 contract is supported")
    if any(isinstance(erosion[key], bool) or not isinstance(erosion[key], int) for key in ("start_frame", "freeze_frame")) or not 1 <= erosion["start_frame"] < erosion["freeze_frame"] <= 120:
        raise RuntimeError("BLOCKED_RECIPE: invalid or unbounded erosion frames")
    spacing = recipe["studs_per_pixel"] * recipe["meters_per_stud"]
    if not math.isfinite(erosion["feature_size_m"]) or erosion["feature_size_m"] < 3 * spacing:
        raise RuntimeError("BLOCKED_RECIPE: erosion feature size below native 3-voxel minimum")
    if hou.isUIAvailable() or hou.node("/obj").children():
        raise RuntimeError("BLOCKED_EXISTING_SESSION: launch a fresh hython process")
    license_category = hou.licenseCategory()
    if license_category == hou.licenseCategoryType.Indie:
        extension = ".hiplc"
    elif license_category == hou.licenseCategoryType.Commercial:
        extension = ".hip"
    else:
        raise RuntimeError("BLOCKED_LICENSE_CATEGORY: " + str(license_category))
    required = ("heightfield", "python", "null", erosion["node_type"])
    types = hou.sopNodeTypeCategory().nodeTypes()
    if any(name not in types for name in required):
        raise RuntimeError("BLOCKED_NODE_UNAVAILABLE: " + repr([name for name in required if name not in types]))
    output.mkdir(parents=True, exist_ok=True)
    parent = hou.node("/obj").createNode("geo", "MathCity_H00_Terrain", run_init_scripts=False)
    erode = parent.createNode(erosion["node_type"], "HF_EROSION", exact_type_name=True)
    # Discover the whole native contract before setting scene controls or cooking
    # the source/macro terrain. An API mismatch produces one complete diagnostic.
    resolve_erode_contract(erode)
    parent.addSpareParmTuple(hou.StringParmTemplate("recipe_json", "H00 Recipe JSON", 1,
                                                  default_value=(json.dumps(recipe, sort_keys=True),)))
    parent.setComment("Synthetic H00; Houdini master; no production MathCity map or Siedlce geography.")
    resolved, erode_readback = configure_erode(erode, recipe)
    source = parent.createNode("heightfield", "HF_BASE", exact_type_name=True)
    span = recipe["resolution"][0] * spacing
    center_x, center_z = [v * recipe["meters_per_stud"] for v in recipe["region_center_xz_studs"]]
    for name, value in {"orient": "zx", "sampling": "center", "initialheight": 0,
                        "initialmask": 0, "divisionmode": "maxaxis", "gridsamples": recipe["resolution"][0],
                        "scale": 1, "size": (span, span), "t": (center_x, 0.0, center_z)}.items():
        set_known(source, name, value)
    bind_recipe(source.parm("gridsamples"), "RECIPE['resolution'][0]")
    for i, parm in enumerate(source.parmTuple("size")):
        bind_recipe(parm, f"RECIPE['resolution'][{i}] * RECIPE['studs_per_pixel'] * RECIPE['meters_per_stud']")
    for i, axis in enumerate((0, 2)):
        bind_recipe(source.parmTuple("t")[axis], f"RECIPE['region_center_xz_studs'][{i}] * RECIPE['meters_per_stud']")
    sop.world_grid(sop.named_volume(check_cook(source), "height"), recipe)
    code = Path(sop.__file__).read_text(encoding="utf-8")
    macro = parent.createNode("python", "HF_MACRO_SHAPING", exact_type_name=True)
    macro.setInput(0, source)
    set_known(macro, "python", code + "\ncook('macro')\n")
    before = sop.named_volume(check_cook(macro), "height").allVoxels()
    erode.setInput(0, macro)
    hou.setFrame(erosion["freeze_frame"])
    after = sop.named_volume(check_cook(erode), "height").allVoxels()
    if len(after) != len(before):
        raise RuntimeError("BLOCKED_EROSION_RESOLUTION")
    delta = [abs(a - b) for a, b in zip(after, before)]
    if not all(math.isfinite(v) for v in after) or max(delta) <= 1e-6:
        raise RuntimeError("BLOCKED_EROSION_NO_VALID_CHANGE")
    final = parent.createNode("python", "HF_CONSTRAINTS_AND_MATERIALS", exact_type_name=True)
    final.setInput(0, erode)
    set_known(final, "python", code + "\ncook('constraints')\n")
    out = parent.createNode("null", "OUT_H00", exact_type_name=True)
    out.setInput(0, final)
    heights, materials, masks = extract(out, recipe, sop)
    native_output = output_preset(parent, out, recipe)
    out.setDisplayFlag(True)
    out.setRenderFlag(True)
    parent.layoutChildren()
    cache_path = output / "h00.bgeo.sc"
    out.geometry().saveToFile(str(cache_path))
    hip_path = output / ("MathCity_H00_Terrain" + extension)
    hou.hipFile.save(str(hip_path), save_to_recent_files=False)
    if not hip_path.is_file() or Path(hou.hipFile.path()).resolve() != hip_path:
        raise RuntimeError("BLOCKED_NATIVE_HIP_SAVE: actual filename differs; do not rename license formats")
    exports = export_terrain(output, recipe, heights, materials, masks)
    sources = [Path(__file__), Path(sop.__file__), Path(__file__).with_name("terrain_contract.py")]
    manifest = {
        "schema_version": 1, "packet_id": "H00", "recipe": recipe,
        "provenance": {"generator": "Houdini", "source_recipe_sha256": hashlib.sha256(config_path.read_bytes()).hexdigest(),
                       "source_files": {p.resolve().relative_to(repo).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}},
        "native": {"houdini_version": hou.applicationVersionString(), "license_category": str(license_category),
                   "hip_file": file_record(hip_path, output), "cache_file": file_record(cache_path, output),
                   "output_node": out.path(), "embedded_recipe_parameter": parent.path() + "/recipe_json",
                   "node_types": {n.name(): n.type().name() for n in parent.children()},
                   "source_parameters": parameter_snapshot(source), "erosion_parameters": parameter_snapshot(erode),
                   "erosion_resolved_names": resolved, "erosion_control_readback": erode_readback,
                   "erosion_changed_sample_count": sum(x > 1e-6 for x in delta),
                   "erosion_delta_max_m": max(delta), "native_output_reference": native_output,
                   "labs_used": False, "warnings": {n.name(): list(n.warnings()) for n in parent.children() if n.warnings()}},
        "exports": exports,
        "exporter": "Houdini cooked Volume -> canonical PNG compatibility adapter",
        "statuses": {"HOUDINI_COOK": "PASS", "NATIVE_OUTPUT_EXECUTION": "NOT_RUN", "NATIVE_REOPEN": "NOT_RUN",
                     "ROBLOX_IMPORT": "NOT_RUN", "STUDIO_PASS": "NOT_RUN", "DEVICE_PASS": "NOT_RUN"},
    }
    write_new_json(output / "manifest.json", manifest)
    return {"status": "HOUDINI_COOK_PASS", "manifest": str(output / "manifest.json"),
            "ROBLOX_IMPORT": "NOT_RUN", "DEVICE_PASS": "NOT_RUN"}


def verify_run(output):
    """Fresh-process native reopen, with complete height/mask equality checks."""
    import hou
    import h00_sop as sop
    if (output / "reopen_verification.json").exists():
        raise RuntimeError("BLOCKED_OUTPUT_EXISTS: preserve the previous reopen result")
    if hou.isUIAvailable() or hou.node("/obj").children():
        raise RuntimeError("BLOCKED_EXISTING_SESSION: reopen requires a fresh hython process")
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    hip_path = checked_artifact(output, manifest["native"]["hip_file"])
    samples_path = checked_artifact(output, manifest["exports"]["height_samples"])
    expected_recipe = manifest["recipe"]
    hou.hipFile.load(str(hip_path), suppress_save_prompt=True, ignore_load_warnings=False)
    out = hou.node(manifest["native"]["output_node"])
    if out is None or json.loads(out.parent().evalParm("recipe_json")) != expected_recipe:
        raise RuntimeError("BLOCKED_REOPEN_RECIPE_OR_OUTPUT")
    heights, materials, masks = extract(out, expected_recipe, sop)
    actual_samples = b"".join(struct.pack("<f", value) for row in heights for value in row)
    expected_samples = samples_path.read_bytes()
    differences = []
    if actual_samples != expected_samples:
        differences.append("height_float32_samples")
    colormap = read_png(checked_artifact(output, manifest["exports"]["colormap"]))
    expected_colors = [bytes(v for key in row for v in MATERIAL_PALETTE[key]) for row in materials]
    if colormap["rows"] != expected_colors:
        differences.append("material_colormap")
    for key, rows in masks.items():
        image = read_png(checked_artifact(output, manifest["exports"]["masks"][key]))
        if image["rows"] != [bytes(round(value * 255) for value in row) for row in rows]:
            differences.append("mask_" + key)
    result = {"schema_version": 1, "status": "PASS" if not differences else "FAIL",
              "scope": "fresh-process native reopen on this installation; no Studio result",
              "hip_sha256": manifest["native"]["hip_file"]["sha256"],
              "houdini_version": hou.applicationVersionString(),
              "same_houdini_version": hou.applicationVersionString() == manifest["native"]["houdini_version"],
              "comparison": "exact all float32 heights and 5 masks/material pixels", "differences": differences,
              "sample_count": len(actual_samples) // 4, "ROBLOX_IMPORT": "NOT_RUN"}
    write_new_json(output / "reopen_verification.json", result)
    if differences:
        raise RuntimeError("BLOCKED_REOPEN_MISMATCH: " + ", ".join(differences))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify-run", type=Path)
    args = parser.parse_args()
    if args.verify_run and (args.config or args.output):
        parser.error("--verify-run cannot be combined with --config/--output")
    if not args.verify_run and not (args.config and args.output):
        parser.error("build requires --config and --output")
    try:
        result = verify_run(args.verify_run.resolve()) if args.verify_run else build(args.config.resolve(), args.output)
        print(json.dumps(result, ensure_ascii=False, allow_nan=False))
        return 0
    except Exception as exc:
        traceback.print_exc(file=sys.stderr)
        print(json.dumps({"status": "BLOCKED_H00", "reason": str(exc), "ROBLOX_IMPORT": "NOT_RUN"}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
