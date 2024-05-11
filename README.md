# ETL Pipeline for Restaurant Data 🍽️

This project implements an Extract-Transform-Load (ETL) pipeline to process restaurant data from a MongoDB database, perform transformations using pandas, and load the processed data into an AWS S3 bucket. 

## Files and Directory Structure 📂

- **Extract.py**: Python script to extract data from MongoDB.
- **Transform.py**: Python script to transform extracted data using pandas.
- **Load.py**: Python script to load transformed data into AWS S3.
- **Main.py**: Entry point script that orchestrates the ETL process.
- **ETL** directory: Contains scripts for extraction, transformation, and loading.
- **provider.tf**: Terraform configuration file to define AWS S3 bucket.
- **S3.tf**: Terraform configuration file to configure AWS provider and S3 bucket.

## Instructions 📝

1. **Setup MongoDB**: Ensure MongoDB is running locally with the necessary database and collection.

2. **Configure AWS Credentials**: Set up AWS credentials with appropriate permissions to access S3.

3. **Install Dependencies**: Install the required Python libraries using `pip install -r requirements.txt`.

4. **Execute ETL Process**: Run `Main.py` to execute the ETL pipeline. This will extract data from MongoDB, transform it, and load it into the specified S3 bucket.

5. **Check S3 Bucket**: Verify that the transformed data files (`restaurant_info.csv` and `address.csv`) are uploaded to the S3 bucket specified in the `Load.py` script.

6. **Terraform Deployment**: Deploy the S3 bucket using Terraform by running `terraform init` and `terraform apply`. Ensure Terraform is properly configured with AWS credentials.

## Additional Information ℹ️

- **MongoDB Configuration**: The extraction script assumes MongoDB is running locally on `localhost` with default port `27017`. Modify the connection parameters in `Extract.py` if necessary.

- **AWS S3 Bucket**: The AWS S3 bucket is configured using Terraform. Make sure Terraform is properly configured with AWS credentials and the desired AWS region.

- **Dependencies**: This project relies on `pymongo` and `pandas` for data extraction and transformation, and `boto3` for AWS S3 integration.


