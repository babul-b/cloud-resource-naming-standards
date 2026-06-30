#!/usr/bin/env python3
"""Validate cloud resource names and labels against a generic naming standard.

Usage:
  python src/naming_validator.py --standard naming-standard.yaml --resources examples/resources.json

The script returns exit code 0 when all resources pass validation.
It returns exit code 1 when one or more resources fail validation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml


def load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def load_json(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("Resources file must contain a JSON list of resource objects.")
    return data


def validate_resource(resource: Dict[str, Any], standard: Dict[str, Any]) -> Tuple[bool, List[str]]:
    errors: List[str] = []

    resource_type = resource.get("type")
    name = resource.get("name")
    labels = resource.get("labels", {})

    if not resource_type:
        errors.append("Missing resource type.")
        return False, errors

    if not name:
        errors.append("Missing resource name.")
        return False, errors

    patterns = standard.get("patterns", {})
    if resource_type not in patterns:
        errors.append(f"Unknown resource type: {resource_type}")
        return False, errors

    regex = patterns[resource_type].get("pattern")
    if not regex:
        errors.append(f"No pattern found for resource type: {resource_type}")
    elif not re.match(regex, name):
        example = patterns[resource_type].get("example", "")
        errors.append(
            f"Name '{name}' does not match expected pattern for {resource_type}. "
            f"Example: {example}"
        )

    if not isinstance(labels, dict):
        errors.append("Labels must be a JSON object.")
        return False, errors

    required_labels = standard.get("required_labels", [])
    for label in required_labels:
        if label not in labels or labels[label] in (None, ""):
            errors.append(f"Missing required label: {label}")

    allowed_envs = set(standard.get("allowed_environments", []))
    env = labels.get("environment_name")
    if env and allowed_envs and env not in allowed_envs:
        errors.append(
            f"Invalid environment_name '{env}'. Allowed values: {sorted(allowed_envs)}"
        )

    allowed_regions = set(standard.get("allowed_regions", []))
    region = labels.get("region_name")
    if region and allowed_regions and region not in allowed_regions:
        errors.append(
            f"Invalid region_name '{region}'. Allowed values: {sorted(allowed_regions)}"
        )

    return len(errors) == 0, errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate cloud resource naming standards.")
    parser.add_argument("--standard", required=True, help="Path to naming-standard.yaml")
    parser.add_argument("--resources", required=True, help="Path to resources.json")
    args = parser.parse_args()

    standard = load_yaml(Path(args.standard))
    resources = load_json(Path(args.resources))

    failed = False
    for index, resource in enumerate(resources, start=1):
        is_valid, errors = validate_resource(resource, standard)
        resource_type = resource.get("type", "unknown")
        name = resource.get("name", "unknown")

        if is_valid:
            print(f"PASS [{index}] {resource_type}: {name}")
        else:
            failed = True
            print(f"FAIL [{index}] {resource_type}: {name}")
            for error in errors:
                print(f"  - {error}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
