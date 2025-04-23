"""Builder classes for different build types."""

# Standard library imports
import logging
import os
import shutil
import tempfile
import subprocess
from pathlib import Path

# Local imports
from dmacli.constants import ROOT_MODIFICATION_FILE, BINARIZE_RELATIVE_PATH
from dmacli.commands.build.strategies import BuilderStrategy
from dmacli.configuration import Configuration

class Builder:
    def __init__(self, strategy: BuilderStrategy, source: Path, destination: Path, cache: bool):
        self.strategy = strategy
        self.source = source
        self.destination = destination
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

    def _copy_modification(self):
        with tempfile.TemporaryDirectory(delete=False) as temp_dir:
            self.modification_path = Path(temp_dir, self.source.name)
            shutil.copytree(
                self.source,
                self.modification_path,
                dirs_exist_ok=True,
            )

    def _binarize_modification(self):
        binarize_path = Path(Configuration().get().toolsPath, BINARIZE_RELATIVE_PATH)
        subprocess.run(
            [
                binarize_path,
                '-noLogs',
                '-targetBonesInterval=56',
                '-maxProcesses=16',
                '-always',
                '-silent',
                f'-addon={self.modification_path.parent}',
                f'-textures={self.modification_path}',
                f'-binpath={binarize_path.parent}',
                self.source,
                self.modification_path,
            ],
            cwd=binarize_path.parent,
            shell=True,
        ).check_returncode()

        subprocess.run(
            [
                binarize_path,
                '-texheaders',
                '-maxProcesses=16',
                '-silent',
                self.modification_path,
                self.modification_path,
            ],
            cwd=binarize_path.parent,
            shell=True,
        ).check_returncode()


class ModificationBuilder(Builder):
    def _pre_build(self):
        os.makedirs(self.destination, exist_ok=True)
        with open(os.path.join(self.source, '.prefix'), 'r') as file:
            self.prefix = file.read()
        
        self._copy_modification()
        self._binarize_modification()

    def _build(self):
        self.strategy.build(self.modification_path, self.destination, self.prefix, self.cache)

    def _post_build(self):
        shutil.copyfile(
            Path(self.source, ROOT_MODIFICATION_FILE),
            Path(self.destination, 'mod.cpp'),
        )

class PackBuilder(Builder):
    def _post_build(self):
        ...
