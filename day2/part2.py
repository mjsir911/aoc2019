#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

from part1 import computer, prog

goal = 19690720

for i in range(99):
    for j in range(99):
        prog[1] = i
        prog[2] = j
        out = computer(prog[:])
        if out == goal:
            print(100 * i + j)
            break
