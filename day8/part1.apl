INP ← ⍎¨⍕⍞

DECODE ← {(((↑⍴⍵)÷(×/⍺)),⍺) ⍴ ⍵}

IMG ← 6 25 DECODE INP

⍝ layer with least amount of 0s (first of sorted sums IMG=0)
LAYER ← IMG[↑⍋ (+/+/(IMG = 0));;]

⍝ # of 1s * # of 2s
⎕← (+/+/LAYER=1) × (+/+/LAYER=2)

myop ← {((⍺=2) × ⍵) + ((⍺≠2)×⍺)}
⎕← (myop ⌿) IMG
