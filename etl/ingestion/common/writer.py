from pyspark.sql import DataFrame

from etl.common.config import Config
from etl.common.constants import CONFIG_PATH


config = Config(CONFIG_PATH)


class RawWriter:

    def __init__(self):

        self.minio = config.section("minio")

    def write(
        self,
        df: DataFrame,
        layer: str,
        source: str,
        table: str,
        mode: str = "overwrite"
    ):

        bucket = self.minio["buckets"][layer]

        output_path = f"s3a://{bucket}/{source}/{table}"

        (
            df.write
            .mode(mode)
            .parquet(output_path)
        )

        print("=" * 70)
        print("Write Successful")
        print(f"Layer  : {layer}")
        print(f"Source : {source}")
        print(f"Table  : {table}")
        print(f"Path   : {output_path}")
        print("=" * 70)