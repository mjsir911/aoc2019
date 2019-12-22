PART1 := part1
PART2 := part2

include ../Makefile
include ../intcode/Makefile

part1: CFLAGS=-DINPUT=1
part2: CFLAGS=-DINPUT=5
part%: ../intcode/computer.c
	$(CC) $(LDFLAGS) $(CPPFLAGS) $(CFLAGS) $(OUTPUT_OPTION) $<
