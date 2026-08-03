import requests

from pyspark.sql import SparkSession

from etl.common.config import Config
from etl.common.constants import CONFIG_PATH

config = Config(CONFIG_PATH)


class ApiReader:

    def __init__(self, spark: SparkSession):

        self.spark = spark

        api_config = config.section("api")

        self.base_url = api_config["base_url"]

        self.timeout = api_config["timeout"]

        self.endpoints = api_config["endpoints"]

    def read(self, endpoint: str):

        if endpoint not in self.endpoints:
            raise ValueError(
                f"Endpoint '{endpoint}' not configured."
            )

        url = self.base_url + self.endpoints[endpoint]

        print("=" * 70)
        print(f"Calling API : {url}")
        print("=" * 70)

        response = requests.get(
            url,
            timeout=self.timeout
        )

        response.raise_for_status()

        json_data = response.json()

        return self.spark.createDataFrame(json_data)