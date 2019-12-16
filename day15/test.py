#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
import random
import json
import pickle
import time

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


data = {}
pos = (0, 0)

wall = object()

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
            if (col, row) == pos:
                sys.stderr.write('x')
            elif data.get((col, row)) == 'oxygen':
                sys.stderr.write('o')
            elif data.get((col, row)) == 'space':
                sys.stderr.write(' ')
            elif data.get((col, row)) == 'wall':
                sys.stderr.write('#')
            else:
                sys.stderr.write(' ')
        sys.stderr.write('\n')

movcounter = 0

def move(dir):
    global pos, movcounter
    movcounter += 1
    if data.get(addcoord(pos, dir)) == 'wall':
        # return early because won't work
        return None
    print(dir)
    inp = int(input().strip())
    if inp == 0:
        data[addcoord(pos, dir)] = 'wall'
    elif inp == 1:
        pos = addcoord(pos, dir)
        data[pos] = 'space'
    elif inp == 2:
        pos = addcoord(pos, dir)
        data[pos] = 'oxygen'
    return inp

import sys
dmap = {'d': 2, 'u': 1, 'l': 3, 'r': 4}
# while True:
# for dir in 'drdldldlulurdrululdldlurdrdrururdrurdrururdldldrdldlruldluruLurulurululdluldluldldldrdrdluldluldlululu':
#     if dir == 'L':
#         move(3)
#         move(3)
#         draw()
#         sys.stderr.write(repr(pos))
#         sys.stderr.write('\n')
#         continue
#     dir = dmap[dir]
#     while True:
#     # for _ in range(random.randint(1, 4)):
#         s = move(dir)
#         if s == 0:
#             break
#         if s == 2:
#             sys.stderr.write(repr(movcounter))
#             sys.stderr.write("\n")
#             sys.stderr.write(repr(pos))
#             sys.stderr.write("\n")
#             exit()
#             with open('data.json', 'wb') as f:
#                 pickle.dump(data, f)
#         sys.stderr.write(repr(pos))
#         sys.stderr.write('\n')
#         draw()

with open('data.json', 'rb') as f:
    data = pickle.load(f)
if False:
    try:
        i = 0
        while True:
            i += 1
            dir = random.choice([1, 2, 3, 4])
            move(dir)
            if i % 100 == 0:
                draw()
    finally:
        with open('data.json', 'wb') as f:
            pickle.dump(data, f)
else:
    for dir in 'drdldldlulurdrululdldlurdrdrururdrurdrururdldldrdldrdldrdluldldldrdldrulurdluLdlurululdluldrurdluldlururuld':
        if dir == 'L':
            move(3)
            move(3)
            continue
        dir = dmap[dir]
        before = pos
        while move(dir) == 1:
            draw()
        if pos == before:
            sys.stderr.write('bad\n')
            exit()



draw()
# sys.stderr.write('\n')
sys.stderr.write(repr(movcounter))
sys.stderr.write('\n')
# sys.stderr.write('\n')
# sys.stderr.write('\n')
# sys.stderr.write(repr(data))
