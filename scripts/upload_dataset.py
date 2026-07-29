from pathlib import Path

from etl.storage.manager import StorageManager

manager = StorageManager(
    "enterprise-retail-lakehouse"
)

folder = Path("data/raw")

for file in folder.glob("*.csv"):

    manager.upload(
        file,
        f"raw/{file.name}"
    )

    print(file.name)