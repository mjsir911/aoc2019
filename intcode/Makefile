LDFLAGS := -lm
CPPFLAGS := -I$(shell pwd)

PART1 += 4<&0
PART2 += 4<&0
mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))

my.in:
	touch my.in

computer: $(mkfile_dir)/computer.c my.in
	$(CC) $(CPPFLAGS) $(LDFLAGS) $(OUTPUT_OPTION) $<

$(firstword $(PART1)) $(firstword $(PART2)): computer

clean: computer
