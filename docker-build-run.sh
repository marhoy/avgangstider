#!/bin/bash

IMAGE_NAME=marhoy/avgangstider
VERSION=$(uvx --from=toml-cli toml get --toml-path=pyproject.toml project.version)
LOCAL_PORT=8080

echo "Building version $VERSION for $PLATFORM"
docker buildx build --platform linux/amd64,linux/arm64 --tag $IMAGE_NAME:$VERSION --tag $IMAGE_NAME:latest .

echo -e "\n\nRunning container on http://localhost:$LOCAL_PORT\n\n"
docker run --rm --publish $LOCAL_PORT:5000 $IMAGE_NAME:$VERSION
