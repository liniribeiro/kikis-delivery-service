import boto3
import requests
from botocore.config import Config

from src.settings import BUCKET_NAME


class S3Service:

    bucket = BUCKET_NAME

    def __init__(self):
        self.s3_client = boto3.client('s3', config=Config(signature_version='s3v4'))

    def get_presigned_link(self, key):
        url = self.s3_client.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': self.bucket,
                'Key': key
            },
            ExpiresIn=60 * 60 * 23 * 7
        )
        return url.replace(" ", "")

    def send_file_to_s3(self, file_name) -> str:
        key = f"kikis-reports/{file_name}"
        self.s3_client.upload_file(file_name, self.bucket, key)
        return self.get_presigned_link(key)

