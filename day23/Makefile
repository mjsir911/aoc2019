PART1 := part1
PART2 := part2
include ../Makefile
include ../intcode/Makefile

part%: part%.go intnet.go computer 
	go build $< $(word 2,$^)
