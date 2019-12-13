include("part1.jl")

function period(bs::Vector{Body{N}}) where N
	for (i, newbs) in enumerate(simulate(bs))
		if newbs == bs
			return i
		end
	end
end

println(lcm(period.(
	[Body([b.pos[i]]) for b in bodies]
	for i in [1, 2, 3]
)))
