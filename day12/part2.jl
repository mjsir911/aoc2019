include("part1.jl")

function gravity(me::Body{1}, others::Vector{Body{1}})::Body{1}
	vel = me.vel[1] + sum(sign(o.pos[1] - me.pos[1]) for o in others)
	return Body{1}((me.pos[1] + vel,), (vel,))
end

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
