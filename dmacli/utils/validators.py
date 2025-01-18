import os
import _winapi
import shutil

from dmacli.configuration import Configuration
from dmacli.constants import DAYZ_DIRECTORY_STRUCTURE
from dmacli.utils.utils import syncronize_files


def validate_build(configuration: Configuration):
    if not os.path.exists(configuration.get().gamePath):
        os.makedirs(configuration.get().gamePath)
    
    for folder in DAYZ_DIRECTORY_STRUCTURE['folders']:
        try:
            _winapi.CreateJunction(
                os.path.normpath(os.path.join(configuration.get().originPath, folder)),
                os.path.normpath(os.path.join(configuration.get().gamePath, folder)),
            )
        except FileExistsError:
            pass
    
    for file in DAYZ_DIRECTORY_STRUCTURE['files']:
        try:
            source = open(os.path.join(configuration.get().originPath, file), 'rb')
        except FileNotFoundError:
            print(f'File {file} not found in {configuration.get().originPath}')
            continue
        
        syncronize_files(
            os.path.join(configuration.get().originPath, file),
            os.path.join(configuration.get().gamePath, file),
        )
    
    for special in DAYZ_DIRECTORY_STRUCTURE['special']:
        if not os.path.exists(os.path.join(configuration.get().gamePath, special)):
            shutil.copytree(
                os.path.join(configuration.get().originPath, special),
                os.path.join(configuration.get().gamePath, special),
            )


def validate_checksum(configuration: Configuration):
    syncronize_files(
        os.path.join(configuration.get().originPath, configuration.get().executeFile),
        os.path.join(configuration.get().gamePath, configuration.get().serverExecuteFile),
    )

    syncronize_files(
        os.path.join(configuration.get().originPath, configuration.get().executeFile),
        os.path.join(configuration.get().gamePath, configuration.get().clientExecuteFile),
    )