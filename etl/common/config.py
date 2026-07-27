from pathlib import Path
import yaml


class Config:

    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.config = self._load()

    def _load(self):
        with open(self.config_path, "r") as file:
            return yaml.safe_load(file)

    def get(self, *keys):
        value = self.config

        for key in keys:
            value = value[key]

        return value