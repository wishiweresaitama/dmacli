import click

from dmacli.commands.create.resource import resource
from dmacli.commands.create.module import module
from dmacli.commands.create.submodule import submodule

@click.group()
def create():
    pass

create.add_command(module)
create.add_command(submodule)
create.add_command(resource)