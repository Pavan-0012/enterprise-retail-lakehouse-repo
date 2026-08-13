from datetime import datetime


class IngestionMetadata:

    @staticmethod
    def build(
        df,
        layer,
        source,
        table,
        execution_time
    ):

        return {

            "layer": layer,

            "source": source,

            "table": table,

            "rows": df.count(),

            "columns": len(df.columns),

            "ingestion_time": datetime.utcnow().isoformat(),

            "execution_time": execution_time,

            "status": "SUCCESS"
        }