import os

import keyboard
import threading

import time
from datetime import datetime

from dmacli.configuration import Configuration
from dmacli.dayz.input_handler import InputHandler
from dmacli.dayz.log_reader import LogReader
from dmacli.utils.utils import execute_process, kill_process, prepare_mods, prepare_profile

class DayzRunner(InputHandler):
    _configuration = None
    _state = None

    def __init__(self, configuration : Configuration):
        super().__init__()

        self._configuration = configuration

        keyboard.add_hotkey('ctrl+alt+home', self._on_start)
        keyboard.add_hotkey('ctrl+alt+end', self._on_stop)

        self._state = StoppedState(self)

    def _on_start(self):
        self._configuration.refresh()
        self._state.run()

    def _on_stop(self):
        self._state.stop()

    def change_state(self, state):
        self._state = state
        print(f'{self.__class__.__name__} state changed to {state.__class__.__name__}')

    def get_executable(self) -> str:
        raise NotImplemented

    def get_executable_args(self) -> list:
        raise NotImplemented
    
    def get_game_path(self) -> str:
        return self._configuration.get().gamePath
    
    def get_label(self) -> str:
        raise NotImplemented
    
    def get_log_folder(self) -> os.path:
        raise NotImplemented
    
    def destroy(self):
        self._on_stop()


class ServerDayzRunner(DayzRunner):
    
    def __init__(self, configuration):
        super().__init__(configuration)

        keyboard.add_hotkey('alt+s+home', self._on_start)
        keyboard.add_hotkey('alt+s+end', self._on_stop)

    def get_executable(self) -> str:
        return self._configuration.get().serverExecuteFile

    def get_executable_args(self) -> list:
        args = self._configuration.get().serverArgs.copy()
        args.append(prepare_mods(self._configuration.get().serverMods, serverside = True))
        args.append(prepare_mods(self._configuration.get().mods))
        args.append(prepare_profile(self._configuration.get().serverProfile))
        return args
    
    def get_label(self) -> str:
        return 'Server'
    
    def get_log_folder(self):
        return os.path.join(
            self._configuration.get().gamePath,
            self._configuration.get().serverProfile,
        )


class ClientDayzRunner(DayzRunner):
    
    def __init__(self, configuration):
        super().__init__(configuration)

        keyboard.add_hotkey('alt+c+home', self._on_start)
        keyboard.add_hotkey('alt+c+end', self._on_stop)

    def get_executable(self):
        return self._configuration.get().clientExecuteFile
    
    def get_executable_args(self):
        args = self._configuration.get().clientArgs.copy()
        args.append(prepare_mods(self._configuration.get().mods))
        args.append(prepare_profile(self._configuration.get().clientProfile))
        return args
    
    def get_label(self) -> str:
        return 'Client'
    
    def get_log_folder(self):
        return os.path.join(
            self._configuration.get().gamePath,
            self._configuration.get().clientProfile,
        )


class State:
    _runner = None

    def __init__(self, runner):
        self._runner = runner

    def run():
        pass

    def stop():
        pass

class RunningState(State):

    _log_file = None
    _running = False
    _search = None

    def __init__(self, runner):
        super().__init__(runner)

        self._running = True
        self._search = threading.Thread(target=self._search_log)
        self._search.start()


    def run(self):
        pass

    def stop(self):
        kill_process(self._runner.get_executable())

        self._running = False
        self._search.join()

        LogReader().pop_log(self._log_file)

        self._runner.change_state(StoppedState(self._runner))

    def _search_log(self):
        launch_time = datetime.now()
        folder = self._runner.get_log_folder()

        while self._running:
            latest_log = max(
                [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".log")],
                key=os.path.getctime,
            )

            if os.path.getctime(latest_log) > launch_time.timestamp():
                self._log_file = open(latest_log, 'r')
                LogReader().push_log(self._log_file, self._runner.get_label())
                break
            
            time.sleep(0.5)


class StoppedState(State):
    def run(self):
        execute_process(
            self._runner.get_game_path(),
            self._runner.get_executable(),
            self._runner.get_executable_args(),
        )

        self._runner.change_state(RunningState(self._runner))

    def stop(self):
        pass
