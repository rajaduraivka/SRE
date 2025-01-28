data "terraform_remote_state" "vpc-dev" {
  backend = "s3"
  config = {
    bucket = "bijak-dev-stage-state-file-2024"
    key    = "vpc/terraform.tfstate"
    region = "ap-south-1"
    profile = "flutter-acc"
  }
  
}

resource "aws_instance" "just_redis" {
  ami = var.ami-id-redis-just
  instance_type = var.redis-just-instance-type
  subnet_id = data.terraform_remote_state.vpc-dev.outputs.private_subnet_ids[0]
  private_ip = var.just_redis_ip
  vpc_security_group_ids = [aws_security_group.just-redis-dev.id]
  key_name = var.key-name-redis-just
  iam_instance_profile = var.instance_profile_ssm
  tags = {
    Name = "Bijak-${var.env}-redis-just"
    env = "${var.env}"
  }

  }

resource "aws_instance" "bastion_flt" {
  ami = var.ami-id-bastion
  instance_type = var.redis-just-instance-type
  subnet_id = data.terraform_remote_state.vpc-dev.outputs.public_subnet_ids[0]
  vpc_security_group_ids = [aws_security_group.bastion-sg.id, aws_security_group.bitbucket_ips.id]
  key_name = var.key-name-redis-just
  iam_instance_profile = var.instance_profile_ssm
  tags = {
    Name = "Bijak-${var.env}-bastion"
    env = "${var.env}"
  }

}

data "terraform_remote_state" "eip-dev" {
  backend = "s3"
  config = {
    bucket = "bijak-dev-stage-state-file-2024"
    key    = "EIP/terraform.tfstate"
    region = "ap-south-1"
    profile = "flutter-acc"
  }
  
}

resource "aws_eip_association" "eip_assoc" {
  instance_id   = aws_instance.bastion_flt.id
  allocation_id = data.terraform_remote_state.eip-dev.outputs.allocation_id
}

/*resource "aws_instance" "just-b2c-new-dev" {
  ami = var.ami-just-b2c-new-dev
  instance_type = var.redis-just-instance-type
  subnet_id = data.terraform_remote_state.vpc-dev.outputs.private_subnet_ids[1]
  vpc_security_group_ids = [aws_security_group.b2b_b2c_sg.id]
  key_name = var.key-name-redis-just
  iam_instance_profile = var.instance_profile_ssm
  tags = {
    Name = "just-b2c-new-dev"
    env = "${var.env}"
  }

}

resource "aws_instance" "Just-b2b-Dev" {
  ami = var.ami-Just-b2b-Dev
  instance_type = var.redis-just-instance-type
  subnet_id = data.terraform_remote_state.vpc-dev.outputs.private_subnet_ids[1]
  vpc_security_group_ids = [aws_security_group.b2b_b2c_sg.id]
  key_name = var.key-name-redis-just
  iam_instance_profile = var.instance_profile_ssm
  tags = {
    Name = "Just-b2b-Dev"
    env = "${var.env}"
  }

}*/

resource "aws_instance" "Just-b2b-b2c-Dev" {
  for_each = { for svc in var.ec2_b2b_b2c : "ec2-${svc.app_name}-${var.env}" => svc}
  ami = each.value.ami_id
  instance_type = each.value.instance_type
  subnet_id = data.terraform_remote_state.vpc-dev.outputs.private_subnet_ids[1]
  private_ip = each.value.ip_addr
  vpc_security_group_ids = [aws_security_group.b2b_b2c_sg.id]
  key_name = var.key-name-redis-just
  iam_instance_profile = var.instance_profile_ssm
  tags = {
    Name = "Just-${each.value.app_name}-Dev"
    env = "${var.env}"
  }

}




/*locals {
  instances = [aws_instance.Just-b2b-Dev, aws_instance.just-b2c-new-dev]
}*/
