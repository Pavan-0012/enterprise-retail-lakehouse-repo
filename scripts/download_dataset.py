import zipfile

from kaggle.api.kaggle_api_extended import KaggleApi

from etl.common.config import Config
from etl.common.constants import CONFIG_PATH
from etl.common.utils import create_run_folder


def main():

    config = Config(CONFIG_PATH)

    dataset = config.get("kaggle", "dataset")

    dataset_name = config.get("dataset", "name")

    raw_path = config.get("paths", "raw")

    output_dir = create_run_folder(
        f"{raw_path}/{dataset_name}"
    )

    print("=" * 60)
    print("Downloading Kaggle Dataset")
    print("=" * 60)
    print(f"Dataset : {dataset}")
    print(f"Output   : {output_dir}")
    print("=" * 60)

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(
        dataset,
        path=str(output_dir),
        unzip=False
    )

    zip_file = next(output_dir.glob("*.zip"))

    print("Extracting dataset...")

    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(output_dir)

    zip_file.unlink()

    print("Download completed.")
    print(f"Files stored in {output_dir}")


if __name__ == "__main__":
    main()