# Cloudinary to S3 Migration

This project migrates all your media files from Cloudinary to an S3 bucket (Amazon S3, or a S3-compatible service such as MinIO).

## Requirements

- Python 3.
- (Optional) Docker and Docker Compose

## Usage

### Basic Usage without Docker

1. **Clone the Repository**

   ```bash
   git clone https://github.com/username/cloudinary-to-s3-migration.git
   cd cloudinary-to-s3-migration
   ```

2. **Configure Environment Variables**

   Copy `.env.example` to a new file named `.env` and fill in the necessary environment variables.

   ```bash
   cp .env.example .env
   nano .env
   ```

3. **Install Python Requirements**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Migration Script**

   ```bash
   python migrate.py
   ```

### Optional Usage with Docker and MinIO

The included Docker Compose file includes a local MinIO server that will automatically create a bucket, and establish communication with the migration container.
This allow you to easily download all the resources to a local bucket which you can then use for programmatic access or via rclone etc.

1. **Run Docker Compose**

   If you want to use MinIO, use Docker Compose to start the MinIO and migration services.

   ```bash
   docker-compose up --build
   ```

   This will also automatically run the migration script after setting up MinIO and the bucket.

## Project Structure

- `migrate.py`: The main migration script.
- `docker-compose.yml` (optional): Docker Compose configuration for MinIO setup.
- `bucket-setup.sh` (optional): A shell script to set up the S3 bucket in MinIO.
- `requirements.txt`: List of Python dependencies.

## Configuration

- Use the `.env` file to configure the migration and (optional) MinIO setup.
- Ensure all environment variables in the `.env` file are correctly set for your setup.

### ENV Configuration

Below are the descriptions of the environment variables used in the `.env` file:

1. **`CLOUDINARY_URL`** (Required)
   - Your Cloudinary URL which includes API key, API secret, and cloud name.
   - Format: `"cloudinary://<api_key>:<api_secret>@<cloud_name>"`

2. **`AWS_ACCESS_KEY_ID`** (Required for AWS S3 / Optional for MinIO)
   - Your AWS access key ID.
   - Default for MinIO: `"minioadmin"`

3. **`AWS_SECRET_ACCESS_KEY`** (Required for AWS S3 / Optional for MinIO)
   - Your AWS secret access key.
   - Default for MinIO: `"minioadmin"`

4. **`S3_BUCKET_NAME`** (Required)
   - The name of your S3 bucket where files will be migrated.
   - Example: `"your-s3-bucket-name"`

5. **`S3_ENDPOINT_URL`** (Optional)
   - The endpoint URL of your S3 service.
   - If using a local MinIO server, use the local server address here.
   - Example: `"http://localhost:9000"`

6. **`MINIO_ROOT_USER`** (Optional)
   - The root user for MinIO, used when setting up a MinIO server.
   - Default: `"minioadmin"`

7. **`MINIO_ROOT_PASSWORD`** (Optional)
   - The root password for MinIO, used when setting up a MinIO server.
   - Default: `"minioadmin"`

8. **`LOG_LEVEL`** (Optional)
   - The log level for the migration script.
   - Options: `"INFO"` (default), `"DEBUG"`
   - Example: `"INFO"`

### Example .env File

Below is an example configuration for the `.env` file:

```plaintext
CLOUDINARY_URL="cloudinary://123456789012345:abcdefghijklmno@cloudname"
AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
S3_BUCKET_NAME="migrated-cloudinary"
S3_ENDPOINT_URL="http://localhost:9000"
MINIO_ROOT_USER="minioadmin"
MINIO_ROOT_PASSWORD="minioadmin"
LOG_LEVEL="INFO"
```

Be sure to replace the placeholder values with your actual credentials and configuration details.


## Troubleshooting

- Check the logs for any errors.
- For Docker setup, use `docker-compose logs` to view logs.

## Conclusion

This tool simplifies the process of migrating your media files from Cloudinary to an S3 bucket, with optional MinIO support for local development or testing.
