from pathlib import Path

from etl.storage.client import MinIOClient


class StorageManager:

    def __init__(self, bucket):

        self.bucket = bucket

        self.client = MinIOClient.get_client()

    def upload(self, file_path, object_name):

        self.client.fput_object(
            self.bucket,
            object_name,
            str(file_path)
        )

    def download(self, object_name, destination):

        self.client.fget_object(
            self.bucket,
            object_name,
            destination
        )

    def list_objects(self):

        return self.client.list_objects(
            self.bucket,
            recursive=True
        )

    def exists(self):

        return self.client.bucket_exists(
            self.bucket
        )

    def delete(self, object_name):

        self.client.remove_object(
            self.bucket,
            object_name
        )

    def object_exists(self, object_name):

        objects = self.client.list_objects(
            self.bucket,
            prefix=object_name
        )

        return any(True for _ in objects)