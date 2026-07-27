from pyspark.sql import SparkSession


def create_spark(app_name: str):

    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName(app_name)
        .config("spark.sql.session.timeZone", "UTC")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    return spark