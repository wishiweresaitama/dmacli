"""Build command module for dmacli."""

import click
from pathlib import Path
from dmacli.commands.build.factories import ModificationBuilderFactory, PackBuilderFactory

@click.command()
@click.option(
    "-s",
    "--source",
    help="Source directory",
    type=click.Path(exists=True, dir_okay=True),
    required=True,
)
@click.option(
    "-d",
    "--destination",
    help="Destination directory",
    type=click.Path(dir_okay=True),
    required=True,
)
@click.option(
    "-b",
    "--builder",
    help="Builder to use",
    type=click.Choice(["fpacker", "addonbuilder", "pbopacker"]),
    default="addonbuilder",
    required=True,
)
@click.option(
    "--pack/--no-pack",
    default=False,
    help="Build as modification or pack",
)
@click.option("--cache/--no-cache", default=False, help="Use cached data")
def build(
    source: click.Path,
    destination: click.Path,
    builder: str,
    cache: bool,
    pack: bool,
) -> None:
    """Build the project using the specified builder.

    Args:
        source: Source directory path
        destination: Destination directory path
        builder: Builder to use (fpacker / addonbuilder / pbopacker)
        cache: Whether to use cached data
    """
    builder_factory = PackBuilderFactory() if pack else ModificationBuilderFactory()
    builder = builder_factory.get_builder(builder, Path(source), Path(destination), cache)
    builder.build()
