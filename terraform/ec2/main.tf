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
output "instance_public_ip" {
  value = aws_instance.my_test_ec2.public_ip
#  value = [for i in aws_instance.my_test_ec2 : i.public_ip]
}
output "instance_id" {
 value       = aws_instance.public_instance.id
 description = "Instance ID"
}
