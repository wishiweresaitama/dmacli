import json
import os
from pathlib import Path
import click

from dmacli.constants import CONFIGURATION_DIR, CONFIGURATION_NAME
from dmacli.models.config import ConfigurationModel


@click.command(name='config')
@click.option('-f', '--file', help='Path to the configuration file', required=True)
def config(file: str):
    try:
        f = open(file, 'r')
    except FileNotFoundError:
        print(f"File {file} not found")
        return
    
    try:
        data = json.load(f)
    except json.JSONDecodeError:
        print(f"File {file} is not a valid JSON file")
        return
    
    f.close()
    configuration = ConfigurationModel(**data)
    
    home = Path.home()
    config_path = home / CONFIGURATION_DIR / CONFIGURATION_NAME
    os.makedirs(config_path.parent, exist_ok=True)

    with open(config_path, 'w') as f:
        f.write(configuration.model_dump_json())
    print(f"Configuration applied to {config_path}")