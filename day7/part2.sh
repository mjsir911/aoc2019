#!/usr/bin/env bash

function unbuffer() {
	stdbuf -i0 -o0 -e0 $@
}

function permut() {
	python3 <<-EOF
	import itertools
	inp = [int(l) for l in '$@'.split(' ')]
	print("\n".join(" ".join(str(c) for c in l) for l in itertools.permutations(inp)))
	EOF
}

function phase() {
	(echo $1; unbuffer cat) | stdbuf -i0 -o0 -e0  ./a.out 2> /dev/null
}

function amplify() {
	loop=$(mktemp -u)
	mkfifo $loop
	trap "rm $loop" EXIT

	(echo 0; unbuffer timeout 0.2 cat <$loop) | phase $1 | phase $2 | phase $3 |phase $4 | phase $5 > >(tee /dev/stdout $loop) | tail -n 1
}


permut 5 6 7 8 9 | while read line; do
	echo $line $(amplify $line)
done | sort -n -k 6 | tail -n 1
