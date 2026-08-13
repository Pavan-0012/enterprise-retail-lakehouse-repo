from etl.common.duckdb import get_duckdb_connection
from etl.common.iceberg import IcebergReader
from etl.silver.config import SilverConfig

con = get_duckdb_connection()
reader = IcebergReader()
config = SilverConfig()

for dataset in config.datasets():

    if not dataset["enabled"]:
        continue

    table = dataset["silver_table"]

    metadata = reader._metadata_path(table)

    print(f"Registering {table}")

    con.execute(f"""
        CREATE OR REPLACE VIEW {table} AS
        SELECT *
        FROM iceberg_scan('{metadata}')
    """)

print("\nAll Iceberg views registered successfully.")