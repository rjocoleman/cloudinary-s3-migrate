#!/bin/sh

# Check if environment variables are set
if [ -z "$MINIO_ENDPOINT_URL" ] || [ -z "$MINIO_ROOT_USER" ] || [ -z "$MINIO_ROOT_PASSWORD" ] || [ -z "$S3_BUCKET_NAME" ]; then
  echo "Error: Required environment variables MINIO_ENDPOINT_URL, MINIO_ROOT_USER, MINIO_ROOT_PASSWORD, and S3_BUCKET_NAME must be set."
  exit 1
fi

# Set MinIO client alias to point to the MinIO server
mc alias set myminio $MINIO_ENDPOINT_URL $MINIO_ROOT_USER $MINIO_ROOT_PASSWORD

# Check if the bucket exists
BUCKET_FOUND=$(mc ls myminio 2>&1 | grep -c "$S3_BUCKET_NAME")

# If the bucket does not exist, create it
if [ "$BUCKET_FOUND" -eq 0 ]; then
  mc mb myminio/$S3_BUCKET_NAME || { echo "Error creating bucket"; exit 1; }
fi
