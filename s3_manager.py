# s3_manager.py
import boto3
from botocore.exceptions import ClientError
import creds
import os

class S3Manager:
    def __init__(self):
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=creds.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=creds.AWS_SECRET_ACCESS_KEY,
            region_name=creds.AWS_REGION,
        )
        self.bucket = creds.S3_BUCKET

    def list_prefix(self, prefix=""):
        """Return folders and files under a prefix"""
        folders, files = set(), []
        try:
            response = self.s3.list_objects_v2(Bucket=self.bucket, Prefix=prefix, Delimiter="/")
            if "CommonPrefixes" in response:
                folders = {p["Prefix"] for p in response["CommonPrefixes"]}
            if "Contents" in response:
                files = [obj["Key"] for obj in response["Contents"] if not obj["Key"].endswith("/")]
        except ClientError as e:
            print("Error listing prefix:", e)
        return sorted(folders), sorted(files)

    def upload_file(self, local_path, s3_path):
        """Upload one file"""
        try:
            self.s3.upload_file(local_path, self.bucket, s3_path)
            print(f"Uploaded {local_path} → s3://{self.bucket}/{s3_path}")
        except ClientError as e:
            print("Upload failed:", e)

    def download_file(self, s3_key, local_path):
        """Download a single S3 file"""
        try:
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            self.s3.download_file(self.bucket, s3_key, local_path)
            print(f"Downloaded s3://{self.bucket}/{s3_key} → {local_path}")
        except ClientError as e:
            print("Download failed:", e)

    def delete_objects(self, keys):
        """Delete multiple objects"""
        try:
            delete_keys = [{"Key": key} for key in keys]
            self.s3.delete_objects(Bucket=self.bucket, Delete={"Objects": delete_keys})
            print(f"Deleted {len(keys)} objects from {self.bucket}")
        except ClientError as e:
            print("Deletion failed:", e)

    def create_folder(self, folder_name):
        """Create an empty folder"""
        if not folder_name.endswith("/"):
            folder_name += "/"
        try:
            self.s3.put_object(Bucket=self.bucket, Key=folder_name)
            print(f"Created folder {folder_name}")
        except ClientError as e:
            print("Folder creation failed:", e)

    def get_object_url(self, key):
        """Public object URL"""
        region = creds.AWS_REGION
        return f"https://{self.bucket}.s3.{region}.amazonaws.com/{key}"
