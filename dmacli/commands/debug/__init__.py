import logging
import os
from pathlib import Path
import subprocess
import click

from dmacli.configuration import Configuration
from dmacli.constants import WORKBENCH_RELATIVE_PATH
from dmacli.utils.utils import prepare_mods

@click.command()
@click.option(
    '-m',
    '--modifications',
    help='Modifications to be debugged',
    required=True,
    multiple=True,
    type=str)
def debug(modifications):
    valid_modifications = []

    for modification in modifications:
        if not os.path.exists(modification):
            continue
        
        valid_modifications.append(modification)
    
    if not valid_modifications:
        logging.error('No valid modifications were provided')
        exit(1)

    executable = Path(Configuration().get().toolsPath, WORKBENCH_RELATIVE_PATH)
    executable_args = prepare_mods([x + '\\Scripts' for x in valid_modifications])

    subprocess.run(f'{executable.name} {executable_args}', cwd=executable.parent, shell=True)