#!/usr/bin/env python3
assert __name__ == '__main__'

import clcc
import sys

args = ['cl', '-nologo']
for x in sys.argv[1:]:
    if x == '-H':
        args.append('-showIncludes')
        continue

    args.append(x)

clcc.shim_and_exit(args)
