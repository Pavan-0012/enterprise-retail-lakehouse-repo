from etl.common.iceberg import IcebergReader
from etl.silver.config import SilverConfig

reader = IcebergReader()
config = SilverConfig()

for dataset in config.datasets():

    if not dataset["enabled"]:
        continue

    table = dataset["silver_table"]

    print("=" * 60)
    print(table.upper())
    print("=" * 60)

    try:

        rows = reader.count(table)

        print(f"Rows : {rows}")

        schema = reader.schema(table)

        print(schema)

        print("SUCCESS\n")

    except Exception as e:

        print(e)