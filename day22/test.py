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

# card_size = 119315717514047
card_size = 10007

deal = lambda c: list(reversed(c))


def deal():
    return lambda i: -i - 1


def cut(n):
    return lambda i: i - n


def increment(n):
    return lambda i: i * n


def parse(line):
    inst, *args = line.split()
    if inst == 'deal':
        if args[-1].isdigit():
            return increment(int(args[-1]))
        return deal()
    if inst == 'cut':
        return cut(int(args[-1]))


def compose(f, g):
    return lambda i: f(g(i))


f = lambda x: x  # identity function
import sys
insts = [l for l in sys.stdin if l]
for line in insts:
    f = compose(parse(line), f)
    # cards = parse(line, cards)

print(f(2019) % card_size)

# cardi = cards[3589]
# cards = list(range(card_size))
# print(cards.index(cardi))
# print(cards)
# for line in insts:
#     cards = parse(line, cards)
#     print(cards)
#     print(cards.index(cardi))
