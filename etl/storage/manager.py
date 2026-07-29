from pathlib import Path

from etl.storage.client import MinIOClient
from etl.common.config import Config
from etl.common.constants import CONFIG_PATH


config = Config(CONFIG_PATH)


class StorageManager:

    def __init__(self):

        self.client = MinIOClient().get_client()
        self.bucket = config.get("bucket", "name")

    def upload_file(self, local_file, object_name):

        self.client.fput_object(
            self.bucket,
            object_name,
            local_file
        )

    def list_objects(self):

        return self.client.list_objects(
            self.bucket,
            recursive=True
        )

    def bucket_exists(self):

        return self.client.bucket_exists(self.bucket)