import duckdb


def get_duckdb_connection():

    con = duckdb.connect("warehouse.duckdb")

    con.install_extension("httpfs")
    con.load_extension("httpfs")

    con.install_extension("iceberg")
    con.load_extension("iceberg")

    con.execute("""
    CREATE PERSISTENT SECRET IF NOT EXISTS minio (
        TYPE S3,
        KEY_ID 'admin',
        SECRET 'password123',
        REGION 'us-east-1',
        ENDPOINT 'localhost:9000',
        USE_SSL false,
        URL_STYLE 'path'
    );
    """)

    return con