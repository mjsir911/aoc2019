import macros
import strutils

macro springScript*(script: untyped): untyped =
  # eventually I'll want to load this straight into the computer and return the
  # array of integers.
  script.expectKind nnkStmtList
  for i, line in script.pairs:
    case line.kind
    of nnkAsgn:
      let dest = line[0]
      let expr = line[1]
      case expr.kind
      of nnkInfix:
        if line[0] notin expr[1..2]: error("Must assign to argument")
        let arg1 = expr[1]
        let arg2 = expr[2]
        let otherarg = if dest == arg1: arg2 else: arg1
        script[i] = newCall("echo", newStrLitNode(expr[0].strVal.toUpper), newStrLitNode(" "), otherarg, newStrLitNode(" "), dest )
      of nnkPrefix:
        let otherarg = expr[1]
        script[i] = newCall("echo", newStrLitNode(expr[0].strVal.toUpper), newStrLitNode(" "), otherarg, newStrLitNode(" "), dest)
      else:
        expr.expectKind({nnkInfix, nnkPrefix})
    of nnkCall:
      script[i] = newCall("echo", newStrLitNode(line[0].strVal.toUpper))
    else:
      line.expectKind({nnkAsgn, nnkCall})
  result = script
