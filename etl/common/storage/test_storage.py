from etl.common.storage.reader import StorageReader
from etl.common.spark import get_spark_session


def main():

    spark = get_spark_session()

    reader = StorageReader(spark)

    df = reader.read(
        layer="raw",
        source="postgres",
        table="customers"
    )

    print("\nSchema")
    df.printSchema()

    print(f"\nRows : {df.count()}")

    df.show(5, truncate=False)

    spark.stop()


if __name__ == "__main__":
    main()