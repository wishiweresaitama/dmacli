import os
import threading
import time

from datetime import datetime
from dmacli.utils.singleton import Singleton

class LogReader(metaclass=Singleton):
    _files = set()
    _labels = {}
    _lock = threading.Lock()

    def __init__(self):
        _logger_reader = threading.Thread(target=self._reader)
        _logger_reader.start()

    def push_log(self, log_file, label):
        with self._lock:
            try:
                self._files.add(log_file)
                self._labels[log_file] = label
            except KeyError:
                pass

    def pop_log(self, log_file):
        with self._lock:
            try:
                self._files.remove(log_file)
                self._labels.pop(log_file)
            except KeyError:
                pass

    def _reader(self):
        while(True):
            with self._lock:
                for file in self._files:
                    self._print_log(file)
            time.sleep(1)

    def _print_log(self, file):
        while True:
            line = file.readline()
            if not line:
                break

            prefix = f'{datetime.now().strftime("%H:%M:%S")} {self._labels[file]}'
            print(
                f"[{prefix}]: {bytearray(line, 'cp1251').decode('utf-8')}",
                end="",
            )
