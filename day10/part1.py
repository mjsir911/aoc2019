#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :


import sys

def domap():
    return list(filter(bool, sum([
        list(map(lambda i: (i[0], y) if i[1] == '#' else (), enumerate(line)))
        for (y, line) in enumerate(sys.stdin)], [])))


def gcd(a, b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def whatever(v):
    """
    reduces vector down into smallest possible integer jumps
    """

    g = abs(gcd(v[0], v[1]))
    return v[0] // g, v[1] // g

def relative_to(origin, p):
    return p[0] - origin[0], p[1] - origin[1]


def path(from_, to):
    smol_step = whatever(relative_to(from_, end))
    a = []
    while to not in a:
        from_ = (smol_step[0] + from_[0], smol_step[1] + from_[1])
        a.append(from_)
    return a



asteroids = domap()

from collections import Counter

visible = Counter()

for start in asteroids:
    for end in asteroids:
        if start == end:
            continue
        if not any(a in asteroids for a in path(start, end)[:-1]):
            visible[start] += 1
print(visible.most_common(n=1)[0][1])
