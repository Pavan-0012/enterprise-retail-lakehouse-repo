from pathlib import Path

from etl.storage.manager import StorageManager


def main():
    manager = StorageManager()

    folder = Path("data/raw")

    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    files = list(folder.glob("*.csv"))

    if not files:
        print("No CSV files found in data/raw")
        return

    print("=" * 60)
    print("Enterprise Retail Lakehouse - Dataset Upload")
    print("=" * 60)
    print(f"Bucket      : {manager.bucket}")
    print(f"Source      : {folder}")
    print(f"Files Found : {len(files)}")
    print("=" * 60)

    uploaded = 0
    failed = 0

    for file in files:
        try:
            print(f"Uploading {file.name}...")

            manager.upload(
                file_path=file,
                object_name=f"raw/{file.name}"
            )

            uploaded += 1
            print(f"✓ Uploaded {file.name}")

        except Exception as ex:
            failed += 1
            print(f"✗ Failed {file.name}")
            print(f"  Reason: {ex}")

    print("=" * 60)
    print(f"Uploaded : {uploaded}")
    print(f"Failed   : {failed}")
    print("=" * 60)


if __name__ == "__main__":
    main()