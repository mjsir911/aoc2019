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

def doit(length, f):
    l = [0] * length
    for i in range(length):
        l[f(i)] = i
    return l

def doit_rev(length, f):
    l = [0] * length
    for i in range(length):
        l[i] = f(i)
    return l

def deal(length):
    def wraps(i):
        return length - i - 1
    return wraps

deal_rev = deal
assert deal_rev(10)(0) == 9
assert deal_rev(10)(9) == 0

def cut(length, n):
    def wraps(i):
        if n > 0:
            if i >= n:
                return i - n
            else:
                return length + i - n
        if n < 0:
            n = abs(n)
            if i >= length - n:
                return i - length + n
            else:
                return n + i
    return wraps

exit()

def cut_rev(length, n):
    def wraps(i):
        nonlocal n
        if n > 0:
            if i >= (length - n):
                return abs((length - n) - i)
            else:
                return i + n
        if n < 0:
            n = abs(n)
            if i < n:
                return length - n + i
            else:
                return i - n
    return wraps


assert cut_rev(10, 3)(7) == 0
assert cut_rev(10, 3)(9) == 2

assert cut_rev(10, 3)(0) == 3
assert cut_rev(10, 3)(4) == 7
assert cut_rev(10, 3)(6) == 9

assert cut_rev(10, -4)(0) == 6
assert cut_rev(10, -4)(3) == 9
assert cut_rev(10, -4)(4) == 0
assert cut_rev(10, -4)(9) == 5



def increment(length, n):
    def wraps(i):
        return i * n % length
    return wraps


# x = y * n % length
# x // n = y % length

class MyNone():
    def __repr__(self):
        return '_'

MyNone = MyNone()

def increment_rev(length, n):
    def whichloop(i):
        return -i % n

    def numinside(loop):
        return (length - (loop % n) - 1) // n + 1

    def overflow(i):
        return abs((length - i) % n - 1)

    def prev_overflow(i):
        return overflow(i + 1)

    def prev(i):
        return i - n

    def lastloop_prev(loop):
        pass

    def wraps(i):
        return numinside(i)
        return whichloop(i)
        loop = whichloop(i)
        if loop == 0:
            return 9
        return n - prev_overflow(i)
        # return (i % n * (length % n) + i // n) % length
        # offset =
        # return ((length // n) + i // n) * (i % n) + -length % n
    return wraps

# print(list(range(10)))
n = 3
print('c ', doit(10, increment(10, n)))  # increments by 7s
print('m ', doit_rev(10, increment_rev(10, n)))  # increments by 7s
print()
n = 7
print('c ', doit(10, increment(10, n)))  # increments by 7s
print('m ', doit_rev(10, increment_rev(10, n)))  # increments by 7s
# # doit(7) # incremnes by 3s
# doit(9) # incremnets by 9s
# print([0, 9, 8, 7, 6, 5, 4, 3, 2, 1])
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

# length = 19315717514047
# length = 10
length = 10007
index = 3589

import sys

f = parse_rev('deal with increment 12', length)
print(doit(f, length)[:15])
print([0, 834, 1668, 2502, 3336, 4170, 5004, 5838, 6672, 7506, 8340, 9174, 1, 835, 1669])
# insts = sys.stdin.read().split('\n')
# insts = [parse_rev(i, length) for i in insts if i]
#
# print(index)
# for command in reversed(insts):
#     index = command(index)
#     print(index)
