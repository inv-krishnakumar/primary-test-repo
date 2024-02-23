import os
import boto3
from botocore.exceptions import ClientError


def put_secret(secret_name, new_secret_values, region_name):
    # Create the Secrets Manager client
    client = boto3.client('secretsmanager', region_name=region_name)

    try:

        # Create or update the secret
        response = client.put_secret_value(
            SecretId=secret_name,
            SecretString=new_secret_values,
            VersionStages=['AWSCURRENT']
        )

        print(f"Secret '{secret_name}' updated successfully. New version ID: {response['VersionId']}")

    except ClientError as e:
        print(f"Error updating secret: {e}")

if __name__ == "__main__":
    print (__name__)
    secret_name = os.getenv('SECRET_NAME')
    region_name = os.getenv('REGION_NAME')
    secret_key={
        "scrt-qi-back-dev-data_exchange":os.getenv('QI_DEV_DATA_EXCHANGE_SECRET_VALUE'),
        "scrt-qi-back-dev-monitor":os.getenv('QI_DEV_MONITOR_SECRET_VALUE'),
        "scrt-qi-back-dev-research":os.getenv('QI_DEV_RESEARCH_SECRET_VALUE'),
        "scrt-qi-back-dev-screening":os.getenv('QI_DEV_SCREENING_SECRET_VALUE'),
        "scrt-qi-back-dev-batch":os.getenv('QI_DEV_BATCH_SECRET_VALUE'),
        "scrt-qi-back-dev-video":os.getenv('QI_DEV_VIDEO_SECRET_VALUE'),
        "scrt-qi-back-dev-customer":os.getenv('QI_DEV_CUSTOMER_SECRET_VALUE'),
        "scrt-qi-back-dev-communication":os.getenv('QI_DEV_COMMUNICATION_SECRET_VALUE'),
        "scrt-qi-bff-dev-textchat":os.getenv('QI_DEV_TEXT_CHAT_SECRET_VALUE'),
        "scrt-qi-bff-dev-customer":os.getenv('QI_DEV_BFF_CUSTOMER_SECRET_VALUE'),
    }

    new_secret_values=secret_key.get(secret_name)


    put_secret(secret_name, new_secret_values, region_name)