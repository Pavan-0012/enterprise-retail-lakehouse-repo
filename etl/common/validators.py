from pathlib import Path


def validate_file(path):

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist")

    return True