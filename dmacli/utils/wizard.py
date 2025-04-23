from abc import abstractmethod
import os
from dmacli.constants import MODIFICATION_DATA_PREFIX, ROOT_MODIFICATION_FILE
from dmacli.models.file import FileModel
from dmacli.templates.structures import CONFIGURATION_STRUCTURE, MODIFICATION_STRUCTURE
from dmacli.utils.utils import preformat


class Wizard:
    _prefix = None

    def __init__(self, path: str, name: str):
        self.path = path
        self.name = name
    
    @abstractmethod
    def create(self):
        os.makedirs(os.path.join(self.path, self.name), exist_ok=False)
        self._create_structure()

    def _create_structure(self):
        for key, value in self._initial_structure.items():
            self._create(key, value, os.path.join(self.path, self.name))
        
    def _create(self, key, value, path):
        if value['kind'] == 'folder':
            os.makedirs(os.path.join(path, key), exist_ok=False)
            for k, v in value['spec'].items():
                self._create(k, v, os.path.join(path, key))
        elif value['kind'] == 'file':
            self._create_file(value['spec'], path)
    
    def _create_file(self, value, path):
        file_context = FileModel(**value)
        with open(os.path.join(path, file_context.name), 'w') as file:
            template = preformat(file_context.context).format(
                MODIFICATION_NAME_PLACEHOLDER=self.name,
                MODIFICATION_PREFIX_PLACEHOLDER=self._prefix,
                ROOT_MODIFICATION_FILE=ROOT_MODIFICATION_FILE,
            )
            file.write(template)


class ModWizard(Wizard):
    
    def __init__(self, path: str, name: str):
        super().__init__(path, name)
        self._initial_structure = MODIFICATION_STRUCTURE

    def create(self):
        return super().create()


class ConfigWizard(Wizard):

    def __init__(self, path: str, name: str):
        super().__init__(path, name)
        self._initial_structure = CONFIGURATION_STRUCTURE

    def create(self):
        return super().create()


class DataWizard(ModWizard):

    def __init__(self, path: str, name: str):
        super().__init__(path, name)
        self._prefix = MODIFICATION_DATA_PREFIX

 
class ModuleWizard(ModWizard):
    
    def __init__(self, path: str, name: str):
        super().__init__(path, name)
        self._prefix = self.name
    
