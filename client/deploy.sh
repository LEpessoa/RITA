#!/bin/bash
IMAGE_NAME="rita_client"
NETWORK_NAME="rita_network"

network_exists=$(docker network ls | grep ${NETWORK_NAME})
if [ -z "$network_exists" ]; then
docker network create ${NETWORK_NAME}
echo "Docker network '${NETWORK_NAME}' created."
else echo "Docker network '${NETWORK_NAME}' already exists."
fi

echo "Building image"
docker build -f ./client/Dockerfile \
    -t ${IMAGE_NAME} .

echo "Removing old containers."
docker rm -f ${IMAGE_NAME} || echo "no container to remove for image "${IMAGE_NAME}

echo "Running new container"
docker run -d --name ${IMAGE_NAME} \
    --network ${NETWORK_NAME} \
    -p 3030:3030 \
    ${IMAGE_NAME}

echo "Deploy finished"