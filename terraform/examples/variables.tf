variable "project_id" {
  description = "Google Cloud project ID"
  type        = string
}

variable "region" {
  description = "Cloud region"
  type        = string
  default     = "region1"
}

variable "environment" {
  description = "Environment code"
  type        = string
  default     = "dev"
}

variable "application" {
  description = "Application or platform name"
  type        = string
  default     = "analytics"
}
