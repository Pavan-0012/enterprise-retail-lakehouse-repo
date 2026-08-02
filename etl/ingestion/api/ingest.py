from etl.common.metadata.ingestion_metadata import IngestionMetadata
from etl.common.metadata.timer import PipelineTimer
from etl.ingestion.api.reader import ApiReader
from etl.ingestion.common.spark import get_spark_session
from etl.ingestion.common.writer import RawWriter


def main():

    timer = PipelineTimer()

    timer.start_timer()

    spark = get_spark_session()

    reader = ApiReader(spark)

    writer = RawWriter()

    df = reader.read(
        "http://localhost:8000/reviews"
    )

    writer.write(
        df=df,
        layer="raw",
        source="api",
        table="reviews"
    )

    metadata = IngestionMetadata.build(
        df=df,
        layer="raw",
        source="api",
        table="reviews",
        execution_time=timer.stop_timer()
    )

    print(metadata)

    spark.stop()


if __name__ == "__main__":
    main()