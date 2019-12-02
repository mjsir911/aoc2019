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



prog = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,1,6,23,27,2,27,9,31,2,6,31,35,1,5,35,39,1,10,39,43,1,43,13,47,1,47,9,51,1,51,9,55,1,55,9,59,2,9,59,63,2,9,63,67,1,5,67,71,2,13,71,75,1,6,75,79,1,10,79,83,2,6,83,87,1,87,5,91,1,91,9,95,1,95,10,99,2,9,99,103,1,5,103,107,1,5,107,111,2,111,10,115,1,6,115,119,2,10,119,123,1,6,123,127,1,127,5,131,2,9,131,135,1,5,135,139,1,139,10,143,1,143,2,147,1,147,5,0,99,2,0,14,0"

prog = [int(op) for op in prog.split(",")]


def computer(reel):
    dispatch = {}
    dispatch[99] = lambda: print('end')
    dispatch[1] = lambda a, b, c: reel.__setitem__(c, reel[a] + reel[b])
    dispatch[2] = lambda a, b, c: reel.__setitem__(c, reel[a] * reel[b])
    for i in range(0, len(reel), 4):
        op = reel[i]
        if op == 99:
            return reel[0]
        arg1, arg2, arg3 = reel[i+1], reel[i+2], reel[i+3]
        dispatch[op](arg1, arg2, arg3)


prog[1] = 12
prog[2] = 2
out = computer(prog[:])
print(out)


goal = 19690720

import copy

for i in range(99):
    for j in range(99):
        prog[1] = i
        prog[2] = j
        out = computer(copy.copy(prog[:]))
        if out == goal:
            print(100 * i + j)
