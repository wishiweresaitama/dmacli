import logging
import os
from pathlib import Path
import subprocess
import click

from dmacli.common.modification import Modification
from dmacli.configuration import Configuration
from dmacli.constants import WORKBENCH_RELATIVE_PATH
from dmacli.utils.utils import create_junction, prepare_mods

@click.command()
@click.option(
    '-m',
    '--modifications',
    help='Modifications to be debugged',
    required=True,
    multiple=True,
    type=str)
def debug(modifications):
    junctions = []

    for modification_path in modifications:
        modification = Modification(modification_path)
        if modification.is_valid():
            junction_path = Path(
                Configuration().get().drivePath,
                modification.get_prefix(),
            )
            os.makedirs(junction_path.parent, exist_ok=True)

            create_junction(modification.get_path(), junction_path)
            junctions.append(str(junction_path))
    
    if not junctions:
        logging.error('No valid modifications were provided')
        exit(1)

    executable = Path(Configuration().get().toolsPath, WORKBENCH_RELATIVE_PATH)
    executable_args = prepare_mods(junctions)
    
    print(f'Running: {executable.name} {executable_args}')

    subprocess.run(f'{executable.name} {executable_args}', cwd=executable.parent, shell=True)