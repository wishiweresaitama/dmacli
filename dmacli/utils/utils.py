import os
import _winapi
import shutil
import subprocess
import hashlib as hl
import time


def preformat(msg):
    """ allow {{key}} to be used for formatting in text
    that already uses curly braces.  First switch this into
    something else, replace curlies with double curlies, and then
    switch back to regular braces
    """
    msg = msg.replace('{{', '<<<').replace('}}', '>>>')
    msg = msg.replace('{', '{{').replace('}', '}}')
    msg = msg.replace('<<<', '{').replace('>>>', '}')
    return msg


def prepare_mods(mods: list, serverside=False) -> str:
    arg_string = '"-mod=' if serverside is False else '"-servermod='
    for mod in mods:
        arg_string = arg_string + mod + ";"
    arg_string += '"'
    return arg_string


def prepare_profile(path) -> str:
    arg_string = '-profiles=' + path
    return arg_string


def create_junction(source, destignation):
    try:
        _winapi.CreateJunction(
            os.path.normpath(source),
            os.path.normpath(destignation),
        )
    except FileExistsError:
        return False
    return True


def delete_junction(source):
    try:
        os.remove(os.path.normpath(source))
    except FileNotFoundError:
        return False
    return True


def execute_process(path, process_name, args: list):
    kill_process(process_name).wait()
    args_string = ""
    for arg in args:
        args_string += f"{arg} "
    return subprocess.Popen(f"{process_name} {args_string}", shell=True, cwd=path)


def kill_process(process_name):
    return subprocess.Popen(
        f'tasklist | find /i "{process_name}">nul && Taskkill /F /IM  "{process_name}"',
        shell=True,
    )

def compare_checksum(a, b):
    try:
        checksum_a = hl.md5(open(a, 'rb').read()).hexdigest()
        checksum_b = hl.md5(open(b, 'rb').read()).hexdigest()    
        return checksum_a == checksum_b
    except FileNotFoundError:
        return False

def syncronize_files(source : os.path, destination : os.path):
    if not compare_checksum(source, destination):
        print(f'Checksum mismatch between {source} and {destination}, copying...')
        shutil.copyfile(source, destination)
        print(f'Done copying {source} to {destination}')

def run_interrupt_listener():
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print('Execution interrupted, exiting...')
            break