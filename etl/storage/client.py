from minio import Minio

from etl.common.config import Config
from etl.common.constants import CONFIG_PATH


config = Config(CONFIG_PATH)


class MinIOClient:

    def __init__(self):

        self.client = Minio(
            endpoint=config.get("minio", "endpoint"),
            access_key=config.get("minio", "access_key"),
            secret_key=config.get("minio", "secret_key"),
            secure=config.get("minio", "secure"),
        )

    def get_client(self):
        return self.client