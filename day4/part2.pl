#!/usr/bin/env swipl
:- use_module(library(clpfd)).
:- [part1].

shy_adjacent_doubles([B, A, A]) :- B #\= A.
shy_adjacent_doubles([B, A, A, C|_]) :- B #\= A, C #\= A.
shy_adjacent_doubles([B|R]) :- shy_adjacent_doubles(R).

part2(N) :- setof(L, (valid_password(L), shy_adjacent_doubles([-1|L]), label(L)), C), length(C, N).
