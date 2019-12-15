#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
import pickle
import time

__appname__     = "part2"
__author__      = "@AUTHOR@"
__copyright__   = ""
__credits__     = ["@AUTHOR@"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "@AUTHOR@"
__email__       = "@EMAIL@"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

def addcoord(p, d):
    if d == 1:  # north
        return p[0], p[1] - 1
    elif d == 2:  # south
        return p[0], p[1] + 1
    elif d == 3:  # west
        return p[0] - 1, p[1]
    elif d == 4:  # east
        return p[0] + 1, p[1]
    print('invalid: ', d)

import sys
def draw():
    time.sleep(0.015)
    for row in range(-25, 20):
        for col in range(-25, 25):
            # if (col, row) == (0, 0):
                # sys.stderr.write('x')
            if data.get((col, row)) == 'oxygen':
                sys.stderr.write('o')
            elif data.get((col, row)) == 'space':
                sys.stderr.write(' ')
            elif data.get((col, row)) == 'wall':
                sys.stderr.write('#')
            else:
                sys.stderr.write(' ')
        sys.stderr.write('\n')

def near(coord):
    return [addcoord(coord, d) for d in [1, 2, 3, 4]]

def tick():
    oxygen = [k for (k, v) in data.items() if v == 'oxygen']
    nearby = [some for cell in oxygen for some in near(cell) if data[some] == 'space']
    for n in nearby:
        data[n] = 'oxygen'

with open('data.json', 'rb') as f:
    data = pickle.load(f)


count = 0
while True:
    count += 1
    draw()
    tick()
    if not [k for (k, v) in data.items() if v == 'space']:
        break
print(count)
