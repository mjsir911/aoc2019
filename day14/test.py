#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
from itertools import repeat


class Factory():
    def __init__(self, max_buf, inputs):
        self.max_buf = max_buf
        self.inputs = inputs
        self.amount_left = 0

    def __next__(self):
        self.amount_left -= 1
        if self.amount_left > 0:
            return 0
        else:
            self.amount_left = self.max_buf
            return sum(next(i) for i in self.inputs)


ore = repeat(1)

a = Factory(2, [ore] * 9)
b = Factory(3, [ore] * 8)
c = Factory(5, [ore] * 7)

ab = Factory(1, [a] * 3 + [b] * 4)
bc = Factory(1, [b] * 5 + [c] * 7)
ca = Factory(1, [c] * 4 + [a] * 1)

fuel = Factory(1, [ab] * 2 + [bc] * 3 + [ca] * 4)

print(next(fuel))
