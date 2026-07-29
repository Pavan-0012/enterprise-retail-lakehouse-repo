from minio import Minio

from etl.common.config import Config
from etl.common.constants import CONFIG_PATH


class MinIOClient:
    """
    Singleton MinIO client.
    """

    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            config = Config(CONFIG_PATH)

            cls._client = Minio(
                endpoint=config.get("minio", "endpoint"),
                access_key=config.get("minio", "access_key"),
                secret_key=config.get("minio", "secret_key"),
                secure=config.get("minio", "secure"),
            )

        return cls._client