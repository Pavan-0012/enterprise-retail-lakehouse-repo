from pathlib import Path

from etl.common.constants import PROJECT_ROOT

RAW_DIRECTORY = PROJECT_ROOT / "data" / "raw" / "olist"

snapshots = sorted(
    [folder for folder in RAW_DIRECTORY.iterdir() if folder.is_dir()]
)

if not snapshots:
    raise FileNotFoundError(
        f"No snapshots found in {RAW_DIRECTORY}"
    )

DATA_DIRECTORY = snapshots[-1]

REVIEW_FILE = DATA_DIRECTORY / "olist_order_reviews_dataset.csv"