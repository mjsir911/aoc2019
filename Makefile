SHELL:=/bin/bash

TESTS1 := $(wildcard tests1/*.in) 
TESTS1 := $(TESTS1:.in=)
TESTS2 := $(wildcard tests2/*.in) 
TESTS2 := $(TESTS2:.in=)

PART1 ?= $(firstword $(wildcard part1*))
PART2 ?= $(firstword $(wildcard part2*))

PART1 += < $|
PART2 += < $|


all: test1 test2 run1 run2

$(foreach test,$(TESTS1),$(eval $(test): $(firstword $(PART1)) | $(test).in; diff <(./$$(PART1)) $$@.out))
$(foreach test,$(TESTS2),$(eval $(test): $(firstword $(PART2)) | $(test).in; diff <(./$$(PART2)) $$@.out))

.PHONY: test1
test1: $(sort $(TESTS1))

.PHONY: test2
test2: $(sort $(TESTS2))

.PHONY: run1
run1: $(firstword $(PART1)) | my.in
	./${PART1}

.PHONY: run2
run2: $(firstword $(PART2)) | my.in
	./${PART2}

clean:
	$(RM) $(shell cat .gitignore) $^
