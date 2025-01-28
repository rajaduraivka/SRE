resource "aws_alb" "just-ec2-alb" {
  name            = "just-services-ec2-${var.env}-lb"
  subnets         = data.terraform_remote_state.vpc-dev.outputs.public_subnet_ids
  security_groups = [aws_security_group.b2b_b2c_sg.id]
}

resource "aws_lb_target_group" "all-ec2-tg" {
  for_each = { for svc in var.ec2_b2b_b2c : "ec2-${svc.app_name}-${var.env}" => svc}
  name        = "${each.value.app_name}-${var.env}-tg"
  port        = "${each.value.port}"
  protocol    = "HTTP"
  vpc_id = data.terraform_remote_state.vpc-dev.outputs.vpc_id
  target_type = "instance"

  health_check {
    healthy_threshold   = "5"
    interval            = "30"
    protocol            = "HTTP"
    matcher             = "200-350"
    timeout             = "5"
    path                = "${each.value.health_check_path}"
    unhealthy_threshold = "2"
  }
}

locals {
  target_group_arns = values(aws_lb_target_group.all-ec2-tg)[*].arn
  random_target_group_arn = element(local.target_group_arns, 0)
}

resource "aws_lb_target_group_attachment" "all-ec2-tg-attachment" {
  for_each = { for svc in var.ec2_b2b_b2c : "ec2-${svc.app_name}-${var.env}" => svc}
  target_group_arn = aws_lb_target_group.all-ec2-tg[each.key].arn
  target_id        = aws_instance.Just-b2b-b2c-Dev[each.key].id
  port             = 80
}

/*resource "aws_alb_listener" "default_80_listener" {
  load_balancer_arn = aws_alb.just-ec2-alb.id
  port              = 80
  protocol          = "HTTP"

  default_action {
    target_group_arn = local.random_target_group_arn
    type             = "forward"
  }
  #depends_on = [ local.default_target_group_arn ]
}

resource "aws_alb_listener_rule" "all-80-port-listener" {
  for_each = { for svc in var.ec2_b2b_b2c : "ec2-${svc.app_name}-${var.env}" => svc}
  listener_arn = aws_alb_listener.default_80_listener.arn
  priority     = each.value.listener_priority

  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.all-ec2-tg[each.key].arn
  }

  condition {
    host_header {
      values = ["${each.value.host_header}"]
    }
  }
}*/

resource "aws_alb_listener" "default_80_listener" {
  load_balancer_arn = aws_alb.just-ec2-alb.id
  port              = 80
  protocol          = "HTTP"

  default_action {
    type = "redirect"

    redirect {
      port        = "443"
      protocol    = "HTTPS"
      status_code = "HTTP_301"
    }
  }
}


resource "aws_alb_listener" "default_443_listener" {
  load_balancer_arn = aws_alb.just-ec2-alb.id
  port              = 443
  protocol          = "HTTPS"
  ssl_policy        = "ELBSecurityPolicy-2016-08"
  certificate_arn   = "${var.certificate_arn_justapi_in}"

  default_action {
    target_group_arn = local.random_target_group_arn
    type             = "forward"
  }
}

resource "aws_alb_listener_rule" "all-443-port-listener" {
  for_each = { for svc in var.ec2_b2b_b2c : "ec2-${svc.app_name}-${var.env}" => svc}
  listener_arn = aws_alb_listener.default_443_listener.arn
  priority     = each.value.listener_priority

  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.all-ec2-tg[each.key].arn
  }

  condition {
    host_header {
      values = ["${each.value.host_header}"]
    }
  }
}