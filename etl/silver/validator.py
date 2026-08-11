from pyspark.sql import DataFrame


class SilverValidator:

    def validate(
        self,
        original_df: DataFrame,
        transformed_df: DataFrame,
        dataset: dict
    ) -> dict:

        metrics = {

            "rows_before": original_df.count(),

            "rows_after": transformed_df.count(),

            "duplicates_removed":
                original_df.count()
                - transformed_df.count(),

            "status": "SUCCESS"
        }

        return metrics