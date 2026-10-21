"""Regression of the observed Erode 3.0 interface; no native Houdini PASS.

Fixture provenance: Houdini 22.0.466, run
H00_20261020T220649684Z_82216fe0, native houdini_environment.json supplied
2026-10-21 (Europe/Warsaw). Only the five required declarations are reproduced.
"""
from __future__ import annotations

import copy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "worldgen"))
import build_h00 as builder


OBSERVED_ERODE_PARAMETERS = [
    {"name": "dofreeze", "label": "Do Freeze", "type": "parmTemplateType.Toggle", "components": 1},
    {"name": "freezeframe", "label": "Freeze at Frame", "type": "parmTemplateType.Int", "components": 1},
    {"name": "startframe", "label": "Start Frame", "type": "parmTemplateType.Int", "components": 1},
    {"name": "seed", "label": "Random Seed", "type": "parmTemplateType.Float", "components": 1},
    {"name": "erosionscale", "label": "Erosion Feature Size", "type": "parmTemplateType.Float", "components": 1},
]
RECIPE = {"seed": 20261020, "erosion": {"start_frame": 1, "freeze_frame": 12, "feature_size_m": 6.72}}


class Template:
    def __init__(self, declaration):
        self.declaration = declaration

    def type(self):
        return self.declaration["type"]

    def numComponents(self):
        return self.declaration["components"]

    def label(self):
        raise AssertionError("UI labels must not select native controls")


class Parm:
    def __init__(self, node, name):
        self.node, self.name = node, name
        self.value, self.expression = None, None

    def deleteAllKeyframes(self):
        self.node.events.append(("delete_keyframes", self.name))
        self.expression = None

    def set(self, value):
        self.node.events.append(("set", self.name, value))
        self.value = value

    def eval(self):
        self.node.events.append(("eval", self.name))
        if self.name in self.node.readback_overrides:
            return self.node.readback_overrides[self.name]
        if self.expression is not None:
            # Expressions are fixed strings authored by configure_erode.
            return eval(self.expression, {"__builtins__": {}}, {"RECIPE": self.node.recipe})
        return self.value


class ParmTuple:
    def __init__(self, declaration, parm):
        self.template, self.parm = Template(declaration), parm

    def parmTemplate(self):
        return self.template

    def __len__(self):
        return self.template.numComponents()


class Node:
    def __init__(self, parameters=None, node_type="heightfield_erode::3.0", recipe=None, overrides=None):
        self.node_type = node_type
        self.recipe = copy.deepcopy(RECIPE if recipe is None else recipe)
        self.readback_overrides = {} if overrides is None else overrides
        self.events = []
        self.parameters, self.tuples = {}, {}
        for declaration in OBSERVED_ERODE_PARAMETERS if parameters is None else parameters:
            name = declaration["name"]
            self.parameters[name] = Parm(self, name)
            self.tuples[name] = ParmTuple(declaration, self.parameters[name])

    def type(self):
        return self

    def name(self):
        return self.node_type

    def parm(self, name):
        return self.parameters.get(name)

    def parmTuple(self, name):
        return self.tuples.get(name)

    def cook(self, *args, **kwargs):
        raise AssertionError("control binding must not cook the terrain")


def record_binding(parm, expression):
    parm.node.events.append(("bind", parm.name, expression))
    parm.expression = expression


class ErodeContractTests(unittest.TestCase):
    def configure(self, node):
        with patch.object(builder, "bind_recipe", side_effect=record_binding):
            return builder.configure_erode(node, node.recipe)

    def test_actual_22_0_466_schema_resolves_and_keeps_float_seed(self):
        node = Node()
        resolved, values = self.configure(node)
        self.assertEqual(resolved, {
            "Freeze": "dofreeze", "Freeze at Frame": "freezeframe", "Start Frame": "startframe",
            "Random Seed": "seed", "Erosion Feature Size": "erosionscale",
        })
        self.assertEqual(values, {"Freeze": 1, "Freeze at Frame": 12, "Start Frame": 1,
                                  "Random Seed": 20261020, "Erosion Feature Size": 6.72})
        self.assertEqual(node.parm("dofreeze").value, 1)
        self.assertIsInstance(node.recipe["seed"], int)

    def test_labels_are_irrelevant_to_selection(self):
        schema = copy.deepcopy(OBSERVED_ERODE_PARAMETERS)
        for parameter in schema:
            parameter["label"] = "A changed or translated UI label"
        resolved = builder.resolve_erode_contract(Node(parameters=schema))
        self.assertEqual(resolved["Freeze"], "dofreeze")

    def test_all_schema_errors_are_reported_before_any_change(self):
        schema = copy.deepcopy(OBSERVED_ERODE_PARAMETERS)
        schema = [p for p in schema if p["name"] not in ("dofreeze", "freezeframe")]
        for parameter in schema:
            if parameter["name"] == "startframe":
                parameter["type"] = "parmTemplateType.String"
            elif parameter["name"] == "seed":
                parameter["type"] = "parmTemplateType.Int"
            elif parameter["name"] == "erosionscale":
                parameter["components"] = 3
        node = Node(parameters=schema)
        with self.assertRaises(RuntimeError) as caught:
            self.configure(node)
        error = str(caught.exception)
        for name in ("dofreeze", "freezeframe", "startframe", "seed", "erosionscale"):
            self.assertIn(name, error)
        self.assertEqual(node.events, [])

    def test_wrong_native_type_is_rejected_without_mutation(self):
        node = Node(node_type="heightfield_erode::2.0")
        with self.assertRaisesRegex(RuntimeError, "BLOCKED_NODE_SCHEMA.*node type"):
            self.configure(node)
        self.assertEqual(node.events, [])

    def test_missing_scalar_handle_is_rejected_without_mutation(self):
        node = Node()
        del node.parameters["seed"]
        with self.assertRaisesRegex(RuntimeError, "missing scalar parameter seed"):
            self.configure(node)
        self.assertEqual(node.events, [])

    def test_all_readback_errors_are_reported(self):
        node = Node(overrides={"dofreeze": 0, "freezeframe": 13, "startframe": 2,
                               "seed": 20261021.0, "erosionscale": float("nan")})
        with self.assertRaises(RuntimeError) as caught:
            self.configure(node)
        error = str(caught.exception)
        self.assertIn("BLOCKED_EROSION_READBACK", error)
        for name in ("dofreeze", "freezeframe", "startframe", "seed", "erosionscale"):
            self.assertIn(name, error)

    def test_large_seed_must_match_exactly(self):
        recipe = copy.deepcopy(RECIPE)
        recipe["seed"] = 2**31 - 1
        node = Node(recipe=recipe, overrides={"seed": float(2**31 - 2)})
        with self.assertRaisesRegex(RuntimeError, "BLOCKED_EROSION_READBACK.*seed"):
            self.configure(node)

    def test_native_float_seed_readback_is_accepted_without_changing_recipe(self):
        node = Node(overrides={"seed": 20261020.0})
        _, readback = self.configure(node)
        self.assertEqual(readback["Random Seed"], 20261020.0)
        self.assertIsInstance(node.recipe["seed"], int)

    def test_only_feature_scale_accepts_small_float_roundoff(self):
        node = Node(overrides={"erosionscale": 6.71999979019165})
        self.configure(node)
        for role, value in (("erosionscale", 6.721), ("seed", 20261020.000001), ("freezeframe", 12.000001)):
            with self.subTest(parameter=role):
                with self.assertRaisesRegex(RuntimeError, "BLOCKED_EROSION_READBACK"):
                    self.configure(Node(overrides={role: value}))

    def test_recipe_expressions_are_bound_before_readback(self):
        node = Node()
        self.configure(node)
        bindings = [i for i, event in enumerate(node.events) if event[0] == "bind"]
        reads = [i for i, event in enumerate(node.events) if event[0] == "eval"]
        self.assertEqual(len(bindings), 4)
        self.assertEqual(len(reads), 5)
        self.assertLess(max(bindings), min(reads))


if __name__ == "__main__":
    unittest.main()
