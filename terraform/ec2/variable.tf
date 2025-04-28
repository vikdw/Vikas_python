variable "flavor" {
  description = "Type of EC2 instance"
  type        = string
  default     = "t2.micro"
}

variable "region" {
  description = "region"
  type        = string
  default     = "ap-south-1"
}