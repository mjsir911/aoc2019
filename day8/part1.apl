#!/usr/bin/env -S apl --OFF -s -f
INP ← ⍎¨⍞

RESHAPE_OVERFLOW ← {(((↑⍴⍵)÷(×/⍺)),⍺) ⍴ ⍵}

IMG ← 6 25 RESHAPE_OVERFLOW INP

⍝ layer with least amount of 0s (first of sorted sums IMG=0)
helper ← {⍵[↑⍋ (+/+/(⍵=0));;]}

CHECKSUM ← {(+/+/(helper ⍵)=1) × (+/+/(helper ⍵)=2)}

⍝ # of 1s * # of 2s
⎕← CHECKSUM IMG

DECODE ← {({((⍺=2) × ⍵) + ((⍺≠2)×⍺)} ⌿) ⍵}
⎕← DECODE IMG
