from pathlib import Path


class FileManager:

    @staticmethod
    def list_csv(path):

        return sorted(Path(path).glob("*.csv"))

    @staticmethod
    def exists(path):

        return Path(path).exists()

    @staticmethod
    def create(path):

        Path(path).mkdir(parents=True, exist_ok=True)