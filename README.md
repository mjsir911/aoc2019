# Advent of code 2019

I'm trying to find idiomatic languages to do challenges in.

For example, day 8 was decoding a toy image encoding, which is arrays on
arrays, which is APL.

Or day 7, which required chaining together different [intcode
computers](./intcode/computer.c`), which it turns out is a really easy job in
bash (just a few `|`s)


Some languages I haven't really found great fits for:
- Trigonometry / polar coordinates / raytracing
: For day 10, we were asked to calculate which asteroids were behind eachother.
This requires some matrix math and/or angle math for stuff. There are plenty of
numerical programming languages, but nothing really shines here

- Graphs & trees
: Same idea, for day 14, and 15 to an extend we were asked to do calculations
which required graph searches and sorts. I haven't found a great language for
this, but I've seen others use python with the `networkx` module.


- Controlling robots!
: So, logo actually works great for this and I've done two project solutions
now in logo. My complaint is actually that the logo implementation I'm using
(ucblogo) ended up crashing on me due to drawing too much. It's also a pretty
old language so doing anything fancy in it requires building from the ground up


Some languages I want to use for *something*:
- perl maybe for more advanced pipe stuff
- perl6/raku for some fancy generator / limit stuff ( see [e][0] for inspiration )
- tcl, though I haven't found a good fit for it yet.
- haskell & functional friends. Can't find enough challenges that lend
	themselves to functional solutions
- ocaml. I've heard its good for writing compilers. Maybe intcode de/compiler?
- red / rebol, very slightly, but I don't get what the big deal is.
- ada for something. doesn't lend itself to anything here
- Erlang for something.
- Forth for something
- Unfortunately, I'll want to do something in java
- Javascript for something. There really should be some use case I'm not
	thinking of
- postscript, for the lols
- D as a computation replacement for julia/C one day
- ALGOL / BASIC ?
- smalltalk?
- surely I could find something to do with awk
- oh, I wonder how you program in sql?

Half the problem is getting new languages installed onto my machine.

I'm mostly doing fast leaderboard attempts in python, I got #40 for part 1 some
day when I really shouldn't have



[0]: http://blogs.perl.org/users/damian_conway/2019/09/to-compute-a-constant-of-calculusa-treatise-on-multiple-ways.html
