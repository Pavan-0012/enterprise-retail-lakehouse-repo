from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CONFIG_PATH = PROJECT_ROOT / "configs" / "config.yaml"

RAW_PATH = PROJECT_ROOT / "data" / "raw"
BRONZE_PATH = PROJECT_ROOT / "data" / "bronze"
SILVER_PATH = PROJECT_ROOT / "data" / "silver"
GOLD_PATH = PROJECT_ROOT / "data" / "gold"