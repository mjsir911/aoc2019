#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

prog = [int(op) for op in input().split(",")]

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


if __name__ == '__main__':
    prog[1] = 12
    prog[2] = 2
    out = computer(prog[:])
    print(out)


