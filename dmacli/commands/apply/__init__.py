import click

from dmacli.commands.apply.config import config
from dmacli.commands.apply.parameter import parameter
@click.group()
def apply():
    pass

apply.add_command(config)
apply.add_command(parameter)