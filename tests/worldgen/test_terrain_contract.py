"""Byte-contract regressions. These tests DO NOT run Houdini or Roblox."""
import struct
import sys
import tempfile
import unittest
import zlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "worldgen"))
from terrain_contract import (MATERIAL_PALETTE, checked_artifact, export_terrain,
                              quantize_height, read_png, sample_position, validate_recipe)
from validate_h00 import validate_exports


def fixture():
    recipe = {"schema_version": 1, "recipe_id": "TEST_FIXTURE_NOT_A_HOUDINI_RUN", "resolution": [8, 8],
              "studs_per_pixel": 4, "meters_per_stud": 0.28,
              "height_range_studs": [-64, 256], "region_center_xz_studs": [0, 0]}
    heights = [[float(x + z * 2) for x in range(8)] for z in range(8)]
    keys = list(MATERIAL_PALETTE)
    materials = [[keys[(x + z * 3) % 5] for x in range(8)] for z in range(8)]
    masks = {key: [[float(cell == key) for cell in row] for row in materials] for key in keys}
    return recipe, heights, materials, masks


class TerrainContractTests(unittest.TestCase):
    def export(self, folder):
        recipe, heights, materials, masks = fixture()
        exports = export_terrain(folder, recipe, heights, materials, masks)
        return {"recipe": recipe, "exports": exports}

    def test_full_file_contract_and_fixed_transform(self):
        with tempfile.TemporaryDirectory() as folder:
            manifest = self.export(folder)
            checked = validate_exports(folder, manifest)
            self.assertEqual(checked["sample_count"], 64)
            self.assertEqual(checked["import_settings"]["position_studs"], [0, 96, 0])
            self.assertEqual(checked["import_settings"]["size_studs"], [32, 320, 32])
            self.assertLessEqual(checked["max_height_quantization_error_studs"], 320 / 65535 / 2)

    def test_png_independent_wire_format(self):
        # Check signature/IHDR/decompressed row bytes without calling our PNG reader.
        with tempfile.TemporaryDirectory() as folder:
            self.export(folder)
            data = (Path(folder) / "terrain/heightmap.png").read_bytes()
            self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
            self.assertEqual(struct.unpack(">IIBBBBB", data[16:29]), (8, 8, 16, 0, 0, 0, 0))
            size = int.from_bytes(data[33:37], "big")
            raw = zlib.decompress(data[41:41 + size])
            self.assertEqual(len(raw), 8 * 17)
            self.assertEqual(raw[0], 0)
            self.assertEqual(int.from_bytes(raw[1:3], "big"), 13107)  # (0 - -64)/320 * 65535

    def test_fixed_range_does_not_shift_between_exports(self):
        recipe, *_ = fixture()
        self.assertEqual(quantize_height(0, recipe), 13107)
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            self.export(first)
            recipe, heights, materials, masks = fixture()
            heights[7][7] = 40.0  # Change one hill, preserving every other native sample.
            export_terrain(second, recipe, heights, materials, masks)
            a = read_png(Path(first) / "terrain/heightmap.png")
            b = read_png(Path(second) / "terrain/heightmap.png")
            self.assertEqual(a["rows"][0], b["rows"][0])
            self.assertNotEqual(a["rows"][7], b["rows"][7])
        with self.assertRaisesRegex(ValueError, "no auto-remap"):
            quantize_height(1000, recipe)

    def test_cell_centers_and_axis_asymmetry(self):
        recipe, *_ = fixture()
        self.assertEqual(sample_position(0, 0, 0, recipe), [-14, 0, -14])
        self.assertEqual(sample_position(7, 0, 0, recipe), [14, 0, -14])
        self.assertEqual(sample_position(0, 7, 0, recipe), [-14, 0, 14])

    def test_float32_inclusive_bounds_and_real_overflow(self):
        recipe, heights, materials, masks = fixture()
        lo, hi = [x * recipe["meters_per_stud"] for x in recipe["height_range_studs"]]
        lo_f32, hi_f32 = [struct.unpack("<f", struct.pack("<f", x))[0] for x in (lo, hi)]
        self.assertEqual(quantize_height(lo_f32, recipe), 0)
        self.assertEqual(quantize_height(hi_f32, recipe), 65535)
        for outside in (lo_f32 - 0.001, hi_f32 + 0.001):
            with self.assertRaisesRegex(ValueError, "no auto-remap"):
                quantize_height(outside, recipe)
        heights[0][0], heights[7][7] = lo, hi
        with tempfile.TemporaryDirectory() as folder:
            exports = export_terrain(folder, recipe, heights, materials, masks)
            validate_exports(folder, {"recipe": recipe, "exports": exports})

    def test_reject_nan_and_invalid_units(self):
        recipe, *_ = fixture()
        for value in [float("nan"), float("inf"), True]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                quantize_height(value, recipe)
        recipe["studs_per_pixel"] = 1
        with self.assertRaises(ValueError):
            validate_recipe(recipe)

    def test_reject_flat_terrain(self):
        recipe, heights, materials, masks = fixture()
        with tempfile.TemporaryDirectory() as folder, self.assertRaisesRegex(ValueError, "flat"):
            export_terrain(folder, recipe, [[0.0] * 8 for _ in range(8)], materials, masks)

    def test_reject_inconsistent_material_partition(self):
        recipe, heights, materials, masks = fixture()
        masks["grass"][0][0] = 0.5
        with tempfile.TemporaryDirectory() as folder, self.assertRaises(ValueError):
            export_terrain(folder, recipe, heights, materials, masks)

    def test_reject_missing_material_class(self):
        recipe, heights, materials, masks = fixture()
        materials = [["grass"] * 8 for _ in range(8)]
        masks = {key: [[float(key == "grass")] * 8 for _ in range(8)] for key in MATERIAL_PALETTE}
        with tempfile.TemporaryDirectory() as folder, self.assertRaisesRegex(ValueError, "five"):
            export_terrain(folder, recipe, heights, materials, masks)

    def test_reject_corruption_and_rehashed_png_crc(self):
        with tempfile.TemporaryDirectory() as folder:
            manifest = self.export(folder)
            path = Path(folder) / "terrain/heightmap.png"
            data = bytearray(path.read_bytes()); data[42] ^= 1; path.write_bytes(data)
            with self.assertRaisesRegex(ValueError, "checksum"):
                validate_exports(folder, manifest)
            with self.assertRaisesRegex(ValueError, "CRC"):
                read_png(path)

    def test_reject_tampered_metadata(self):
        with tempfile.TemporaryDirectory() as folder:
            manifest = self.export(folder)
            manifest["exports"]["import_settings"]["position_studs"][1] = 0
            with self.assertRaisesRegex(ValueError, "transform"):
                validate_exports(folder, manifest)

    def test_reject_artifact_escape(self):
        with tempfile.TemporaryDirectory() as folder, self.assertRaisesRegex(ValueError, "escapes"):
            checked_artifact(folder, {"path": "../outside.png", "bytes": 0, "sha256": "0" * 64})

    def test_reject_overwrite_and_detect_probe_rotation(self):
        with tempfile.TemporaryDirectory() as folder:
            manifest = self.export(folder)
            with self.assertRaisesRegex(ValueError, "already exists"):
                self.export(folder)
            manifest["exports"]["probes"][0]["position_studs"][0] *= -1
            with self.assertRaisesRegex(ValueError, "probe coordinates"):
                validate_exports(folder, manifest)


if __name__ == "__main__":
    unittest.main()
