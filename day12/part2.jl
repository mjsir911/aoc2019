include("part1.jl")

function period(bs::Vector{Body{N}}) where N
	for (i, newbs) in enumerate(simulate(bs))
		if newbs == bs
			return i
		end
	end
end

println(lcm(
	period([Body([b.pos[1]]) for b in bodies]),
	period([Body([b.pos[2]]) for b in bodies]),
	period([Body([b.pos[3]]) for b in bodies]),
))
