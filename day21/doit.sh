#!/usr/bin/env bash

function strip_comment() {
	grep '^[^#]'
}

exec 4<&0
strip_comment < $1 | ./encode.sh | ./a.out | ./decode.awk; echo
