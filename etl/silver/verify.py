from etl.common.spark import get_spark_session
from etl.silver.config import SilverConfig


def main():

    spark = get_spark_session()

    config = SilverConfig()

    print("\n" + "=" * 80)
    print("VERIFYING SILVER ICEBERG TABLES")
    print("=" * 80)

    for dataset in config.datasets():

        if not dataset["enabled"]:
            continue

        table_name = (
            f"enterprise."
            f"{dataset.get('namespace', 'silver')}."
            f"{dataset['silver_table']}"
        )

        try:

            df = spark.read.table(table_name)

            print("\n" + "-" * 80)
            print(f"Table      : {table_name}")
            print(f"Rows       : {df.count()}")
            print(f"Columns    : {len(df.columns)}")

            print("\nSchema")
            df.printSchema()

            print("\nSample Data")
            df.show(5, truncate=False)

        except Exception as e:

            print("\n" + "-" * 80)
            print(f"FAILED : {table_name}")
            print(e)

    print("\n" + "=" * 80)
    print("VERIFICATION COMPLETED")
    print("=" * 80)

    spark.stop()


if __name__ == "__main__":
    main()