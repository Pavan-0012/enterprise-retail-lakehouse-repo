from pyspark.sql import DataFrame
from pyspark.sql.functions import col, trim, current_timestamp
from pyspark.sql.types import StringType


class SilverTransformer:

    def transform(
        self,
        df: DataFrame,
        dataset: dict
    ) -> DataFrame:

        cleaning = dataset.get("cleaning", {})

        # Trim all string columns
        if cleaning.get("trim_strings", True):

            for field in df.schema.fields:

                if isinstance(field.dataType, StringType):

                    df = df.withColumn(
                        field.name,
                        trim(col(field.name))
                    )

        # Remove NULL Primary Keys
        if cleaning.get("drop_null_primary_keys", True):

            df = df.dropna(
                subset=dataset["primary_keys"]
            )

        # Remove Duplicate Primary Keys
        if cleaning.get("drop_duplicates", True):

            df = df.dropDuplicates(
                dataset["primary_keys"]
            )

        # Audit Columns
        if dataset.get("audit_columns", True):

            df = df.withColumn(
                "created_timestamp",
                current_timestamp()
            )

        return df