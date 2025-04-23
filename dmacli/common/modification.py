import os
from pathlib import Path

from dmacli.constants import ROOT_MODIFICATION_FILE, ROOT_PREFIX_FILE


class Modification:
    _prefix = None
    _is_valid = False
    _path = None
    
    def __init__(self, path):
        self.path = path
        self._prefix = None
        self._is_valid = self._is_valid_modification()
        if self._is_valid_modification():
            self._is_valid = True
            self._prefix = self._get_prefix()

    def get_prefix(self):
        return self._prefix
    
    def get_path(self):
        return self.path
    
    def is_valid(self):
        return self._is_valid

    def _is_valid_modification(self):
        path_obj = Path(self.path)
        return \
            os.path.exists(path_obj / ROOT_PREFIX_FILE) and \
            os.path.exists(path_obj / ROOT_MODIFICATION_FILE)
    
    def _get_prefix(self):
        with open(Path(self.path) / ROOT_PREFIX_FILE, 'r') as file:
            return file.read().strip()