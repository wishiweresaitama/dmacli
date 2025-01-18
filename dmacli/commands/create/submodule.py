import click

from dmacli.utils.wizard import ConfigWizard


@click.command()
@click.argument('path', type=click.Path(exists=True), required=True)
@click.option('-n', '--name', help='Name of the module', required=True)
def submodule(path, name):
    ConfigWizard(path, name).create()