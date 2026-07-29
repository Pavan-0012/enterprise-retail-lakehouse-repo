from pathlib import Path

import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Engine

from seed.postgres.database import get_schema


class PostgresLoader:

    def __init__(self, engine: Engine):
        self.engine = engine
        self.schema = get_schema()

    def load_table(
        self,
        csv_path: Path,
        table_name: str,
    ) -> None:

        print(f"\nLoading {table_name}...")

        df = pd.read_csv(csv_path)

        with self.engine.begin() as conn:
            conn.execute(
                text(
                    f'DROP TABLE IF EXISTS "{self.schema}"."{table_name}" CASCADE'
                )
            )

        df.to_sql(
            name=table_name,
            con=self.engine,
            schema=self.schema,
            if_exists="replace",
            index=False,
            method="multi",
            chunksize=5000,
        )

        print(f"Loaded {len(df):,} rows into {self.schema}.{table_name}")