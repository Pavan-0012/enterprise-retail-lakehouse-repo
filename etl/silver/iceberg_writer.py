from pyspark.sql import DataFrame
from pyspark.sql import SparkSession


class IcebergWriter:

    def __init__(self, spark: SparkSession):

        self.spark = spark

    def create_namespace(
        self,
        namespace: str
    ):

        self.spark.sql(
            f"""
            CREATE NAMESPACE IF NOT EXISTS
            enterprise.{namespace}
            """
        )

    def write(
        self,
        df: DataFrame,
        dataset: dict
    ):

        namespace = dataset.get("namespace","silver")

        table = dataset["silver_table"]

        write_mode = dataset.get(
            "write_mode",
            "overwrite"
        )

        self.create_namespace(namespace)

        table_name = (
            f"enterprise.{namespace}.{table}"
        )

        if write_mode == "overwrite":

            (
                df.writeTo(table_name)
                .using("iceberg")
                .createOrReplace()
            )

        elif write_mode == "append":

            (
                df.writeTo(table_name)
                .append()
            )

        print("=" * 70)

        print(f"Iceberg Table : {table_name}")

        print(f"Mode          : {write_mode}")

        print("=" * 70)