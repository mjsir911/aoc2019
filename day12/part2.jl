struct Dimension
	pos::Int
	vel::Int
end
struct Body
	x::Dimension
	y::Dimension
	z::Dimension
end

function simulate(me::Dimension, others::Vector{Dimension})
	vel = 0
	for b in others
		if b == me
			continue
		end
		vel += sign(b.pos - me.pos)
	end
	return Dimension(me.pos + me.vel + vel, me.vel + vel)
end

function simulate(me::Body, others::Vector{Body})
	return Body(
		simulate(me.x, [o.x for o in others]),
		simulate(me.y, [o.y for o in others]),
		simulate(me.z, [o.z for o in others]),
	)
end

simulate(bs::Vector{Body}) = [simulate(b, bs) for b in bs]

b1 = Body(Dimension(-13, 0), Dimension(14, 0), Dimension(-7, 0))
b2 = Body(Dimension(-18, 0), Dimension(9, 0), Dimension(0, 0))
b3 = Body(Dimension(0, 0), Dimension(-3, 0), Dimension(-3, 0))
b4 = Body(Dimension(-15, 0), Dimension(3, 0), Dimension(-13, 0))
# b1 = Body([-13, 14, -7], [0, 0, 0])
# b2 = Body([-18, 9, 0], [0, 0, 0])
# b3 = Body([0, -3, -3], [0, 0, 0])
# b4 = Body([-15, 3, -13], [0, 0, 0])

# d1 = Dimension(-13, 0)
# d2 = Dimension(-18, 0)
# d3 = Dimension(0, 0)
# d4 = Dimension(-15, 0)
# d1 = Dimension(-1, 0)
# d2 = Dimension( 2, 0)
# d3 = Dimension( 4, 0)
# d4 = Dimension( 3, 0)

function period(a::Vector{Dimension})
	vectors = a
	i = 0
	while true
		i += 1
		vectors = [simulate(v, vectors) for v in vectors]
		if vectors == a
			return i
		end
	end
end

bodies = [b1, b2, b3, b4]
println(lcm(
	period([b.x for b in bodies]),
	period([b.y for b in bodies]),
	period([b.z for b in bodies]),
))
