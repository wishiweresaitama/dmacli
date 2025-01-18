import os
import sys
import click

from dmacli.configuration import Configuration
from dmacli.dayz.dayz_runner import ClientDayzRunner, ServerDayzRunner
from dmacli.utils.utils import run_interrupt_listener
from dmacli.utils.validators import validate_build, validate_checksum

@click.command()
def run():
    config = Configuration()

    validate_build(config)
    validate_checksum(config)

    server = ServerDayzRunner(config)
    client = ClientDayzRunner(config)

    run_interrupt_listener()

    server.destroy()
    client.destroy()