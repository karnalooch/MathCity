"""Embedded Python SOP operations; executed only inside native Houdini.

The base and erosion nodes remain SideFX HeightField SOPs. This code shapes
their real volume primitives and creates material layers by cloning a native
heightfield primitive, preserving its transform and heightfield flag.
"""
import json
import math

import hou

MATERIAL_KEYS = ("grass", "ground", "sand", "rock", "asphalt")


def smoothstep(a, b, x):
    t = max(0.0, min(1.0, (x - a) / (b - a)))
    return t * t * (3.0 - 2.0 * t)


def gaussian(x, z, feature):
    cx, cz = feature["center_xz_m"]
    rx, rz = feature["radius_xz_m"]
    return math.exp(-((x - cx) / rx) ** 2 - ((z - cz) / rz) ** 2)


def named_volume(geo, name):
    matches = [p for p in geo.prims() if isinstance(p, hou.Volume)
               and p.attribValue("name") == name]
    if len(matches) != 1 or not matches[0].isHeightField():
        raise RuntimeError("BLOCKED_HEIGHTFIELD_LAYER: " + name)
    return matches[0]


def voxel_positions(volume):
    """Return positions in the documented allVoxels x-fastest local order."""
    nx, ny, nz = volume.resolution()
    return [tuple(volume.indexToPos((x, y, z)))
            for z in range(nz) for y in range(ny) for x in range(nx)]


def world_grid(volume, recipe):
    """Map actual voxel centers onto the fixed PNG X/Z grid; reject rotation/drift."""
    width, depth = recipe["resolution"]
    spacing = recipe["studs_per_pixel"] * recipe["meters_per_stud"]
    cx, cz = [v * recipe["meters_per_stud"] for v in recipe["region_center_xz_studs"]]
    min_x, min_z = cx - width * spacing / 2, cz - depth * spacing / 2
    positions = voxel_positions(volume)
    if len(positions) != width * depth:
        raise RuntimeError("BLOCKED_GRID_RESOLUTION: " + repr(volume.resolution()))
    lookup = [[None for _ in range(width)] for _ in range(depth)]
    for local_index, (x, y, z) in enumerate(positions):
        column = round((x - min_x) / spacing - 0.5)
        row = round((z - min_z) / spacing - 0.5)
        if not (0 <= column < width and 0 <= row < depth):
            raise RuntimeError("BLOCKED_GRID_EXTENT")
        expected = (min_x + (column + 0.5) * spacing, min_z + (row + 0.5) * spacing)
        if max(abs(x - expected[0]), abs(z - expected[1]), abs(y)) > spacing * 1e-4:
            raise RuntimeError("BLOCKED_GRID_ORIENTATION_OR_SAMPLING")
        if lookup[row][column] is not None:
            raise RuntimeError("BLOCKED_GRID_DUPLICATE")
        lookup[row][column] = local_index
    if any(i is None for row in lookup for i in row):
        raise RuntimeError("BLOCKED_GRID_INCOMPLETE")
    return positions, lookup


def shape_base(geo, recipe):
    volume = named_volume(geo, "height")
    positions, _ = world_grid(volume, recipe)
    f = recipe["features"]
    seed_phase = (recipe["seed"] % 997) / 997 * 2 * math.pi
    values = []
    for x, _, z in positions:
        height = f["base_height_m"] + f["hill"]["height_m"] * gaussian(x, z, f["hill"])
        height -= f["valley"]["depth_m"] * gaussian(x, z, f["valley"])
        # Wide natural bank plus low-amplitude relief; no pixel-level noise.
        height += 4 * smoothstep(-16, -4, z + 0.12 * x)
        height += 0.75 * math.sin(x / 17 + seed_phase) * math.cos(z / 23)
        basin = f["basin"]
        bx, bz = basin["center_xz_m"]
        rx, rz = basin["radius_xz_m"]
        distance = math.sqrt(((x - bx) / rx) ** 2 + ((z - bz) / rz) ** 2)
        basin_height = basin["bed_height_m"] + (basin["shore_height_m"] - basin["bed_height_m"]) * min(1, distance * distance)
        weight = 1 - smoothstep(0.82, 1.2, distance)
        height = height * (1 - weight) + basin_height * weight
        values.append(height)
    volume.setAllVoxels(values)


def duplicate_layer(geo, name, values):
    """Clone a real HF layer rather than creating an unflagged 3D volume."""
    if any(p.attribValue("name") == name for p in geo.prims()):
        raise RuntimeError("BLOCKED_DUPLICATE_LAYER: " + name)
    clone = hou.Geometry(geo)
    height = named_volume(clone, "height")
    clone.deletePrims([p for p in clone.prims() if p != height])
    height.setAttribValue("name", name)
    height.setAllVoxels(values)
    geo.merge(clone)


def constrain_and_mask(geo, recipe):
    volume = named_volume(geo, "height")
    positions, lookup = world_grid(volume, recipe)
    values = list(volume.allVoxels())
    features = recipe["features"]
    road, pad = features["road"], features["pad"]
    road_weights, pad_weights = [], []
    for i, (x, _, z) in enumerate(positions):
        road_weight = 1 - smoothstep(road["half_width_m"], road["half_width_m"] + road["blend_m"], abs(z - road["center_z_m"]))
        target = road["height_at_x0_m"] + x * road["grade"]
        values[i] = values[i] * (1 - road_weight) + target * road_weight
        px, pz = pad["center_xz_m"]
        hx, hz = pad["half_size_xz_m"]
        outside = max(abs(x - px) - hx, abs(z - pz) - hz)
        pad_weight = 1 - smoothstep(0, pad["blend_m"], outside)
        values[i] = values[i] * (1 - pad_weight) + pad["height_m"] * pad_weight
        road_weights.append(road_weight)
        pad_weights.append(pad_weight)
    volume.setAllVoxels(values)
    width, depth = recipe["resolution"]
    spacing = recipe["studs_per_pixel"] * recipe["meters_per_stud"]
    layers = {key: [0.0] * len(values) for key in MATERIAL_KEYS}
    for row in range(depth):
        for column in range(width):
            i = lookup[row][column]
            left, right = max(0, column - 1), min(width - 1, column + 1)
            back, front = max(0, row - 1), min(depth - 1, row + 1)
            dx = (values[lookup[row][right]] - values[lookup[row][left]]) / ((right - left) * spacing)
            dz = (values[lookup[front][column]] - values[lookup[back][column]]) / ((front - back) * spacing)
            slope = math.hypot(dx, dz)
            if road_weights[i] >= 1 - 1e-8:
                key = "asphalt"
            elif pad_weights[i] >= 1 - 1e-8:
                key = "ground"
            elif values[i] < features["basin"]["shore_height_m"] + 2:
                key = "sand"
            elif slope > 0.65 or values[i] > 30:
                key = "rock"
            elif slope > 0.3:
                key = "ground"
            else:
                key = "grass"
            layers[key][i] = 1.0
    for name, data in layers.items():
        duplicate_layer(geo, name, data)


def cook(mode):
    node = hou.pwd()
    recipe = json.loads(node.parent().evalParm("recipe_json"))
    geo = node.geometry()
    geo.clear()
    geo.merge(node.inputs()[0].geometry())
    if mode == "macro":
        shape_base(geo, recipe)
    elif mode == "constraints":
        constrain_and_mask(geo, recipe)
    else:
        raise RuntimeError("Unknown H00 SOP mode")
