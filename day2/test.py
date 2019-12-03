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

"1,0,0,0,99"

def f1(noun, verb):
    reel = [1, noun, verb, 0, 99]
    reel[reel[3]] = add(noun, verb)

"1,1,1,4,99,5,6,0,99"
def f2(noun, verb):
    def dispatch(reel, i):
        op = reel[i]
        # state machine has three conditionals:
        # 1) 99 is not in the four-evened previous cells
        # 2) r[i] = 1 iff r[r[i+3]] = r[i+1] + r[i+2]
        # 3) r[i] = 2 iff r[r[i+3]] = r[i+1] * r[i+2]
        # because the only modified inputs are r[1] & r[2], you can create a
        # static function that evaluates answer based on r[1] & r[2]
        arg1, arg2 = reel[i + 1], reel[i + 2]
        ret = (99 not in reel[0:i:4]) * (
                  (op == 2) * (reel[i + 1] * reel[i + 2]) +\
                  (op == 1) * (arg1 + arg2)
              ) +\
              ((99 in reel[0:i:4]) * reel[reel[i + 3]])
        reel[reel[i + 3]] = ret
        return reel

    reel = [1, noun, verb, 4, 99, 5, 6, 0, 99]
    for i in range(0, 99, 4):
        print(reel)
        if reel[i] == 99:
            return reel
        reel = dispatch(reel, i)

print(f2(1, 1))
