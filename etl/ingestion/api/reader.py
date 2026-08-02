import requests

from pyspark.sql import SparkSession


class ApiReader:

    def __init__(self, spark: SparkSession):

        self.spark = spark

    def read(self, url: str):

        response = requests.get(url, timeout=30)

        response.raise_for_status()

        json_data = response.json()

        return self.spark.createDataFrame(json_data)