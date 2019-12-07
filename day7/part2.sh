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
	(echo $1; cat) | unbuffer ./a.out
}

function start() {
	(echo 0; cat) | phase $1
}

function amplify() {
	in=$(mktemp -u)
	out=$(mktemp -u)
	mkfifo $in $out
	unbuffer cat $in | phase $1 | phase $2 | phase $3 | phase $4 | phase $5 > $out &
	unbuffer cat $out | tee /dev/stderr > $in &

	echo 0 > $in

	wait $engined
	# unbuffer cat $out | while read line; do echo $line >&2; echo $line ; done > $in
}


# permut 5 6 7 8 9 | while read line; do
# 	echo $line $(amplify $line)
# 	sleep 0.1
# done

mkfifo start
(echo 0; unbuffer cat start) | phase 9 | phase 8 | phase 7 | phase 6 | phase 5 > start
