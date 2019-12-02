#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import os
from math import *


def fuel_required(mass):
    return floor(mass / 3) - 2


print(sum(fuel_required(int(l)) for l in os.sys.stdin))
