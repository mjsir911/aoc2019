#!/usr/bin/env bash

loop=$(mktemp)
rm $loop
mkfifo $loop

function unbuffer() {
	stdbuf -i0 -o0 -e0 $@
}


unbuffer cat < $loop | unbuffer ./part1.logo | ./a.out > $loop
