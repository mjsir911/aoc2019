#!/usr/bin/env bash

function permut() {
	python3 <<-EOF
	import itertools
	inp = [int(l) for l in '$@'.split(' ')]
	print("\n".join(" ".join(str(c) for c in l) for l in itertools.permutations(inp)))
	EOF
}

function phase() {
	(echo $1; cat) | ./a.out
}

function amplify() {
	echo 0 | phase $1 | phase $2 | phase $3 | phase $4 | phase $5
}



gcc computer.c -lm -DINTPROG="$(cat | tr -d '\n')"
permut 0 1 2 3 4 | while read line; do
	echo $(amplify $line)
done | sort -n | tail -n 1
