provider "aws" {
    project     = var.project
    region      = var.aws_region
    alias       = var.aws_alias
    profile     = var.aws_profile
    access_key  = var.aws_access_key
    secret_key  = var.aws_secret_key
}
