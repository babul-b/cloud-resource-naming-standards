# Generic Terraform example for a storage bucket naming convention.
# Replace provider/project details with your own environment settings.

locals {
  bucket_name = "bkt-${var.environment}-${var.region}-${var.application}-landing-raw-data"

  common_labels = {
    resource_name      = "storage-bucket"
    project_name       = var.project_id
    region_name        = var.region
    environment_name   = var.environment
    application_name   = var.application
    owner_name         = "data-engineering"
    purpose            = "store-raw-landing-data"
    automation_source  = "terraform"
    data_classification = "internal"
  }
}

resource "google_storage_bucket" "landing_raw_data" {
  name          = local.bucket_name
  project       = var.project_id
  location      = var.region
  storage_class = "STANDARD"

  uniform_bucket_level_access = true

  labels = local.common_labels
}
