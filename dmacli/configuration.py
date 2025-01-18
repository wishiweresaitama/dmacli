import json
from pathlib import Path
from dmacli.constants import CONFIGURATION_DIR, CONFIGURATION_NAME
from dmacli.models.config import ConfigurationModel
from dmacli.utils.singleton import Singleton


class Configuration(metaclass=Singleton):
    _config = None

    def __init__(self):
        self.refresh()

    def refresh(self):
        with open(Path.home() / CONFIGURATION_DIR / CONFIGURATION_NAME, 'r') as file:
            self._config = ConfigurationModel(
                **json.loads(
                    file.read(),
                ),
            )

    def get(self):
        return self._config

    def dump(self):
        return self._config.model_dump_json(indent=4)