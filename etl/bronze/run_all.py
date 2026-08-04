from etl.bronze.postgres.process import main as postgres
from etl.bronze.api.process import main as api
from etl.bronze.files.process import main as files


def main():

    postgres()

    api()

    files()


if __name__ == "__main__":
    main()