from pathlib import Path

from etl.storage.manager import StorageManager
from etl.common.config import Config
from etl.common.constants import CONFIG_PATH

config = Config(CONFIG_PATH)

storage = StorageManager()

# Read raw path from config
raw_path = config.get("paths", "raw")

dataset_folder = Path(raw_path)

files = list(dataset_folder.glob("*.csv"))

print(f"Found {len(files)} CSV files")

for file in files:
    object_name = f"raw/{file.name}"

    print(f"Uploading {file.name}...")

    storage.upload_file(
        str(file),
        object_name
    )

    print(f"✅ Uploaded {file.name}")

print("All files uploaded successfully!")