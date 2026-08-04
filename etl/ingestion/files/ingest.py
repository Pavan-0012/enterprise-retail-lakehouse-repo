from pathlib import Path

from etl.common.metadata.ingestion_metadata import IngestionMetadata
from etl.common.metadata.timer import PipelineTimer
from etl.common.source_config import SourceConfig

from etl.common.spark import get_spark_session
from etl.common.storage.writer import StorageWriter
from etl.ingestion.files.reader import FileReader


def main():

    spark = get_spark_session()

    reader = FileReader(spark)

    writer = StorageWriter()

    config = SourceConfig()

    latest_folder = max(
        Path("data/raw/olist").iterdir(),
        key=lambda folder: folder.name
    )

    for dataset in config.file_datasets():

        if not dataset["enabled"]:
            continue

        timer = PipelineTimer()
        timer.start_timer()

        csv_file = latest_folder / dataset["file"]

        print(f"\nIngesting File : {csv_file.name}")

        df = reader.read(str(csv_file))

        writer.write(
            df=df,
            layer="raw",
            source="files",
            table=dataset["target_table"]
        )

        metadata = IngestionMetadata.build(
            df=df,
            layer="raw",
            source="files",
            table=dataset["target_table"],
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