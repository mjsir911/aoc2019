#!/usr/bin/env -S apl --OFF -s -f

neighbors ← {↑+/(¯1 1∘.⊖⊂⍵),(¯1 1∘.⌽⊂⍵)}
eros2 ← {~((1≠neighbors ⍵) ∧ ⍵)}
eros1 ← {((1=neighbors ⍵) ∨ (2=neighbors ⍵)) ∧ eros2 ⍵}
g←{{0⍪0⍪⍨2 1⍉⍵}⍣2⊢⍵}
gi ← {¯1 ¯1↓1 1↓⍵}
eros ← { gi eros1 g ⍵ }
life ← eros
Show←{'.#'[⎕IO+⍵]}
world ← 5 5 ⍴ 0 1 0 1 1 0 1 1 1 0 1 1 0 1 0 1 1 1 1 0 1 1 0 1 1
]BOXING 9
many ← {⍵,⊂eros ↑⌽⍵}

repeating ← {∨/∧/¨,¨(⊂↑⌽⍺)=⍵}

# dup1 ← ,↑⌽many⍣86 ⊂world
# (many⍣86 ⊂world) repeating (many⍣85 ⊂world)
# (many⍣86 ⊂world) repeating (many⍣85 ⊂world)

biodiversity ← {+/ (,⍵) ∧ 2*((⍳25) - 1) }

↑⌽many⍣repeating ⊂world
biodiversity ↑⌽many⍣repeating ⊂world
# many⍣10 ⊂world
# (many⍣61 ⊂world) repeating (many⍣70 ⊂world)

# ∧/¨(,¨((⊂world)=(many⍣10 ⊂world)))
