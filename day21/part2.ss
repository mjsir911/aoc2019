#!doit.sh
OR B T
AND C T
AND A T
NOT T J
AND D J
OR E T
OR H T
AND T J
RUN

!(a && b && c) && D && (H || (E))
