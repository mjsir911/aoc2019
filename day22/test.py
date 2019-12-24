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

cut = lambda c, n: c[n:] + c[:n]

# print(cut([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
#
# print(cut([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], -4))

def increment(c, n):
    ret = [0] * len(c)
    for i, card in enumerate(c):
        ret[(i * n) % len(ret)] = card
    return ret

# factory = list(range(card_size))
# print(increment(factory, 3))

def parse(line, cards):
    inst, *args = line.split()
    if inst == 'deal':
        if args[-1].isdigit():
            return increment(cards, int(args[-1]))
        return deal(cards)
    if inst == 'cut':
        return cut(cards, int(args[-1]))

import sys
cards = list(range(card_size))

insts = [l for l in sys.stdin if l]
for line in insts:
    cards = parse(line, cards)

cardi = cards[3589]
cards = list(range(card_size))
print(cards.index(cardi))
print(cards)
for line in insts:
    cards = parse(line, cards)
    print(cards)
    print(cards.index(cardi))
