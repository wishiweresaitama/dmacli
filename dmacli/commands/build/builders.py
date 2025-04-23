"""Builder classes for different build types."""

# Standard library imports
import logging
import os
import shutil
from pathlib import Path

# Local imports
from dmacli.constants import ROOT_MODIFICATION_FILE
from dmacli.commands.build.strategies import BuilderStrategy, BinarizeStrategy
from dmacli.utils.utils import copy_directory
from dmacli.common.modification import Pack
class Builder:
    def __init__(
        self,
        builder_strategy: BuilderStrategy,
        binarize_strategy: BinarizeStrategy,
        source: Path,
        destination: Path,
        cache: bool,
    ):
        self.builder_strategy = builder_strategy
        self.binarize_strategy = binarize_strategy
        self.source = source.resolve()
        self.destination = destination.resolve()
        self.cache = cache

    def build(self):
        logging.info(f'Preparing build...')
        self._pre_build()

        logging.info(f'Building module {self.source} to {self.destination}...')
        self._build()

        logging.info('Post-build actions...')
        self._post_build()

        logging.info('Build completed successfully')

    def _pre_build(self):
        pass

    def _build(self):
        pass

    def _post_build(self):
        pass


class ModificationBuilder(Builder):
    def _pre_build(self):
        os.makedirs(self.destination, exist_ok=True)
        with open(os.path.join(self.source, '.prefix'), 'r') as file:
            self.prefix = file.read()

    def _build(self):
        copy = copy_directory(self.source)
        self.binarize_strategy.binarize(self.source, copy)
        self.builder_strategy.build(copy, self.destination, self.source.name, self.prefix, self.cache)

    def _post_build(self):
        shutil.copyfile(
            Path(self.source, ROOT_MODIFICATION_FILE),
            Path(self.destination, 'mod.cpp'),
        )

class PackBuilder(Builder):
    def _pre_build(self):
        self.pack = Pack(self.source)

    def _build(self):
        for modification in self.pack.get_modifications():
            logging.info(f'Building modification {modification.get_path()}...')

            # relative_path = modification.get_path().relative_to(self.source)
            # destination = self.destination / relative_path

            copy = copy_directory(modification.get_path())
            self.binarize_strategy.binarize(modification.get_path(), copy)
            self.builder_strategy.build(copy, self.destination, modification.get_name(), modification.get_prefix(), self.cache)
    
    def _post_build(self):
        ...
