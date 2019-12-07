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

class Orbit:
    def orbits(self):
        return self.child.orbits() + [self.child]


class COM:
    def orbits(self):
        return []

file = open('my.in')
orbits = {
    'COM': COM()
}
for line in file:
    com, body  = line.strip().split(')')
    orbits[body] = Orbit()

file = open('my.in')
for line in file:
    com, body  = line.strip().split(')')
    orbits[body].child = orbits[com]

total = 0
for body in orbits.values():
    total += len(body.orbits())
print(total)

