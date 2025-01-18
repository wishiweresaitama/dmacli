import click

from dmacli.utils.wizard import ModuleWizard


@click.command()
@click.argument('path', type=click.Path(exists=True), required=True)
@click.option('-n', '--name', help='Name of the module', required=True)
def module(path, name):
    ModuleWizard(path, name).create()