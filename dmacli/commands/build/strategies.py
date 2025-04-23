"""Builder strategies for different build methods."""

# Standard library imports
import base64
import os
import subprocess
import tempfile
from pathlib import Path

# Local imports
from yapbol import PBOFile
from dmacli.commands.build.pboutils.pboutils import PBOHeaderExtensionWrapper
from dmacli.configuration import Configuration
from dmacli.constants import (
    ADDON_BUILDER_RELATIVE_PATH,
    BUILDER_INCLUDE_FILES,
    CPP_TO_BIN_RELATIVE_PATH,
    ROOT_MODIFICATION_FILE,
)


class BuilderStrategy:
    def build(self, source: Path, destination: Path, prefix: str, cache: bool):
        ...


class AddonBuilderStrategy(BuilderStrategy):
    def build(self, source: Path, destination: Path, prefix: str, cache: bool):
        executable = Path(Configuration().get().toolsPath, ADDON_BUILDER_RELATIVE_PATH)
        source_encoded = base64.b64encode(str(source).encode()).decode()

        wildcard_path = Path(tempfile.gettempdir(), 'include.wildcard.txt')

        with open(wildcard_path, 'w') as file:
            file.write(','.join(BUILDER_INCLUDE_FILES))

        subprocess.run(
            [
                executable.name,
                source,
                Path(destination, 'addons'),
                f'-toolsDirectory={Path(Configuration().get().toolsPath)}',
                f'-prefix={prefix}',
                f'-temp={Path(tempfile.gettempdir(), source_encoded)}',
                f'-include={wildcard_path}',
                '-clear' if not cache else '',
                f'-packonly', # workaround issue https://feedback.bistudio.com/T188609
            ],
            cwd=executable.parent,
            shell=True,
        ).check_returncode()


class FPackerBuilderStrategy(BuilderStrategy):
    def build(self, source: Path, destination: Path, prefix: str, cache: bool):
        executable = 'FPackerEx.exe'
        subprocess.run(
            [
                executable,
                source,
                '-o',
                Path(destination, 'addons'),
                '-b',
                Path(Configuration().get().toolsPath, CPP_TO_BIN_RELATIVE_PATH),
                '--compress',
                'False'
            ],
            shell=True,
        ).check_returncode()

        pbo = PBOFile.read_file(Path(destination, 'addons', f'{destination.name}.pbo'))

        pbo_headers = PBOHeaderExtensionWrapper(pbo.pbo_header.header_extension)
        pbo_headers['prefix'] = prefix
        pbo_headers.commit()

        pbo.save_file(Path(destination, 'addons', f'{destination.name}.pbo'))


class PboPackerBuilderStrategy(BuilderStrategy):
    def build(self, source: Path, destination: Path, prefix: str, cache: bool):
        ...
