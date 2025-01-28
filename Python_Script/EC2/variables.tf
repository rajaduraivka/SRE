variable "ami-id-redis-just" {}
variable "redis-just-instance-type" {}
variable "just_redis_ip" {}
variable "vpc_cidr" {}
variable "key-name-redis-just" {}
variable "env" {}
variable "ami-id-bastion" {}
variable "vpn_ip_1" {}
variable "vpn_ip_2" {}
variable "bastion_instance_type" {}
variable "instance_profile_ssm" {}
variable "ami-just-b2c-new-dev" {}
variable "ami-Just-b2b-Dev" {}
variable "certificate_arn_justapi_in" {}

variable "ec2_b2b_b2c" {
  description = "List of services running on EC2"
  type = list(object({
    app_name    = string
    port = number
    health_check_path = string
    host_header  = string
    listener_priority = number
    instance_type = string
    ami_id = string
    ip_addr = string
  }))
  default = [ {
    app_name    = "b2b"
    ami_id = "ami-0e6abe4cea31dad34"
    port = 80
    health_check_path = "/"
    host_header  = "dev-flt.justapi.in"
    listener_priority = 1
    instance_type = "t3.micro"
    ip_addr = "10.16.76.73"
    
  },
  {
    app_name = "b2c"
    ami_id = "ami-01aba81a36f77dc9c"
    port = 80
    health_check_path = "/"
    host_header  = "devb2c-flt.justapi.in"
    listener_priority = 2
    instance_type = "t2.small"
    ip_addr = "10.16.88.43"
  }
   ]
}

variable "bitbucket_ips" {
  type = list(string)
  
}
