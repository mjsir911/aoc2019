#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

from sys import stdin


def fuel_required(mass):
    return mass // 3 - 2


print(sum(fuel_required(int(l)) for l in stdin))
