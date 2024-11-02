#!/bin/bash
IMAGE_NAME="rita_backend"
NETWORK_NAME="rita_network"

network_exists=$(docker network ls | grep ${NETWORK_NAME})
if [ -z "$network_exists" ]; then
docker network create ${NETWORK_NAME}
echo "Docker network '${NETWORK_NAME}' created."
else echo "Docker network '${NETWORK_NAME}' already exists."
fi

echo "Building image"
docker build -f ./backend/Dockerfile -t ${IMAGE_NAME} --no-cache ./

echo "Removing old containers."
docker rm -f ${IMAGE_NAME} || echo "no container to remove for image "${IMAGE_NAME}

echo "Running new container"
docker run -d --name ${IMAGE_NAME} \
    --network ${NETWORK_NAME} \
    -e db_host="rita_db" \
    -e db_port=3306 \
    -e uplink_key="somerandomeuplinkkey" \
    -e uplink_address="rita_client" \
    -e db_user='rita' \
    -e db_password='rita_rocks' \
    ${IMAGE_NAME}

echo "Deploy finished"