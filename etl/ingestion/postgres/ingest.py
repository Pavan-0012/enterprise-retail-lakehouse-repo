from etl.ingestion.common.spark import get_spark_session
from etl.ingestion.common.writer import RawWriter
from etl.ingestion.postgres.reader import PostgresReader
from etl.common.metadata.timer import PipelineTimer
from etl.common.metadata.ingestion_metadata import IngestionMetadata
from etl.ingestion.metadata import timer


def main():
    timer = PipelineTimer()

    timer.start_timer()

    spark = get_spark_session()

    reader = PostgresReader(spark)

    writer = RawWriter()

    df = reader.read("customers")

    df.printSchema()

    df.show(5, truncate=False)

    print("Output Path:", "data/raw/postgres/customers")
    print("fs.defaultFS =", spark.sparkContext._jsc.hadoopConfiguration().get("fs.defaultFS"))

    writer.write(
    df=df,
    layer="raw",
    source="postgres",
    table="customers"
    )

    execution_time = timer.stop_timer()

    metadata = IngestionMetadata.build(
        df=df,
        layer="raw",
        source="postgres",
        table="customers",
        execution_time=execution_time
    )

    print("\n")
    print("=" * 70)
    print("INGESTION METADATA")
    print("=" * 70)

    for key, value in metadata.items():
        print(f"{key:<25}: {value}")

    print("=" * 70)

    spark.stop()


if __name__ == "__main__":
    main()