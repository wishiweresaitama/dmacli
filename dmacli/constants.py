from os import getenv


CONFIGURATION_NAME = 'config.json'
CONFIGURATION_DIR = '.dmacli'

MODIFICATION_NAME_PLACEHOLDER = 'ModificationNamePlaceholder'
MODIFICATION_DATA_PREFIX = getenv('MODIFICATION_DATA_PREFIX', 'Resources')

WORKBENCH_RELATIVE_PATH = 'Bin/Workbench/workbenchApp.exe'
BUILDER_RELATIVE_PATH = 'Bin/AddonBuilder/AddonBuilder.exe'

DAYZ_DIRECTORY_STRUCTURE = {
    'folders': [
        'Addons', 'bliss', 'dta', 'sakhal'
    ],
    'files': [
        'amd_ags_x64.dll',
        'CrashReporter.exe',
        'dayz.gproj',
        'steam_api64.dll',
        'steam_appid.txt',
    ],
    'special': [
        'mpmissions',
    ]
}