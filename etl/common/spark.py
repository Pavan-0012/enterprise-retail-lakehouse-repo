from pyspark.sql import SparkSession

from etl.common.config import Config
from etl.common.constants import CONFIG_PATH


class SparkSessionFactory:
    """
    Factory for creating configured Spark sessions.
    """

    @staticmethod
    def create():

        config = Config(CONFIG_PATH)

        spark = (
            SparkSession.builder
            .appName(config.get("spark", "app_name"))
            .master(config.get("spark", "master"))

            .config(
                "spark.driver.memory",
                config.get("spark", "driver_memory")
            )

            .config(
                "spark.executor.memory",
                config.get("spark", "executor_memory")
            )

            .config(
                "spark.sql.shuffle.partitions",
                config.get("spark", "shuffle_partitions")
            )

            .config(
                "spark.sql.session.timeZone",
                config.get("spark", "timezone")
            )

            .getOrCreate()
        )

        spark.sparkContext.setLogLevel("WARN")

        return spark