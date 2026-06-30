#!/usr/bin/env bash
set -euo pipefail
python src/naming_validator.py --standard naming-standard.yaml --resources examples/resources.json
