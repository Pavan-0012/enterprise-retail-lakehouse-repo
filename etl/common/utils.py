from datetime import datetime
from pathlib import Path


def generate_run_id():
    """
    Generate ingestion run id.
    """

    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def create_run_folder(base_path):
    """
    Create timestamped folder.
    """

    run_id = generate_run_id()

    folder = Path(base_path) / run_id

    folder.mkdir(parents=True, exist_ok=True)

    return folder