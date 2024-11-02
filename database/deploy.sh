#!/bin/bash
IMAGE_NAME="rita_db"
NETWORK_NAME="rita_network"
MYSQL_ROOT_PASSWORD="rita_rocks"
HOST_PORT="3337"

network_exists=$(docker network ls | grep ${NETWORK_NAME})
if [ -z "$network_exists" ]; then
docker network create ${NETWORK_NAME}
echo "Docker network '${NETWORK_NAME}' created."
else echo "Docker network '${NETWORK_NAME}' already exists."
fi

echo "Building image"
docker build -f ./database/Dockerfile -t ${IMAGE_NAME} --no-cache ./

echo "Removing old containers."
docker rm -f ${IMAGE_NAME} || echo "no container to remove for image "${IMAGE_NAME}

echo "Running new container"
docker run -d --name ${IMAGE_NAME} \
    --network ${NETWORK_NAME} \
    -e MYSQL_ROOT_PASSWORD="${MYSQL_ROOT_PASSWORD}" \
    -p ${HOST_PORT}:3306 \
    ${IMAGE_NAME}

echo "Waiting for container startup to restore database."
while true; do
    if docker logs "${IMAGE_NAME}" 2>&1 | grep -q "Ready for start up.";
        then echo "Container is ready for database restoration."
        break
    fi # Sleep for a short interval before checking again sleep 5 
    sleep 5
done

echo "Restoring database"
mysql -uroot \
-p${MYSQL_ROOT_PASSWORD} -P${HOST_PORT} -h127.0.0.1 --init-command="SET SESSION FOREIGN_KEY_CHECKS=0;" < ./database/Database.sql

echo "Deploy finished"
