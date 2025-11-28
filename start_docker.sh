#!/bin/bash

IMAGE_NAME="ilora-repro"
CONTAINER_NAME="ilora-container"

# Build the image
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

# Check if container exists and remove it
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "Removing existing container..."
    docker rm -f $CONTAINER_NAME
fi

# Run the container in the background
# Note: --gpus all requires NVIDIA Container Toolkit
echo "Starting container..."
docker run -d \
    --name $CONTAINER_NAME \
    --gpus all \
    --shm-size=150g \
    -v $(pwd):/app \
    --restart unless-stopped \
    $IMAGE_NAME \
    tail -f /dev/null

echo "Container '$CONTAINER_NAME' started in background."
echo "You can enter the container using: docker exec -it $CONTAINER_NAME bash"
