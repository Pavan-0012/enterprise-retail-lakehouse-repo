from pyspark.sql import SparkSession

from etl.common.config import Config
from etl.common.constants import CONFIG_PATH

config = Config(CONFIG_PATH)


class PostgresReader:

    def __init__(self, spark: SparkSession):
        self.spark = spark

    def read(self, table: str):

        url = (
            f"jdbc:postgresql://"
            f"{config.get('postgres', 'host')}:"
            f"{config.get('postgres', 'port')}/"
            f"{config.get('postgres', 'database')}"
        )

        df = (
            self.spark.read
            .format("jdbc")
            .option("url", url)
            .option("dbtable", f"{config.get('postgres', 'schema')}.{table}")
            .option("user", config.get("postgres", "username"))
            .option("password", config.get("postgres", "password"))
            .option("driver", "org.postgresql.Driver")
            .load()
        )

        return df