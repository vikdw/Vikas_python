terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = var.region
}

resource "aws_instance" "my_test_ec2" {
#   count= 2
#   for_each = {"a" = "test1", "b"="test2"}
  ami           = "ami-0e35ddab05955cf57"
  instance_type = var.flavor

  tags = {
    name= "test1"
    # count = "count-${count.index}"
    # "${each.key}" = "${each.value}"
  }
}
