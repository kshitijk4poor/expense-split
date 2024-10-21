#!/bin/bash

# Ensure Docker is running
if ! systemctl is-active --quiet docker
then
    echo "Docker is not running. Starting Docker..."
    sudo systemctl start docker
fi

# Navigate to infrastructure directory
cd infrastructure

# Build and start services
docker-compose up --build -d

echo "Deployment complete. All services are up and running."