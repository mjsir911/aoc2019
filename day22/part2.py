#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

__appname__     = "part2"
__author__      = "@AUTHOR@"
__copyright__   = ""
__credits__     = ["@AUTHOR@"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "@AUTHOR@"
__email__       = "@EMAIL@"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""


def modinv(x, p):
    return pow(x, p-2, p)


def doit(length, f):
    l = [0] * length
    for i in range(length):
        l[f(i) % length] = i
    return l


def doit_rev(length, f):
    l = [0] * length
    for i in range(length):
        l[i] = f(i) % length
    return l


def deal(length):
    def wraps(i):
        return -i - 1
    return wraps

deal_rev = deal
assert deal_rev(10)(0) == 9
assert deal_rev(10)(9) == 0

def cut(length, n):
    def wraps(i):
        return (i - n) % length
    return wraps

def cut_rev(length, n):
    def wraps(i):
        return (i + n + length)
    return wraps


# assert cut_rev(10, 3)(7) == 0
# assert cut_rev(10, 3)(9) == 2
#
# assert cut_rev(10, 3)(0) == 3
# assert cut_rev(10, 3)(4) == 7
# assert cut_rev(10, 3)(6) == 9
#
# assert cut_rev(10, -4)(0) == 6
# assert cut_rev(10, -4)(3) == 9
# assert cut_rev(10, -4)(4) == 0
# assert cut_rev(10, -4)(9) == 5



def increment(length, n):
    def wraps(i):
        return i * n
    return wraps

def increment_rev(length, n):
    def wraps(i):
        return i // n
    return wraps

print([increment_rev(10, 3)(increment(10, 3)(i)) for i in range(10)])
# print(doit_rev(10, increment_rev(10, 3)))
exit()


# assert increment_rev(10, 3)(0) == 0
# assert increment_rev(10, 3)(3) == 1
# assert increment_rev(10, 3)(6) == 2
# assert increment_rev(10, 3)(9) == 3
#
# assert increment_rev(10, 3)(2) == 4
# assert increment_rev(10, 3)(5) == 5
# assert increment_rev(10, 3)(8) == 6
#
# assert increment_rev(10, 3)(1) == 7
# assert increment_rev(10, 3)(4) == 8
# assert increment_rev(10, 3)(7) == 9


def parse(line, length):
    inst, *args = line.split()
    if inst == 'deal':
        if args[-1].isdigit():
            return increment(length, int(args[-1]))
        return deal(length)
    if inst == 'cut':
        return cut(length, int(args[-1]))


def parse_rev(line, length):
    inst, *args = line.split()
    if inst == 'deal':
        if args[-1].isdigit():
            return increment_rev(length, int(args[-1]))
        return deal_rev(length)
    if inst == 'cut':
        return cut_rev(length, int(args[-1]))


def compose(f, g):
    return lambda x: f(g(x))

# length = 19315717514047
# length = 10
length = 10007
index = 3589

import sys

insts = open('my.in', 'r').read().split('\n')
insts = [parse_rev(i, length) for i in insts if i]

from functools import reduce
f = reduce(compose, insts)

class Polynomial(tuple):
    def __call__(self, x):
        return sum(mul * (x ** i) for i, mul in enumerate(reversed(self)))

    def __pow__(self, n):
        assert n == 2
        return Polynomial(((self[0] ** 2), self[0] * self[1] + self[1]))

    def __mod__(self, n):
        from operator import mod
        from itertools import repeat
        return Polynomial(map(mod, self, repeat(n)))

# f = Polynomial((-17584892732278919399014760500371073496575520206629306885585573311933055587053384343403253418618412807862531365703696551339613887356028695756144640000000,
#            -279894881169884414520727297171387139533541678605363352096978380061550209875419931903039237651322820491002708411625967820599124581520932680764840034226064636)) % length


# f = lambda x: \
#     (-17584892732278919399014760500371073496575520206629306885585573311933055587053384343403253418618412807862531365703696551339613887356028695756144640000000 % length) * x +\
#     (-279894881169884414520727297171387139533541678605363352096978380061550209875419931903039237651322820491002708411625967820599124581520932680764840034226064636 % length)

print(f)
print(f(index) % length)
print(f(f(index)) % length)
print(f(f(f(index))) % length)
print(f(f(f(f(index)))) % length)
# print(f(f(f(f(f(f(index)))))) % length)
# print(((f ** 2) ** 2)(index) % length)
# print(f(index) % length)
