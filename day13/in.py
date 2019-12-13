#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

__appname__     = "in"
__author__      = "@AUTHOR@"
__copyright__   = ""
__credits__     = ["@AUTHOR@"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "@AUTHOR@"
__email__       = "@EMAIL@"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

from getch import getch
import time
import sys
while True:
    time.sleep(0.01)
    in_ = input()
    sys.stderr.write(in_)
    in_ = in_.strip()
    if in_ == ',':
        print('-1')
    elif in_ == '.':
        print('1')
    elif in_ == '':
        print('0')
    else:
        sys.stderr.write('invalid: ' + repr(in_))
