#!/usr/bin/env -S nim c -r -f --verbosity:0
import springscript
import part1

springScript:
  temp = isGround(2) or temp                 # OR B T
  temp = isGround(3) and temp                # AND C T
  temp = isGround(1) and temp                # AND A T
  jump = not temp                            # NOT T J
  jump = isGround(jump_distance) and jump    # AND D J
  temp = isGround(jump_distance + 1) or temp # OR E T
  temp = isGround(jump_distance * 2) or temp # OR H T
  jump = temp and jump                       # AND T J
  run()
