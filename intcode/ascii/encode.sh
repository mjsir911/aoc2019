#!/usr/bin/env bash
while read; do
	echo "$REPLY" | fold -w1 | while read; do
		printf "%d\n" "'$REPLY"
	done
	printf "10\n"
done
