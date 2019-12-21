#!/usr/bin/env bash

function strip_comment() {
	grep '^[^#]'
}

strip_comment < $1 | ./encode.sh | ./a.out | ./decode.awk; echo
