from pyspark.sql import SparkSession

from etl.common.config import Config
from etl.common.constants import CONFIG_PATH

config = Config(CONFIG_PATH)


def get_spark_session() -> SparkSession:

    spark_cfg = config.section("spark")
    minio_cfg = config.section("minio")

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

    # ---------- MinIO ----------
    builder = (
        builder
        .config("spark.hadoop.fs.s3a.endpoint", minio_cfg["endpoint"])
        .config("spark.hadoop.fs.s3a.access.key", minio_cfg["access_key"])
        .config("spark.hadoop.fs.s3a.secret.key", minio_cfg["secret_key"])
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .config(
            "spark.hadoop.fs.s3a.aws.credentials.provider",
            "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider"
        )
    )

    spark = builder.getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    return spark