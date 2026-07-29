from etl.common.config import Config
from etl.common.constants import CONFIG_PATH
from etl.storage.client import MinIOClient


class StorageManager:
    """
    High-level abstraction for MinIO storage operations.
    """

    def __init__(self):
        config = Config(CONFIG_PATH)

        self.bucket = config.get("bucket", "name")
        self.client = MinIOClient.get_client()

        self._validate_bucket()

    def _validate_bucket(self):
        if not self.client.bucket_exists(self.bucket):
            raise RuntimeError(
                f"Bucket '{self.bucket}' does not exist."
            )

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

    def list_objects(self, prefix=None):
        return self.client.list_objects(
            self.bucket,
            prefix=prefix,
            recursive=True
        )

    def exists(self):
        return self.client.bucket_exists(self.bucket)

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

        return next(objects, None) is not None