#!/usr/bin/env bash

INFILE=$(realpath $1)
pushd $(dirname "$0") > /dev/null

function strip_comment() {
	grep '^[^#]'
}

strip_comment < $INFILE | ./encode.sh | ../computer | ./decode.awk; echo
