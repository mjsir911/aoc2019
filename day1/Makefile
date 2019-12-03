PART1 := part1

include ../Makefile

% %.hi %.o: %.hs
	ghc $<

clean:
	$(RM) *.o *.hi $(PART1) $(PART2)
