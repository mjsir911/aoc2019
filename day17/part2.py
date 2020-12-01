#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

from sys import stderr
from time import sleep

from part1 import m, draw

draw()

dmap = {'V': (0, 1), '>': (1, 0), '<': (-1, 0), '^': (0, -1)}

start = [c for (c, v) in m.items() if v in '^<>V'][0]
print(start)

left = {'^': '<', '<': 'V', 'V': '>', '>': '^'}
right = {'^': '>', '>': 'V', 'V': '<', '<': '^'}

def add_cord(a, b):
    return a[0] + b[0], a[1] + b[1]

insts = []
def next_dir(d, c, m):
    print(f'd: {d}, c: {c}', file=stderr)
    forwards = add_cord(c, dmap[d])
    l = add_cord(c, dmap[left[d]])
    r = add_cord(c, dmap[right[d]])
    print('oldpos: ', c, file=stderr)
    if m.get(forwards, '.') == '#':
        newdir, newpos = d, forwards
    elif m.get(l, '.') == '#':
        insts.append('L')
        newdir, newpos = left[d], l
    elif m.get(r, '.') == '#':
        insts.append('R')
        newdir, newpos = right[d], r
    print('newpos: ', newpos, file=stderr)
    insts.append('s')

    m[c] = '#'
    m[newpos] = newdir

    return newdir, newpos



d = m[start]
c = start

import time
while True:
    try:
        d, c = next_dir(d, c, m)
    except:
        break
    draw(); sleep(0.05)

def compress_p1(insts):
    ret = []
    for i in insts:
        if i == 's':
            if isinstance(ret[-1], int):
                ret[-1] += 1
            else:
                ret.append(1)
        else:
            ret.append(i)

    return [str(i) for i in ret]

print(','.join(compress_p1(insts)))

