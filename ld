#!/usr/bin/env python3
assert __name__ == '__main__'

import clcc
import sys

args = ('link', sys.argv[1:])
clcc.shim_and_exit(args)
