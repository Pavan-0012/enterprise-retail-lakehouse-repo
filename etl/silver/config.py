import json

from etl.common.constants import PROJECT_ROOT


CONFIG_PATH = PROJECT_ROOT / "configs" / "silver.json"


class SilverConfig:

    def __init__(self):

        with open(CONFIG_PATH, "r", encoding="utf-8") as file:
            self.config = json.load(file)

    def datasets(self):

        return self.config["datasets"]