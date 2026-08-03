import json

from pathlib import Path

from etl.common.constants import PROJECT_ROOT


CONFIG_FILE = PROJECT_ROOT / "configs" / "sources.json"


class SourceConfig:

    def __init__(self):

        with open(CONFIG_FILE, "r") as f:

            self.config = json.load(f)

    def postgres_tables(self):

        return self.config["postgres"]["tables"]

    def api_endpoints(self):

        return self.config["api"]["endpoints"]

    def file_datasets(self):

        return self.config["files"]["datasets"]