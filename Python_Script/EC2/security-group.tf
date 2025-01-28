#Security Group for Redis Instance
resource "aws_security_group" "just-redis-dev" {
    name = "just_redis_dev_sg"
    description = "Allow database traffic"
    vpc_id = data.terraform_remote_state.vpc-dev.outputs.vpc_id
    #vpc_id = module.vpc.vpc_id

    ingress {
    from_port   = 6367
    to_port     = 6367
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]  # Adjust as necessary
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]  # Adjust as necessary
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "just_redis_dev_sg"
  }
}

#Bastion Security Group
resource "aws_security_group" "bastion-sg" {
    name = "bastion_sg"
    description = "Bastion SG"
    vpc_id = data.terraform_remote_state.vpc-dev.outputs.vpc_id

    ingress {
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = [var.vpn_ip_1, var.vpn_ip_2]  # Adjust as necessary
    }

    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }

    tags = {
    Name = "just_bastion_dev_sg"
  }
}

#Dev B2B_B2C SG
resource "aws_security_group" "b2b_b2c_sg" {
    name = "b2b_b2c_${var.env}_sg"
    description = "b2b_b2c_${var.env}_sg"
    vpc_id = data.terraform_remote_state.vpc-dev.outputs.vpc_id

    ingress {
        from_port   = 80
        to_port     = 80
        protocol    = "tcp"
        #cidr_blocks = ["3.109.127.79/32", "65.1.61.129/32"]  # Adjust as necessary
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        from_port   = 443
        to_port     = 443
        protocol    = "tcp"
        #cidr_blocks = ["3.109.127.79/32", "65.1.61.129/32"]  # Adjust as necessary
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = [var.vpc_cidr]  # Adjust as necessary
    }

    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }

    tags = {
    Name = "b2b_b2c_${var.env}_sg"
  }
}

#Bitbucket IPS
resource "aws_security_group" "bitbucket_ips" {
  name = "bitbucket_ip_sg"
  description = "Allow Bitbucket for deployment"
  vpc_id = data.terraform_remote_state.vpc-dev.outputs.vpc_id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.bitbucket_ips
  }

  egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }

  tags = {
    Name = "bitbucket_ip_sg"
  }


}