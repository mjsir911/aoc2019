SHELL:=/bin/bash

TESTS1 := $(wildcard tests1/*.in) 
TESTS1 := $(TESTS1:.in=)
TESTS2 := $(wildcard tests2/*.in) 
TESTS2 := $(TESTS2:.in=)

PART1 ?= $(wildcard part1*)
PART2 ?= $(wildcard part2*)


all: test1 test2 run1 run2

$(TESTS1): $(PART1)
	diff <(./$(PART1) < $@.in) $@.out

$(TESTS2): $(PART2)
	diff <(./$(PART2) < $@.in) $@.out

.PHONY: test1
test1: $(sort $(TESTS1))

.PHONY: test2
test2: $(sort $(TESTS2))

.PHONY: run1
run1: my.in $(PART1)
	./${PART1} < $<

.PHONY: run2
run2: my.in $(PART2)
	./${PART2} < $<
