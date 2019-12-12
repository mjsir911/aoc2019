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

import collections


class Pos(collections.namedtuple("Pos", "x y z")):
    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y, self.z + other.z)

    def energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


class Vel(collections.namedtuple("Vel", "x y z")):
    def __add__(self, other):
        return Vel(self.x + other.x, self.y + other.y, self.z + other.z)

    def energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


class Body():
    def __init__(self, pos, vel=Vel(x=0, y=0, z=0)):
        self.pos = pos
        self.vel = vel

    def newvel(self, other):
        return Vel(
            0 if self.pos.x == other.pos.x else 1 if self.pos.x < other.pos.x else -1,
            0 if self.pos.y == other.pos.y else 1 if self.pos.y < other.pos.y else -1,
            0 if self.pos.z == other.pos.z else 1 if self.pos.z < other.pos.z else -1,
        )

    def energy(self):
        return self.pos.energy() * self.vel.energy()

    def __repr__(self):
        return f'Body(pos={self.pos}, vel={self.vel}, energy={self.energy()})'

    def __eq__(self, other):
        return self.pos == other.pos and self.vel == other.vel

    def __hash__(self):
        return hash((self.pos, self.vel))


b1 = Body(pos=Pos(x=-13, y=14, z=-7))
b2 = Body(pos=Pos(x=-18, y=9, z=0))
b3 = Body(pos=Pos(x=0, y=-3, z=-3))
b4 = Body(pos=Pos(x=-15, y=3, z=-13))

# b1 = Body(pos=Pos(x=-1, y=0, z=2))
# b2 = Body(pos=Pos(x=2, y=-10, z=-7))
# b3 = Body(pos=Pos(x=4, y=-8, z=8))
# b4 = Body(pos=Pos(x=3, y=5, z=-1))


seen = set()
bodies = (b1, b2, b3, b4)
seen.add(bodies)
i = 0
while True:
    i += 1
    for ba in bodies:
        for bb in bodies:
            if ba == bb:
                continue
            ba.vel += ba.newvel(bb)

    bodies = tuple(Body(pos=b.pos + b.vel, vel=b.vel) for b in bodies)

    if hash(bodies) in seen:
        print(i)
        break
    seen.add(hash(bodies))

