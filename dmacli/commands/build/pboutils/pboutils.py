from yapbol import PBOHeaderExtension
from functools import reduce

class PBOHeaderExtensionWrapper:
    headers = {}

    def __init__(self, extension: PBOHeaderExtension):
        self.extension = extension
        
        for i in range(0, len(self.extension.strings), 2):
            self.headers[self.extension.strings[i]] = self.extension.strings[i + 1]

    def __getitem__(self, key):
        return self.headers[key]

    def __setitem__(self, key, value):
        self.headers[key] = value

    def commit(self):
        self.extension.strings = list(reduce(lambda x, y: x + y, self.headers.items()))
