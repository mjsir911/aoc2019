#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
from itertools import repeat, islice
from sys import stdin


class Factory():
    def __init__(self, max_buf, inputs):
        self.max_buf = max_buf
        self.inputs = (sum(i) for i in zip(*inputs))
        self.amount_left = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.amount_left -= 1
        if self.amount_left > 0:
            return 0
        else:
            self.amount_left = self.max_buf
            return next(self.inputs)

    @classmethod
    def fromGraph(cls, g, goal, known=None):
        if known is None:
            known = {}

        if goal not in known:
            # this is a mess
            # see V for at least an explanation for the double comprehension
            # https://spapas.github.io/2016/04/27/python-nested-list-comprehensions/
            ins = [a for subgoal, amount in g[goal][1].items() for a in [cls.fromGraph(g, subgoal, known)] * amount]
            known[goal] = cls(g[goal][0], ins)
        return known[goal]


ore = islice(repeat(1), int(1e12))

dependency_graph = {}


def parse(s):
    amount, name = s.split(' ')
    return name, int(amount)


for line in stdin:
    ins, out = line.strip().split(' => ')
    ins = dict(parse(i) for i in ins.split(', '))
    out = parse(out)

    dependency_graph[out[0]] = (out[1], ins)

# print(dependency_graph)
fuel = Factory.fromGraph(dependency_graph, 'FUEL', {'ORE': ore})
print(next(fuel))

fuel_num = 0
used_ore = 0
for i in fuel:
    fuel_num += 1
    used_ore += i
    print(used_ore, fuel_num)

print(fuel_num)
