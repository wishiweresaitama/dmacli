import click

from dmacli.commands.apply import apply
from dmacli.commands.build import build
from dmacli.commands.create import create
from dmacli.commands.debug import debug
from dmacli.commands.describe import describe
from dmacli.commands.run import run

@click.group()
def cli():
    pass

cli.add_command(apply)
cli.add_command(describe)
cli.add_command(create)
cli.add_command(debug)
cli.add_command(build)
cli.add_command(run)