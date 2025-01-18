import json
from pathlib import Path
import click

from dmacli.constants import CONFIGURATION_DIR, CONFIGURATION_NAME
from dmacli.models.config import ConfigurationModel


@click.command()
def config():
    home = Path.home()
    config_path = home / CONFIGURATION_DIR / CONFIGURATION_NAME
    try:
        f = open(config_path, 'r')
    except FileNotFoundError:
        print(f"Configuration file not found at {config_path}")
        return
    
    data = json.load(f)
    f.close()
    
    configuration = ConfigurationModel(**data)
    print(configuration.model_dump_json(indent=4))