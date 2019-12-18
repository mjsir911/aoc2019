#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

from subprocess import Popen, PIPE

app = Popen("./a.out", stdout=PIPE, stdin=PIPE)

m = {}
def draw():
    for row in range(0, 50):
        for col in range(0, 60):
            print(m.get((col, row), '.'), end='')
        print()

if 1:
    x = 0
    y = 0
    for line, _ in zip(app.stdout, range(2745)):
        c = chr(int(line.decode().strip()))
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

def find_intersects():
    for c in m.keys():
        if m.get((c[0], c[1]), '.') == '#':
            if m.get((c[0], c[1]+1), '.') == '#':
                if m.get((c[0], c[1]-1), '.') == '#':
                    if m.get((c[0]+1, c[1]), '.') == '#':
                        if m.get((c[0]-1, c[1]), '.') == '#':
                            yield c


s = list(find_intersects())
for i in s:
    m[i] = 'O'
draw()
# print([(c) for c in s])
print(s)
print([c[0] * c[1] for c in s])
print(sum([c[0] * c[1] for c in s]))

