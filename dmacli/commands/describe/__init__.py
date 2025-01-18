
import click

from dmacli.commands.describe.config import config

@click.group()
def describe():
    pass

describe.add_command(config)