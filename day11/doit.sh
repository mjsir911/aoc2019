#!/usr/bin/env bash

loop=$(mktemp)
rm $loop
mkfifo $loop

function unbuffer() {
	stdbuf -i0 -o0 -e0 $@
}


exec 4<&0
unbuffer cat < $loop | unbuffer $1 | ./computer > $loop
