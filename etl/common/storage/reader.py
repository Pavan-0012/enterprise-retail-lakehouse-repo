from pyspark.sql import DataFrame
from pyspark.sql import SparkSession

from etl.common.config import Config
from etl.common.constants import CONFIG_PATH

config = Config(CONFIG_PATH)


class StorageReader:

    def __init__(self, spark: SparkSession):

        self.spark = spark

        self.minio = config.section("minio")

    def read(
        self,
        layer: str,
        source: str,
        table: str
    ) -> DataFrame:

        bucket = self.minio["buckets"][layer]

        input_path = f"s3a://{bucket}/{source}/{table}"

        print("=" * 70)
        print("READING DATASET")
        print("=" * 70)
        print(f"Layer  : {layer}")
        print(f"Source : {source}")
        print(f"Table  : {table}")
        print(f"Path   : {input_path}")
        print("=" * 70)

        return self.spark.read.parquet(input_path)