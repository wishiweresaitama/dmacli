import json
import logging

from pathlib import Path
from dmacli.constants import CONFIGURATION_DIR, CONFIGURATION_NAME
from dmacli.models.config import ConfigurationModel
from dmacli.utils.singleton import Singleton


class Configuration(metaclass=Singleton):
    _config = None

    def __init__(self):
        self.refresh()

    def refresh(self):
        try:
            with open(Path.home() / CONFIGURATION_DIR / CONFIGURATION_NAME, 'r') as file:
                self._config = ConfigurationModel(
                    **json.loads(
                        file.read(),
                        ),
                    )
        except FileNotFoundError:
            logging.warning(f"Configuration file not found, creating default configuration")
            self._config = ConfigurationModel()

    def get(self):
        return self._config

    def set(self, param: str, value: str):
        if not ConfigurationModel.is_valid_parameter(param):
            raise ValueError(f"Parameter {param} is not valid")
        
        setattr(self._config, param, value)

    def dump(self):
        return self._config.model_dump_json(indent=4)

    def save(self):
        os.makedirs(Path.home() / CONFIGURATION_DIR, exist_ok=True)
        with open(Path.home() / CONFIGURATION_DIR / CONFIGURATION_NAME, 'w') as file:
            file.write(self.dump())
