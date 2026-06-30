# Generic Terraform example for a firewall rule naming convention.
# This is only a template. Review source ranges, target service accounts,
# protocols, and ports before using in any environment.

locals {
  firewall_rule_name = "fw-data-${var.environment}-allow-ingress-${var.application}-api"
}

resource "google_compute_firewall" "allow_api_ingress" {
  name        = local.firewall_rule_name
  project     = var.project_id
  network     = "default"
  direction   = "INGRESS"
  priority    = 1000
  description = "Allows approved ingress traffic for the ${var.application} API."

  allow {
    protocol = "tcp"
    ports    = ["443"]
  }

  # Replace with approved private source ranges for your organization.
  source_ranges = ["10.0.0.0/24"]

  target_tags = [
    "ingress",
    var.environment,
    "data",
    var.application
  ]
}
