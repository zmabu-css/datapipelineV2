# ETL Data Pipeline V2

The objective of this project is to design and implement a scalable ETL (Extract, Transform, Load) pipeline using Python and AWS services. The pipeline automates the process of extracting data from multiple sources, transforming it for analysis, and loading it into a centralized data warehouse for business insights.

### Technologies Used
- Programming Languages: Python
- Databases: PostgreSQL, Amazon Redshift
- Tools: AWS (Amazon Redshift), Pandas
- Libraries: SQLAlchemy, Boto3

## Setup Guide

### Prerequisites

**Account Setup**
- Azure Account: Create an Azure account if you don't have one. You can sign up at Azure.
- AWS Account: Create an AWS account if you don't have one. You can sign up at AWS.
- Development Environment: Ensure you have Python and necessary libraries installed.

**Install Required Tools:**
- Azure CLI: Install from Azure CLI Installation Guide.
- AWS CLI: Install from AWS CLI Installation Guide.
- PostgreSQL: Install from PostgreSQL Installation Guide.
- SQLAlchemy: `` pip install SQLAlchemy. ``
- Pandas: `` pip install pandas. ``
- psycopg2: `` pip install psycopg2-binary. ``
- Boto3: `` pip install boto3. ``

### Configuration Files
**aws_config.json: Store your AWS credentials and Redshift details.**

```
{
    "aws_access_key_id": "YOUR_AWS_ACCESS_KEY_ID",
    "aws_secret_access_key": "YOUR_AWS_SECRET_ACCESS_KEY",
    "region": "YOUR_AWS_REGION",
    "redshift": {
        "dbname": "your_db_name",
        "user": "your_username",
        "password": "your_password",
        "host": "your_redshift_cluster_host",
        "port": 5439
    }
}
```
**azure_config.json: Store your Azure credentials and storage details.**
```
{
    "azure_storage_account_name": "your_storage_account_name",
    "azure_storage_account_key": "your_storage_account_key",
    "blob_container_name": "your_blob_container_name"
}
```
### Run the program in Terminal

`` python main.py ``

