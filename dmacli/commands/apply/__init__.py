import click

from dmacli.commands.apply.config import config

@click.group()
def apply():
    pass

apply.add_command(config)