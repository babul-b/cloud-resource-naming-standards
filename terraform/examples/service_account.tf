# Generic Terraform example for a service account naming convention.

locals {
  service_account_id = "sa-data-${var.environment}-${var.region}-${var.application}-pipeline"
}

resource "google_service_account" "pipeline_runner" {
  project      = var.project_id
  account_id   = local.service_account_id
  display_name = local.service_account_id
  description  = "Service account used by the ${var.application} pipeline in ${var.environment}."
}
