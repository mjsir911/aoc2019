#!/usr/bin/env -S nim c -r -f --verbosity:0

const jump_distance* = 4

type Register* = enum
  jump="J", temp="T", A="A", B="B", C="C", D="D", E="E", F="F", G="G", H="H"

proc isGround*(n: int): Register =  Register(n + 1)

when isMainModule:
  import springscript
  springScript:
    jump = not isGround(3)
    jump = isGround(jump_distance) and jump
    temp = not isGround(1)
    jump = jump or temp
    walk()
