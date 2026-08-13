from etl.common.duckdb import get_duckdb_connection


class IcebergReader:

    def __init__(self):

        self.con = get_duckdb_connection()

    def _metadata_path(self, table):

        version = self.con.execute(f"""
            SELECT content
            FROM read_text(
                's3://silver/silver/{table}/metadata/version-hint.text'
            )
        """).fetchone()[0].strip()

        return (
            f"s3://silver/silver/{table}/metadata/"
            f"v{version}.metadata.json"
        )

    def dataframe(self, table):

        metadata = self._metadata_path(table)

        return self.con.execute(f"""
            SELECT *
            FROM iceberg_scan('{metadata}')
        """).fetchdf()

    def count(self, table):

        metadata = self._metadata_path(table)

        return self.con.execute(f"""
            SELECT COUNT(*)
            FROM iceberg_scan('{metadata}')
        """).fetchone()[0]

    def schema(self, table):

        metadata = self._metadata_path(table)

        return self.con.execute(f"""
            DESCRIBE
            SELECT *
            FROM iceberg_scan('{metadata}')
        """).fetchdf()