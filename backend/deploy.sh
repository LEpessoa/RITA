#!/bin/bash
IMAGE_NAME="rita_backend"

echo "Building image"
cd .. && docker build -f ./backend/Dockerfile \
    -t ${IMAGE_NAME} --no-cache .

echo "Removing old containers."
docker rm -f ${IMAGE_NAME} || echo "no container to remove for image "${IMAGE_NAME}

echo "Running new container"
docker run -d --name ${IMAGE_NAME} \
    --network resilient_net \
    ${IMAGE_NAME}

echo "Deploy finished"