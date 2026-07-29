from black.schema import get_schema


class PostgresLoader:

    def __init__(self, engine):
        self.engine = engine
        self.schema = get_schema()


class PostgresValidator:

    def __init__(self, engine):
        self.engine = engine
        self.schema = get_schema()

class PostgresLoader:

    def __init__(self, engine):
        self.engine = engine
        self.schema = get_schema()