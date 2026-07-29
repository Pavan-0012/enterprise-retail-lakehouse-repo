from pathlib import Path

import yaml


class Config:
    """
    Loads and merges all YAML configuration files.
    """

    def __init__(self, config_directory):

        self._config = {}

        config_directory = Path(config_directory)

        if not config_directory.exists():
            raise FileNotFoundError(
                f"Configuration directory not found: {config_directory}"
            )

        yaml_files = sorted(config_directory.glob("*.yaml"))

        for yaml_file in yaml_files:

            with yaml_file.open("r", encoding="utf-8") as stream:

                data = yaml.safe_load(stream)

                if data:

                    self._config.update(data)

    def get(self, section, key):

        if section not in self._config:
            raise KeyError(
                f"Section '{section}' not found."
            )

        values = self._config[section]

        if key not in values:
            raise KeyError(
                f"Key '{key}' not found in section '{section}'."
            )

        return values[key]

    def section(self, section):

        return self._config.get(section, {})

    def has_section(self, section):

        return section in self._config

    def has_key(self, section, key):

        return (
            section in self._config
            and key in self._config[section]
        )