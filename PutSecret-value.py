import os
import json
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def put_secret(secret_name, new_secret_values, region_name):
    # Create the Secrets Manager client
    client = boto3.client('secretsmanager', region_name=region_name)

    try:
        # Convert the new secret values to a JSON string
        new_secret_string = json.dumps(new_secret_values)

        # Create or update the secret
        response = client.put_secret_value(
            SecretId=secret_name,
            SecretString=new_secret_string,
            VersionStages=['AWSCURRENT']
        )

        print(f"Secret '{secret_name}' updated successfully. New version ID: {response['VersionId']}")

    except ClientError as e:
        print(f"Error updating secret: {e}")

if __name__ == "__main__":
    # Replace these variables with your actual values or set them in the .env file
    secret_name = os.getenv('SECRET_NAME', 'default_secret_name')
    region_name = os.getenv('REGION_NAME', 'us-east-1')
    new_secret_values = os.getenv('Secret_value')

    put_secret(secret_name, new_secret_values)