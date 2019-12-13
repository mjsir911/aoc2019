include("part1.jl")

function period(a::Vector{Body{N}}) where N
	vectors = a
	i = 0
	while true
		i += 1
		vectors = [interact(v, vectors) for v in vectors]
		if vectors == a
			return i
		end
	end
end

println(lcm(
	period([Body((b.pos[1],)) for b in bodies]),
	period([Body((b.pos[2],)) for b in bodies]),
	period([Body((b.pos[3],)) for b in bodies]),
))
