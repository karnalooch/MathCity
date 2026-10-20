"""Read-only Houdini capability inventory; run with the existing hython.

This does not open a HIP, cook a graph, inspect license keys, install HDAs or
connect to Roblox. The report describes the actual process, not a target version.
"""
from __future__ import annotations

import argparse
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path


def inventory() -> dict:
    import hou

    types = hou.sopNodeTypeCategory().nodeTypes()
    wanted = ("heightfield", "volumewrangle")
    selected = {}
    for name, node_type in sorted(types.items()):
        if not (any(token in name.lower() for token in wanted) or name in ("python", "null")):
            continue
        entry = {"description": node_type.description(), "parameters": []}
        try:
            for parm in node_type.parmTemplateGroup().entriesWithoutFolders():
                parameter = {
                    "name": parm.name(),
                    "label": parm.label(),
                    "type": str(parm.type()),
                    "components": parm.numComponents(),
                }
                # Read declared tokens/labels only; do not execute dynamic menus.
                for method_name, key in (("menuItems", "menu_items"), ("menuLabels", "menu_labels")):
                    method = getattr(parm, method_name, None)
                    if callable(method):
                        try:
                            parameter[key] = list(method())
                        except Exception as exc:
                            parameter[key + "_error"] = str(exc)
                entry["parameters"].append(parameter)
        except Exception as exc:
            entry["parameter_inventory_error"] = str(exc)
        definition = node_type.definition()
        if definition is not None:
            entry["definition_library"] = definition.libraryFilePath()
        selected[name] = entry

    labs = sorted(name for name in types if name.lower().startswith("labs::"))
    return {
        "schema_version": 1,
        "packet_id": "P00",
        "recorded_utc": datetime.now(timezone.utc).isoformat(),
        "status": "HOUDINI_INSPECTED",
        "python_executable": sys.executable,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "houdini_version": hou.applicationVersionString(),
        "houdini_version_tuple": list(hou.applicationVersion()),
        "license_category": str(hou.licenseCategory()),
        "sop_node_types": selected,
        "labs": {
            "status": "DETECTED" if labs else "NOT_DETECTED_IN_THIS_PROCESS",
            "registered_sop_count": len(labs),
            "registered_sop_names": labs,
        },
        "cook_status": "NOT_RUN",
        "studio_status": "NOT_RUN",
        "device_status": "NOT_RUN",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.exists():
        parser.error("Refusing to overwrite an existing inventory; use a new run directory.")
    try:
        result = inventory()
        exit_code = 0
    except Exception as exc:
        result = {
            "schema_version": 1,
            "packet_id": "P00",
            "recorded_utc": datetime.now(timezone.utc).isoformat(),
            "status": "BLOCKED_HOUDINI_INSPECTION",
            "error": str(exc),
            "python_executable": sys.executable,
            "cook_status": "NOT_RUN",
            "studio_status": "NOT_RUN",
            "device_status": "NOT_RUN",
        }
        exit_code = 1
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(result["status"])
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
