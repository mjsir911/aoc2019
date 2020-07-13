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
many ← {⍵,⊂eros ↑⌽⍵}

repeating ← {∨/∧/¨,¨(⊂↑⌽⍺)=⍵}

biodiversity ← {+/ (,⍵) ∧ 2*((⍳⍴,⍵) - 1) }

]BOXING 9
↑⌽many⍣repeating ⊂world
biodiversity ↑⌽many⍣repeating ⊂world
