provider "aws" {
  # shared_credentials_file = "$HOME/.aws/credentials"
  region = "us-east-2"
}

# random string for flask secret-key env variable
resource "random_string" "flask-secret-key" {
  length = 16
  special = true
  override_special = "/@\" "
}

data "aws_availability_zones" "azs" {}

# create a VPC (Virtual Private Cloud)
resource "aws_vpc" "vpc" {
  cidr_block            = "10.0.0.0/16"
  enable_dns_hostnames  = true
  enable_dns_support    = true

  tags = {
    Name = "fast-api-vpc"
  }
}

resource "aws_internet_gateway" "internet_gateway" {
  vpc_id = aws_vpc.vpc.id
  tags = {
    Name = "fast-api-igw"
  }
}

locals {
  subnets = flatten([aws_subnet.public_subnets.*.id])
}

# create a Route Table for the VPC
resource "aws_route_table" "rt_public" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.internet_gateway.id
  }

  tags = {
    Name = "fast-api-rt-public"
  }
}

resource "aws_default_route_table" "rt_private_default" {
  default_route_table_id = aws_vpc.vpc.default_route_table_id

  tags = {
    Name = "fast-api-rt-private-default"
  }
}

resource "aws_subnet" "public_subnets" {
  count                  = 2
  cidr_block             = "10.0.${2 * (1 - 1) + count.index + 1}.0/24"
  vpc_id                 = aws_vpc.vpc.id
  availability_zone      = data.aws_availability_zones.azs.names[count.index]
  map_public_ip_on_launch = true

  tags = {
    Name = "fast-api-tf-public-${count.index + 1}"
  }
}


# create <count> number of private subnets in each availability zone
resource "aws_subnet" "private_subnets" {
  count             = 2
  cidr_block        = "10.0.${2 * (1 - 1) + count.index + 1 + 2}.0/24"
  vpc_id            = aws_vpc.vpc.id
  availability_zone = data.aws_availability_zones.azs.names[count.index]

  tags = {
    Name = "fast-api-tf-private-${count.index + 1}"
  }
}

resource "aws_route_table_association" "public-rt-association" {
  count = 2
  route_table_id = aws_route_table.rt_public.id
  subnet_id = aws_subnet.public_subnets.*.id[count.index]
}

# Associate the private subnets with the public route table
resource "aws_route_table_association" "private-rt-association" {
  count = 2
  route_table_id = aws_route_table.rt_public.id
  subnet_id = aws_subnet.private_subnets.*.id[count.index]
}

resource "aws_security_group" "public-sg" {
  name = "public-group-default"
  description = "access to public instances"
  vpc_id = aws_vpc.vpc.id
}

# create security group for ALB
resource "aws_security_group" "alb_sg" {
  name = "alb-group"
  description = "control access to the application load balancer"
  vpc_id = aws_vpc.vpc.id

  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = [
      "0.0.0.0/0"]
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = [
      "0.0.0.0/0"]
  }
}

# create security group to access the ecs cluster (traffic to ecs cluster should only come from the ALB)
resource "aws_security_group" "ecs_sg" {
  name = "ecs-from-alb-group"
  description = "control access to the ecs cluster"
  vpc_id = aws_vpc.vpc.id

  ingress {
    from_port = 8003
    to_port = 8003
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    security_groups = [aws_security_group.alb_sg.id]
  }

  egress {
    protocol = "-1"
    from_port = 0
    to_port = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# create security group for RDS
resource "aws_security_group" "rds_sg" {
  name = "postgres-public-group"
  description = "access to public rds instances"
  vpc_id = aws_vpc.vpc.id

  ingress {
    protocol = "tcp"
    from_port = 5432
    to_port = 5432
    cidr_blocks = ["0.0.0.0/0"]
    security_groups = [aws_security_group.alb_sg.id]
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_alb" "alb" {
  load_balancer_type = "application"
  name = "application-load-balancer"
  subnets = aws_subnet.public_subnets.*.id
  security_groups = [aws_security_group.alb_sg.id]
}

resource "aws_alb_target_group" "target_group" {
  name = "ecs-target-group"
  port = 80
  protocol = "HTTP"
  vpc_id = aws_vpc.vpc.id
  target_type = "ip"
}

resource "aws_alb_listener" "fp-alb-listener" {
  load_balancer_arn = aws_alb.alb.arn
  port = 80
  protocol = "HTTP"
  default_action {
    target_group_arn = aws_alb_target_group.target_group.arn
    type = "forward"
  }
 }
  resource "aws_ecs_cluster" "fp-ecs-cluster" {
  name = "fast-api-app"

  tags = {
    Name = "fast-api-app"
  }
}


data "template_file" "task_definition_template" {
  template = file("task_definition.json.tpl")
  vars = {
    REPOSITORY_URL = "alejofig/bff:latest"
    BROKER_HOST = "pulsar-aws-useast1.streaming.datastax.com"
    PULSAR_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDk1ODgxOTYsImlzcyI6ImRhdGFzdGF4Iiwic3ViIjoiY2xpZW50OzRhZDgzOWUwLTFjNDEtNGE0YS1hZDlmLWZiMjBlMTQ2NTdkNTtibTl0YjI1dmJHbDBhV05oY3c9PTtmYzBiNjQ2Y2RmIiwidG9rZW5pZCI6ImZjMGI2NDZjZGYifQ.hjZL55Fi9lK6gmrkdcmgchx8gC-knnwzcH4c6iDBott8FX8vSSRJLBUq2yhEWDXi_XKp2UPPzlOqzJuBWhjiacLNtNMPrq-1VahJZAof96b4CvJthhRsSBZZN-eMtitW8OWOtx5mkoVNGZOBfSsfpoojZ6soITuSG_tP58VKOQbtarj1du-TlzANYroCQ3wlMRBR7QCphhot7fPtCWDYVkSJu5vpY-9Qh3fyxFFDqmn1WvM0x0hj-ESMoPYIwrN0Nmz3FiXzoMR6tif_95cGvk_2CsVzVWnZO2cYKKruu_j3qf3KdlqxIhdMxw_M_pPv61FgbEsCajeq5NTKpTpUww"
    LEGAL_HOST = "https://pxq5fvl4cqt7yzkynzjabgtaj40vbrdg.lambda-url.us-east-1.on.aws/"
  }
}

resource "aws_ecs_task_definition" "task_definition" {
  family = "fast-api-app"
  requires_compatibilities = [
    "FARGATE"]
  network_mode = "awsvpc"
  cpu = 256
  memory = 512
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn  # Nuevo
  container_definitions = data.template_file.task_definition_template.rendered

}

resource "aws_ecs_service" "flask-service" {
  name = "fast-api-app-service"
  cluster = aws_ecs_cluster.fp-ecs-cluster.id
  task_definition = aws_ecs_task_definition.task_definition.arn
  desired_count = 1
  launch_type = "FARGATE"

  network_configuration {
    security_groups = [
      aws_security_group.ecs_sg.id]
    subnets = aws_subnet.public_subnets.*.id
    assign_public_ip = true
  }

  load_balancer {
    container_name = "fast-api-app"
    container_port = 8003
    target_group_arn = aws_alb_target_group.target_group.id
  }

  depends_on = [
    aws_alb_listener.fp-alb-listener
  ]
}

output "alb-dns-name" {
  value = aws_alb.alb.dns_name
}

resource "aws_cloudwatch_log_group" "ecs_log_group" {
  name              = "/ecs/fast-api-app"  # Nombre del grupo de logs
  retention_in_days = 7  # Retención de los logs en días (ajusta según tus necesidades)
}


resource "aws_iam_role" "ecs_task_execution_role" {
  name               = "fast-api-ecs-task-execution-role"
  assume_role_policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "ecs-tasks.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy" "fast-api-ecs_cloudwatch_policy" {
  name        = "fast-api-ecs-cloudwatch-policy"
  description = "Policy to allow ECS to write logs to CloudWatch"

  policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        "Resource": "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_cloudwatch_attachment" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = aws_iam_policy.fast-api-ecs_cloudwatch_policy.arn
}