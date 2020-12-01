PART1 = part1.mac
PART2 = part2.mac
include ../Makefile

run1: $(firstword $(PART1)) | my.in
	maxima --very-quiet -b ./${PART1}
run2: $(firstword $(PART2)) | my.in
	maxima --very-quiet -b ./${PART2}
