import click

from dmacli.configuration import Configuration


@click.command()
def config():
    print(Configuration().dump())