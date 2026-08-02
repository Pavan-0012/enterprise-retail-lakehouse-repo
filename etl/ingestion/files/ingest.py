from pathlib import Path

from etl.common.metadata.ingestion_metadata import IngestionMetadata
from etl.common.metadata.timer import PipelineTimer
from etl.ingestion.common.spark import get_spark_session
from etl.ingestion.common.writer import RawWriter
from etl.ingestion.files.reader import FileReader


def main():

    timer = PipelineTimer()

    timer.start_timer()

    spark = get_spark_session()

    reader = FileReader(spark)

    writer = RawWriter()

    latest_folder = max(
        (Path("data/raw/olist")).iterdir(),
        key=lambda folder: folder.name
    )

    csv_file = latest_folder / "olist_geolocation_dataset.csv"

    df = reader.read(str(csv_file))

    writer.write(
        df=df,
        layer="raw",
        source="files",
        table="geolocation"
    )

    metadata = IngestionMetadata.build(
        df=df,
        layer="raw",
        source="files",
        table="geolocation",
        execution_time=timer.stop_timer()
    )

    print(metadata)

    spark.stop()


if __name__ == "__main__":
    main()