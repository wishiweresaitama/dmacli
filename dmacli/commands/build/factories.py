from pathlib import Path

from dmacli.commands.build.builders import Builder, ModificationBuilder, PackBuilder
from dmacli.commands.build.strategies import FPackerBuilderStrategy, AddonBuilderStrategy, PboPackerBuilderStrategy


class BuilderFactory:
    def get_builder(self, builder_type: str, source: Path, destination: Path, cache: bool) -> Builder:
        ...


class ModificationBuilderFactory:
    def get_builder(self, builder_type: str, source: Path, destination: Path, cache: bool) -> Builder:
        if builder_type == 'fpacker':
            return ModificationBuilder(FPackerBuilderStrategy(), source, destination, cache)
        elif builder_type == 'addonbuilder':
            return ModificationBuilder(AddonBuilderStrategy(), source, destination, cache)
        elif builder_type == 'pbopacker':
            return ModificationBuilder(PboPackerBuilderStrategy(), source, destination, cache)
        else:
            raise ValueError(f'Invalid builder type: {builder_type}')


class PackBuilderFactory:
    def get_builder(self, builder_type: str, source: Path, destination: Path, cache: bool) -> Builder:
        if builder_type == 'fpacker':
            return PackBuilder(FPackerBuilderStrategy(), source, destination, cache)
        elif builder_type == 'addonbuilder':
            return PackBuilder(AddonBuilderStrategy(), source, destination, cache)
        elif builder_type == 'pbopacker':
            return PackBuilder(PboPackerBuilderStrategy(), source, destination, cache)
        else:
            raise ValueError(f'Invalid builder type: {builder_type}')
