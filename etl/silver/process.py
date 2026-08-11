from etl.common.metadata.ingestion_metadata import IngestionMetadata
from etl.common.metadata.timer import PipelineTimer
from etl.common.spark import get_spark_session
from etl.common.storage.reader import StorageReader

from etl.silver.config import SilverConfig
from etl.silver.transformer import SilverTransformer
from etl.silver.validator import SilverValidator
from etl.silver.iceberg_writer import IcebergWriter
from etl.silver.logger import SilverLogger


def main():

    spark = get_spark_session()

    config = SilverConfig()

    reader = StorageReader(spark)

    transformer = SilverTransformer()

    validator = SilverValidator()

    writer = IcebergWriter()

    logger = SilverLogger()

    for dataset in config.datasets():

        if not dataset["enabled"]:
            continue

        timer = PipelineTimer()

        timer.start_timer()

        try:

            print(f"\nProcessing {dataset['silver_table']}")

            df = reader.read(
                layer="bronze",
                source=dataset["source"],
                table=dataset["bronze_table"]
            )

            original_df = df

            df = transformer.transform(
                df,
                dataset
            )

            metrics = validator.validate(
                original_df,
                df,
                dataset
            )

            writer.write(
                df=df,
                table=dataset["silver_table"]
            )

            metadata = IngestionMetadata.build(
                df=df,
                layer="silver",
                source=dataset["source"],
                table=dataset["silver_table"],
                execution_time=timer.stop_timer()
            )

            logger.log(
                dataset = dataset,
                metrics = metrics,
                execution_time=metadata["execution_time"]
            )

        except Exception as e:

            print("\n" + "=" * 70)
            print("FAILED")
            print("=" * 70)
            print(f"Source        : {dataset['source']}")
            print(f"Bronze Table  : {dataset['bronze_table']}")
            print(f"Silver Table  : {dataset['silver_table']}")
            print(f"Error         : {e}")
            print("=" * 70)

    spark.stop()


if __name__ == "__main__":
    main()