#!/usr/bin/env swipl
:- use_module(library(clpfd)).

% near(A, B) :- A #= B + 1; A #= B - 1.
% adjacent_doubles(L) :- element(IA, L, A), element(IB, L, A), near(IA, IB).
adjacent_doubles([A, A|_]).
adjacent_doubles([_|R]) :- adjacent_doubles(R).

incrementing([_]).
incrementing([A,B|R]) :- A #=< B, incrementing([B|R]), !.

password(N, [A, B, C, D, E, F]) :- F #= N mod 10, E #= N // 10 mod 10, D #= N // 100 mod 10, C #= N // 1000 mod 10, B #= N // 10000 mod 10, A #= N // 100000 mod 10.

within_range(L, R) :- N in R, password(N, L).

valid_password(L) :- within_range(L, 272091..815432), adjacent_doubles(L), incrementing(L).

part1(N) :- setof(L, (valid_password(L), label(L)), C), length(C, N).
