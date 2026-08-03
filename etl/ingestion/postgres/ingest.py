from etl.common.metadata.ingestion_metadata import IngestionMetadata
from etl.common.metadata.timer import PipelineTimer
from etl.common.source_config import SourceConfig
from etl.ingestion.common.spark import get_spark_session
from etl.ingestion.common.writer import RawWriter
from etl.ingestion.postgres.reader import PostgresReader


def main():

    spark = get_spark_session()

    reader = PostgresReader(spark)

    writer = RawWriter()

    config = SourceConfig()

    for table in config.postgres_tables():

        if not table["enabled"]:
            continue

        timer = PipelineTimer()

        timer.start_timer()

        df = reader.read(table["source_table"])

        writer.write(
            df=df,
            layer="raw",
            source="postgres",
            table=table["target_table"]
        )

        metadata = IngestionMetadata.build(
            df=df,
            layer="raw",
            source="postgres",
            table=table["target_table"],
            execution_time=timer.stop_timer()
        )

        print(metadata)

    spark.stop()


if __name__ == "__main__":
    main()