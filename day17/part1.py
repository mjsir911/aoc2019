#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

from subprocess import Popen, PIPE

app = Popen("./computer | ./decode.awk", shell=True, stdout=PIPE, pass_fds=[4], text=True)

m = {}

def draw():
    for row in range(0, 50):
        for col in range(0, 60):
            print(m.get((col, row), '.'), end='')
        print()


if 1:
    maze = app.stdout
else:
    from io import StringIO
    maze = StringIO("""
..#.........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^..'
""")

for y, line in enumerate(maze):
    line = line.strip()
    for x, char in enumerate(line):
        m[x, y] = char

def find_intersects():
    for c in m.keys():
        if m.get((c[0], c[1]), '.') == '#':
            if m.get((c[0], c[1]+1), '.') == '#':
                if m.get((c[0], c[1]-1), '.') == '#':
                    if m.get((c[0]+1, c[1]), '.') == '#':
                        if m.get((c[0]-1, c[1]), '.') == '#':
                            yield c


if __name__ == '__main__':
    s = list(find_intersects())
    for i in s:
        m[i] = 'O'
    draw()
    # print([(c) for c in s])
    # print(s)
    # print([c[0] * c[1] for c in s])
    print(sum([c[0] * c[1] for c in s]))
