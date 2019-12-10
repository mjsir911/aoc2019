LDFLAGS := -lm
PART1 := part1
PART2 := part2

include ../Makefile


part1.o: CFLAGS=-DINPUT=1
part2.o: CFLAGS=-DINPUT=2
part%.o: computer.c
	$(LINK.c) -c $(OUTPUT_OPTION) $<
