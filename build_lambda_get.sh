export DOCKER_DEFAULT_PLATFORM=linux/amd64
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 344488016360.dkr.ecr.us-east-1.amazonaws.com
docker build -t microlegalget -f Dockerfile.lambda_get .
docker tag microlegalget:latest 344488016360.dkr.ecr.us-east-1.amazonaws.com/microlegalget:latest
docker push 344488016360.dkr.ecr.us-east-1.amazonaws.com/microlegalget:latest