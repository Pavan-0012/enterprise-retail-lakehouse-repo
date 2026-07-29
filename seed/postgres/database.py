from sqlalchemy import create_engine

from etl.common.config import Config
from etl.common.constants import CONFIG_PATH

config = Config(CONFIG_PATH)


def get_postgres_config():
    return config.section("postgres")


def get_schema():
    return config.get("postgres", "schema")


def get_engine():
    postgres = get_postgres_config()

    connection = (
        f"postgresql://{postgres['username']}:"
        f"{postgres['password']}@"
        f"{postgres['host']}:"
        f"{postgres['port']}/"
        f"{postgres['database']}"
    )

    return create_engine(connection)