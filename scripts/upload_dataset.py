from pathlib import Path

from etl.common.config import Config
from etl.common.constants import CONFIG_PATH
from etl.storage.manager import StorageManager


def latest_folder(dataset_path):
    """
    Return latest ingestion folder.
    """

    folders = sorted(
        [
            folder
            for folder in dataset_path.iterdir()
            if folder.is_dir()
        ]
    )

    if not folders:
        raise RuntimeError(
            f"No ingestion folders found in {dataset_path}"
        )

    return folders[-1]


def main():

    config = Config(CONFIG_PATH)

    raw_root = Path(
        config.get("paths", "raw")
    )

    dataset_name = config.get(
        "dataset",
        "name"
    )

    dataset_path = raw_root / dataset_name

    source_folder = latest_folder(
        dataset_path
    )

    manager = StorageManager()

    files = list(
        source_folder.glob("*.csv")
    )

    if not files:
        print("No CSV files found.")
        return

    print("=" * 60)
    print("Enterprise Retail Lakehouse Upload")
    print("=" * 60)
    print(f"Bucket      : {manager.bucket}")
    print(f"Dataset     : {dataset_name}")
    print(f"Run         : {source_folder.name}")
    print(f"Files Found : {len(files)}")
    print("=" * 60)

    uploaded = 0
    failed = 0

    for file in files:

        object_name = (
            f"raw/"
            f"{dataset_name}/"
            f"{source_folder.name}/"
            f"{file.name}"
        )

        try:

            print(f"Uploading {file.name}")

            manager.upload(
                file,
                object_name
            )

            uploaded += 1

            print(f"✓ Uploaded {file.name}")

        except Exception as ex:

            failed += 1

            print(f"✗ Failed {file.name}")

            print(ex)

    print("=" * 60)
    print(f"Uploaded : {uploaded}")
    print(f"Failed   : {failed}")
    print("=" * 60)


if __name__ == "__main__":
    main()