from pyspark.sql import SparkSession


class FileReader:

    def __init__(self, spark: SparkSession):

        self.spark = spark

    def read(self, path: str):

        return (

            self.spark.read

            .option("header", True)

            .option("inferSchema", True)

            .csv(path)
        )