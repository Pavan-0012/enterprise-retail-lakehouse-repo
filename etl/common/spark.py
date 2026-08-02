from pyspark.sql import SparkSession

from etl.common.config import Config
from etl.common.constants import CONFIG_PATH

config = Config(CONFIG_PATH)


def get_spark_session():

    spark_cfg = config.section("spark")

    builder = (
        SparkSession.builder
        .appName(spark_cfg["app_name"])
        .master(spark_cfg["master"])
    )

    packages = ",".join(spark_cfg["packages"])

    builder = builder.config(
        "spark.jars.packages",
        packages
    )

    for key, value in spark_cfg["configs"].items():
        builder = builder.config(key, value)

    spark = builder.getOrCreate()

    return spark