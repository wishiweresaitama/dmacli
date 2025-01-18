import base64
import logging
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import click

from dmacli.configuration import Configuration
from dmacli.constants import BUILDER_RELATIVE_PATH

@click.command()
@click.option('-s', '--source', help='Source directory', type=click.Path(exists=True, dir_okay=True), required=True)
@click.option('-d', '--destination', help='Destination directory', type=click.Path(dir_okay=True), required=True)
def build(source: click.Path, destination: click.Path):
    os.makedirs(destination, exist_ok=True)
    executable = Path(Configuration().get().toolsPath, BUILDER_RELATIVE_PATH)
    
    prefix = ''
    try:
        with open(os.path.join(source, '.prefix'), 'r') as file:
            prefix = file.read()
    except FileNotFoundError:
        logging.info('No prefix file found, using module name as prefix')

    source_encoded = base64.b64encode(source.encode()).decode()
    
    logging.info(f'Building module {source} to {destination}')
    logging.info(f'Encoded source: {source_encoded} | Prefix: {prefix}')

    subprocess.run(
        [
            executable.name,
            source,
            Path(destination, 'addons'),
            f'-prefix={prefix}',
            f'-temp={Path(tempfile.gettempdir(), source_encoded)}',
        ],
        cwd=executable.parent,
        shell=True,
    ).check_returncode()

    shutil.copyfile(
        Path(source, 'mod.cpp'),
        Path(destination, 'mod.cpp'),
    )
