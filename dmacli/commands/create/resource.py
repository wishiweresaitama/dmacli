import click

from dmacli.utils.wizard import DataWizard


@click.command()
@click.argument('path', type=click.Path(exists=True), required=True)
@click.option('-n', '--name', help='Name of the module', required=True)
def resource(path, name):
    DataWizard(path, name).create()