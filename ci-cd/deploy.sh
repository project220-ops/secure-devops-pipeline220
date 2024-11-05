#!/bin/bash
echo "Deploying the Docker container..."
docker run -d --name neural-net-container neural-net-image
