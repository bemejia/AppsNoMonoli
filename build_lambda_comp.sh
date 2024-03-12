export DOCKER_DEFAULT_PLATFORM=linux/amd64
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 344488016360.dkr.ecr.us-east-1.amazonaws.com
docker build -t microlegalcomp -f Dockerfile.lambda_comp .
docker tag microlegalcomp:latest 344488016360.dkr.ecr.us-east-1.amazonaws.com/microlegalcomp:latest
docker push 344488016360.dkr.ecr.us-east-1.amazonaws.com/microlegalcomp:latest