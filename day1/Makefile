PART1 := part1
PART2 := part2

include ../Makefile

% %.hi %.o: %.hs
	ghc $<

clean:
	$(RM) *.o *.hi $(PART1) $(PART2)
