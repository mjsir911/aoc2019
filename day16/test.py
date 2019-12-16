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

import itertools

def phase(l, i):
    indexes = [n for b in range(i) for n in range((i+b-1), len(l), (i * 4))]
    r1 = sum(l[n] for n in indexes)
    r2 = sum(l[n+(2*i)] for n in indexes if n+(2*i) < len(l))
    return abs(r1 - r2) % 10
    # return abs(sum([(n * m) for (n, m) in zip(l, test)])) % 10

base = [0, 1, 0, -1]
def phase2(l):
    for i, t in enumerate(l):
        yield phase(l, i+1)

# print(list(mul_iter(base, 2))[1:])
# print(phase([9, 8, 7, 6, 5], [1, 2, 3]))

# s = [int(x) for x in '12345678']
# s = [int(x) for x in input()]
inp = "03036732577212944063491565474664"
n = int(inp[:7])
# inp = input()
s = tuple(int(x) for x in inp)
s = s * 10000


def get_slices_pos(i, nl):
    return [slice(i+b-1,b+i+i-1) for b in range(0, nl, i * 4)]


def get_slices_neg(i, nl):
    return [slice(i+b-1,b+i+i-1) for b in range(i*2, nl, i * 4)]


def apply_slices(l, sl):
    return [x for s in sl for x in l[s]]


def apply_indices(n, sl):
    return [x for s in sl for x in range(*s.indices(n))]


import functools
@functools.lru_cache(100000000)
def doit(l, n, level=0):
    print(n, level)
    if level == 100:
        return s[n]
    pos = get_slices_pos(n, len(l))
    neg = get_slices_neg(n, len(l))
    posi = list(reversed(apply_indices(len(l), pos)))
    negi = list(reversed(apply_indices(len(l), neg)))
    return (sum(doit(l, pi, level=level+1) for pi in posi) - sum(doit(l, ni, level=level+1) for ni in negi)) % 10

def phase(l, i):
    return sum(l[i:]) % 10

def phase3(l, r):
    return (0,) * r + tuple(phase(l, i+1) for _, i in zip(l[r:], range(r,r*2)))

def phase2(l):
    return tuple(phase(l, i) for i in range(len(l)))


for _ in range(101):
    print(s[303673:303673+8], len(s))
    s = phase3(s, 303673)
