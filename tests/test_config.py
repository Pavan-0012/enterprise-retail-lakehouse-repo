from etl.common.config import Config
from etl.common.constants import CONFIG_PATH


def main():

    config = Config(CONFIG_PATH)

    print("=" * 60)

    print("Project")

    print(config.get("project", "name"))

    print("=" * 60)

    print("Spark")

    print(config.get("spark", "app_name"))

    print(config.get("spark", "master"))

    print("=" * 60)

    print("MinIO")

    print(config.get("minio", "endpoint"))

    print(config.get("bucket", "name"))

    print("=" * 60)

    print("Dataset")

    print(config.get("dataset", "name"))

    print(config.get("kaggle", "dataset"))

    print("=" * 60)


if __name__ == "__main__":
    main()