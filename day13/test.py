#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

__appname__     = "test"
__author__      = "@AUTHOR@"
__copyright__   = ""
__credits__     = ["@AUTHOR@"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "@AUTHOR@"
__email__       = "@EMAIL@"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

import sys
m = {}

def draw():
    for row in range(25):
        for col in range(40):
            print(m.get((col, row), ' '), end='')
        print()
    print(m.get('score', 0))

left = ','
right = '.'
stay = ' '
def think():
    xb = m['ball'][0]
    if 'paddle' not in m:
        sys.stderr.write(',\n')
        return
    xp = m['paddle'][0]
    print(xb, xp)
    if xb < xp:
        dir = left
    elif xb > xp:
        dir = right
    else:
        dir = stay
    print(f'b: {xb}, p: {xp}')
    sys.stderr.write(dir + '\n')

a = {0: ' ', 1: '|', 2: '#', 3: 'T', 4: 'O'}

i = 0
while True:
    i += 1
    x = int(input())
    y = int(input())
    id_ = int(input())
    if x == -1 and y == 0:
        m['score'] = id_
        continue

    m[(x, y)] = a[id_]
    if id_ == 3:
        m['paddle'] = (x, y)
    elif id_ == 4:
        m['ball'] = (x, y)
    draw()
    if id_ == 4:
        think()

# print(len([i for i in m.values() if i == '#']))
