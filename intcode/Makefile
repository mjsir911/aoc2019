LDFLAGS := -lm
CPPFLAGS := -I$(shell pwd)

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))

my.in:
	touch my.in

computer: $(mkfile_dir)/computer.c my.in
	$(CC) $(CPPFLAGS) $(LDFLAGS) $(OUTPUT_OPTION) $<

.PHONY: run1
run1: my.in $(PART1)
	./${PART1} 4< $<

.PHONY: run2
run2: my.in $(PART2)
	./${PART2} 4< $<


$(PART1) $(PART2): computer

clean: computer
