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

# Latest timestamped folder
DATA_DIRECTORY = snapshots[-1]

TABLE_MAPPING = {
    "olist_customers_dataset.csv": "customers",
    "olist_orders_dataset.csv": "orders",
    "olist_order_items_dataset.csv": "order_items",
    "olist_order_payments_dataset.csv": "payments",
    "olist_products_dataset.csv": "products",
    "olist_sellers_dataset.csv": "sellers",
}