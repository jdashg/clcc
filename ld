#!/usr/bin/env python3
assert __name__ == '__main__'

import clcc

import subprocess
import sys


args = [clcc.path('link')]
for x in sys.argv[1:]:
    args.append(x)

exit(subprocess.run(args).returncode)
