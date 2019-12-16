#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import os
from math import *


def fuel_required_revised(mass):
    ret = floor(mass / 3) - 2
    if ret <= 0:
        return 0
    return ret + fuel_required_revised(ret)


print(sum(fuel_required_revised(int(l)) for l in os.sys.stdin))
