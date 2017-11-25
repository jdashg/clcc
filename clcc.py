# python3
assert __name__ != '__main__'

import os
import subprocess

try:
    cl_path_path = os.path.join(os.path.dirname(__file__), '.cl-path.txt')
    with open(cl_path_path, 'r') as f:
        INCLUDE = f.readline()
        LIB = f.readline()
        cl_path = f.readline()
except FileNotFoundError:
    print('Run `dump-path.bat` from the desired "Tools Command Prompt".')
    print('(You probably want "x64 Native Tools Command Prompt for VR 2017")')
    exit(1)


CL_ENV = dict(os.environ)
try:
    CL_ENV['INCLUDE'] += ';' + INCLUDE
except KeyError:
    CL_ENV['INCLUDE'] = INCLUDE

try:
    CL_ENV['LIB'] += ';' + LIB
except KeyError:
    CL_ENV['LIB'] = LIB

CL_DIR = os.path.dirname(cl_path)

def run(args):
    args[0] = os.path.join(CL_DIR, args[0])
    return subprocess.run(args, env=CL_ENV).returncode
