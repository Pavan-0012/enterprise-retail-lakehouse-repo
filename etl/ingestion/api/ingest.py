from etl.common.metadata.ingestion_metadata import IngestionMetadata
from etl.common.metadata.timer import PipelineTimer
from etl.common.source_config import SourceConfig

from etl.ingestion.api.reader import ApiReader
from etl.ingestion.common.spark import get_spark_session
from etl.ingestion.common.writer import RawWriter


def main():

    spark = get_spark_session()

    reader = ApiReader(spark)

    writer = RawWriter()

    config = SourceConfig()

    for endpoint in config.api_endpoints():

        if not endpoint["enabled"]:
            continue

        timer = PipelineTimer()
        timer.start_timer()

        print(f"\nIngesting API endpoint : {endpoint['name']}")

        df = reader.read(endpoint["name"])

        writer.write(
            df=df,
            layer="raw",
            source="api",
            table=endpoint["target_table"]
        )

        metadata = IngestionMetadata.build(
            df=df,
            layer="raw",
            source="api",
            table=endpoint["target_table"],
            execution_time=timer.stop_timer()
        )

        print("=" * 70)
        print("INGESTION METADATA")
        print("=" * 70)

        for key, value in metadata.items():
            print(f"{key:<25}: {value}")

        print("=" * 70)

    spark.stop()


if __name__ == "__main__":
    main()