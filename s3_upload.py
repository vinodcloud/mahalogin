#!/usr/bin/python3
import boto3
s3_client = boto3.client('s3')
response = s3_client.upload_file('/var/lib/jenkins/file1', 'cf-templates-z36e7fpqfst3-us-east-2', 'file1-2-9')
print(response)
