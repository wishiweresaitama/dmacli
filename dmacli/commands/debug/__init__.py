import logging
import os
from pathlib import Path
import subprocess
import click

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

    for modification in modifications:
        if not os.path.exists(modification):
            continue
        
        junction_path = os.path.join(
            Configuration().get().drivePath,
            os.path.split(modification)[1],
        )

        create_junction(modification, junction_path)
        junctions.append(junction_path)
    
    if not junctions:
        logging.error('No valid modifications were provided')
        exit(1)

    executable = Path(Configuration().get().toolsPath, WORKBENCH_RELATIVE_PATH)
    executable_args = prepare_mods(junctions)

    subprocess.run(f'{executable.name} {executable_args}', cwd=executable.parent, shell=True)