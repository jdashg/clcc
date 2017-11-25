# python3
assert __name__ != '__main__'

import os

try:
    cl_path_path = os.path.join(os.path.dirname(__file__), '.cl-path.txt')
    with open(cl_path_path, 'r') as f:
        cl_path = f.readline()
except FileNotFoundError:
    print('Run `dump-path.bat` from the desired "Tools Command Prompt".')
    print('(You probably want "x64 Native Tools Command Prompt for VR 2017")')
    exit(1)

BIN_PATH = os.path.dirname(cl_path)

def path(bin_name):
    return os.path.join(BIN_PATH, bin_name)
