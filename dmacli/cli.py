import click

from dmacli.commands.apply import apply
from dmacli.commands.describe import describe
from dmacli.commands.create import create

@click.group()
def cli():
    pass

cli.add_command(apply)
cli.add_command(describe)
cli.add_command(create)