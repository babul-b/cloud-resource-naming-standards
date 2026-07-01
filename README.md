# Cloud Resource Naming Standards

This repository contains a generic, anonymized cloud resource naming standard that can be used as a starting point for public learning, internal governance, or infrastructure-as-code review.

> Medium article: [https://medium.com/@babul_b/a-practical-guide-to-cloud-resource-naming-conventions](https://medium.com/@babul_b/a-practical-guide-to-cloud-resource-naming-conventions-c1bbe581f268)

## What is included

```text
.
├── naming-standard.yaml
├── examples/resources.json
├── src/naming_validator.py
├── scripts/validate.sh
├── terraform/examples/
│   ├── variables.tf
│   ├── storage_bucket.tf
│   ├── service_account.tf
│   └── firewall_rule.tf
├── .github/workflows/validate-naming.yml
└── docs/medium-story.md
```

## Purpose

The goal of this repo is to show a practical naming standard for common cloud resources:

- Virtual machines
- Firewall rules
- Storage buckets
- Service accounts
- Custom IAM roles
- Alert policies
- Data processing clusters
- Autoscaling policies

All examples are generic and use placeholders. Do not commit real company names, customer names, project IDs, IP ranges, secrets, service-account keys, or confidential architecture details.

## Naming pattern examples

| Resource | Pattern | Example |
|---|---|---|
| Virtual machine | `vm-<os>-<env>-<region>-<project>-<purpose>` | `vm-ubnt-dev-region1-analytics-edge` |
| Firewall rule | `fw-<team>-<env>-<action>-<direction>-<project>-<purpose>` | `fw-data-dev-allow-ingress-analytics-api` |
| Storage bucket | `bkt-<env>-<region>-<project>-<component>-<purpose>` | `bkt-prod-region1-reporting-curated-data` |
| Service account | `sa-<team>-<env>-<region>-<project>-<purpose>` | `sa-data-dev-region1-analytics-pipeline` |
| Custom IAM role | `cr_<team>_<env>_<region>_<project>_<purpose>` | `cr_data_dev_region1_analytics_pipeline_runner` |
| Alert policy | `alert-policy-<env>-<region>-<application>-<component>-<condition>` | `alert-policy-prod-region1-data-pipeline-failure` |
| Data processing cluster | `cluster-<env>-<project>-<nodes>-<workload-type>-<scaling-mode>-<number>` | `cluster-prod-analytics-5-batch-autoscale-1` |

## Run validation locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run validation:

```bash
python src/naming_validator.py --standard naming-standard.yaml --resources examples/resources.json
```

Or:

```bash
./scripts/validate.sh
```

Expected output:

```text
PASS [1] virtual_machine: vm-ubnt-dev-region1-analytics-edge
PASS [2] storage_bucket: bkt-prod-region1-reporting-curated-data
PASS [3] service_account: sa-data-dev-region1-analytics-pipeline
PASS [4] firewall_rule: fw-data-dev-allow-ingress-analytics-api
```

## License

This sample is provided for learning and reference. Add your preferred license before publishing publicly.
