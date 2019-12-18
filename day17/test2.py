#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

from subprocess import Popen, PIPE

# app = Popen("./a.out", bufsize=3, stdout=PIPE, stdin=PIPE)
# appin, appout = app.stdin, app.stdout

import sys
appout, appin = sys.stdin, sys.stdout
oldprint = print
def print(*args, **kwargs):
    import sys
    return oldprint(*args, file=sys.stderr, **kwargs)

m = {}
def draw():
    for row in range(0, 50):
        for col in range(0, 60):
            print(m.get((col, row), '.'), end='')
        print()

if 1:
    x = 0
    y = 0
    for line, _ in zip(appout, range(2745)):
        c = chr(int(line.strip()))
        if c == '\n':
            y += 1
            x = 0
        else:
            m[(x, y)] = c
            x += 1
else:
    test_in = \
"""..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^..'"""


    for y, line in enumerate(test_in.split()):
        for x, c in enumerate(line):
            m[(x, y)] = c

# draw()
# # print([(c) for c in s])
# print(s)
# print([c[0] * c[1] for c in s])
# print(sum([c[0] * c[1] for c in s]))
import time


def mywrite(s):
    ret = b'\n'.join(str(ord(c)).encode() for c in s) + b'\n'
    print('writing: ', repr(ret))
    return ret

def mydecode(b):
    t = b.decode().strip().split()
    return ''.join(chr(int(i)) for i in t)

def myread(in_):
    import os
    import select
    import time
    b = b''
    while True:
        r, w, e = select.select([ in_ ], [], [], 0)
        if in_ in r:
            b += os.read(in_.fileno(), 50)
        else:
            break
    return mydecode(b)

def non_block_read(output):
    import fcntl
    import os
    fd = output.fileno()
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
    try:
        return output.read()
    except:
        return ""

def myread():
    import select
    while True:
        r, w, e = select.select([appout], [], [], 0.05)
        if r:
            a = r[0].readline()
            for i in a.split():
                i = int(i)
                if i > 130:
                    print(i)
                else:
                    print(chr(i), end='')
        else:
            break


import pickle
pickle.dump(m, open("data.pickle", 'wb'))
def mywrite(s):
    for c in s:
        appin.write(str(ord(c)))
        appin.write("\n")
    appin.write(str(ord("\n")))
    appin.write("\n")


draw()
exit()
myread()
mywrite("A,B,A,C,B,A,C,A,C,B")
myread()

mywrite("L,12,L,8,L,8")
myread()

mywrite("L,12,R,4,L,12,R,6")
myread()

mywrite("R,4,L,12,L,12,R,6")
myread()

mywrite(["y"])
while True:
    import time
    myread()
# print(app.stdout.read(2))
exit()
print('resp: ', myread(app.stdout))
app.stdin.write(mywrite('L,12\n'))
print('resp: ', myread(app.stdout))
app.stdin.write(mywrite('L,12\n'))
print('resp: ', myread(app.stdout))
app.stdin.write(mywrite('L,12\n'))
print('resp: ', myread(app.stdout))
app.stdin.write(mywrite('y\n'))
print('resp: ', myread(app.stdout))
for line in app.stdout:
    print('hi', line)
    continue

    for _ in range(2765):
        x = 0
        y = 0
        c = chr(int(line.decode().strip()))
        if c == '\n':
            y += 1
            x = 0
        else:
            m[(x, y)] = c
            x += 1
    draw()
