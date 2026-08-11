from pyspark.sql import DataFrame


class IcebergWriter:

    def write(
        self,
        df: DataFrame,
        table: str
    ):

        full_table = f"enterprise.default.{table}"

        (
            df.writeTo(full_table)
            .using("iceberg")
            .createOrReplace()
        )

        print(f"Iceberg table created : {full_table}")