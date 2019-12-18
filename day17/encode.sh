#!/usr/bin/env bash
while read; do
	for char in $(echo $REPLY | fold -w1); do
		printf "%d\n" "'$char"
	done
	printf "10\n"
done
