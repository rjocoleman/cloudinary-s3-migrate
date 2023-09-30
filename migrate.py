import os
import cloudinary
import cloudinary.api
from boto3 import client
import requests
import logging

# Set up logging
log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# Cloudinary Configuration
config = cloudinary.config(secure=True)

# S3 Client Configuration
s3 = client(
    's3',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    endpoint_url=os.environ.get('S3_ENDPOINT_URL', None)
)

def fetch_cloudinary_resources(next_cursor=None):
    """Fetch Cloudinary resources using pagination."""
    logging.debug("Fetching Cloudinary resources.")
    return cloudinary.api.resources(max_results=500, next_cursor=next_cursor)

def upload_file_to_s3(file_content, filename):
    """Upload a file to the S3 bucket."""
    logging.debug(f"Uploading {filename} to S3.")
    s3.put_object(Bucket=os.environ['S3_BUCKET_NAME'], Key=filename, Body=file_content)


def main():
    """Main function to fetch files from Cloudinary and upload them to S3."""
    next_cursor = None
    while True:
        response = fetch_cloudinary_resources(next_cursor)

        for resource in response['resources']:
            file_url = resource['url']
            cloudinary_response = requests.get(file_url)
            # Use the public_id and format fields to create the filename with the correct extension
            filename = f"{resource['public_id']}.{resource['format']}"
            upload_file_to_s3(cloudinary_response.content, filename)
            logging.info(f'Uploaded {filename} to S3')

        next_cursor = response.get('next_cursor')
        if not next_cursor:
            break

if __name__ == "__main__":
    main()
