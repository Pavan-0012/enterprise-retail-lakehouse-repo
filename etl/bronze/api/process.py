from etl.common.metadata.ingestion_metadata import IngestionMetadata
from etl.common.metadata.timer import PipelineTimer
from etl.common.source_config import SourceConfig
from etl.common.spark import get_spark_session
from etl.common.storage.reader import StorageReader
from etl.common.storage.writer import StorageWriter


def main():

    spark = get_spark_session()

    reader = StorageReader(spark)

    writer = StorageWriter()

    config = SourceConfig()

    print("=" * 70)
    print("API RAW → BRONZE")
    print("=" * 70)

    for endpoint in config.api_endpoints():

        if not endpoint["enabled"]:
            continue

        timer = PipelineTimer()
        timer.start_timer()

        print(f"\nProcessing : {endpoint['target_table']}")

        df = reader.read(
            layer="raw",
            source="api",
            table=endpoint["target_table"]
        )

        writer.write(
            df=df,
            layer="bronze",
            source="api",
            table=endpoint["target_table"]
        )

        metadata = IngestionMetadata.build(
            df=df,
            layer="bronze",
            source="api",
            table=endpoint["target_table"],
            execution_time=timer.stop_timer()
        )

        print(metadata)

    spark.stop()


if __name__ == "__main__":
    main()