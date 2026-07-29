from pathlib import Path

import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Engine

from seed.postgres.database import get_schema


class PostgresValidator:

    def __init__(self, engine: Engine):
        self.engine = engine
        self.schema = get_schema()

    def validate(
        self,
        csv_path: Path,
        table_name: str,
    ) -> bool:

        csv_count = len(pd.read_csv(csv_path))

        with self.engine.connect() as conn:
            db_count = conn.execute(
                text(
                    f'SELECT COUNT(*) FROM "{self.schema}"."{table_name}"'
                )
            ).scalar()

        status = "PASS" if csv_count == db_count else "FAIL"

        print(
            f"{table_name:<20}"
            f"{csv_count:>15,}"
            f"{db_count:>20,}"
            f"{status:>10}"
        )

        return csv_count == db_count