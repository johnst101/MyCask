#!/bin/bash

# Run PostgreSQL in a Docker container
docker run --name mycask-db \
  -e POSTGRES_USER=mycask \
  -e POSTGRES_PASSWORD=mycask123 \
  -e POSTGRES_DB=mycask \
  -p 5432:5432 \
  -d postgres:15

docker ps
echo "PostgreSQL database started in Docker container 'mycask-db'."