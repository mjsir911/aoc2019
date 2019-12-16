#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import collections

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

Point = collections.namedtuple("Point", ["x", "y"])

from math import sqrt

def distance(p1, p2):
    xa, ya = p1
    xb, yb = p2
    return abs(xa - xb) + abs(ya - yb)


Line = collections.namedtuple("Line", ["a", "b"])

# m = abs(y2 - y1) / abs(x2 - x1)

# y - y1 = m(x - x1)
# y = m(x - x1) + y1


# find y, x when y1 = y2, x1 = x2
# Return true if line segments AB and CD intersect
def intersect(l1, l2):
    (A, B), (C, D) = l1, l2
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

# wire is list of lines
class Wire(tuple):
    @staticmethod
    def parse(s):
        p = Point(0, 0)
        tmp = []
        for inst in s.split(","):
            oldp = p
            if inst.startswith("R"):
                p = Point(p.x + int(inst.replace("R", "")), p.y)
            elif inst.startswith("L"):
                p = Point(p.x - int(inst.replace("L", "")), p.y)
            elif inst.startswith("U"):
                p = Point(p.x, p.y + int(inst.replace("U", "")))
            elif inst.startswith("D"):
                p = Point(p.x, p.y - int(inst.replace("D", "")))
            tmp.append(Line(oldp, p))
        return Wire(tmp)

    def intersect(self, w):
        for line1 in self:
            for line2 in w:
                if intersect(line1, line2):
                    yield intersect(line1, line2)



test = lambda s: distance(Point(0, 0), s)
w1 = Wire.parse("R8,U5,L5,D3")
w2 = Wire.parse("U7,R6,D4,L4")
print(w1)
print(w2)
print(list(w1.intersect(w2)))
print(list(map(test, w1.intersect(w2))))
