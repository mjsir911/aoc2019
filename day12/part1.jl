import StaticArrays

struct Body{DimN}
		pos::StaticArrays.SVector{DimN,Int}
		vel::StaticArrays.SVector{DimN,Int}
end

function newvel(me::Body{N}, other::Body{N}) where N
	return sign.(other.pos - me.pos)
end

function interact(me::Body, others::Vector{Body{N}})::Body{N} where N
	vel = me.vel
	for b in others
		if b == me
			continue
		end
		vel += newvel(me, b)
	end
	return Body(me.pos + vel, vel)
end

function energy(me::Body)
	return sum(abs, me.pos) * sum(abs, me.vel)
end

function Body(p::NTuple{N, Int}) where N
	return Body{N}(p, zeros(N))
end
b1 = Body((-13, 14, -7))
b2 = Body((-18, 9, 0))
b3 = Body((0, -3, -3))
b4 = Body((-15, 3, -13))


bodies = [b1, b2, b3, b4]
for i in range(1, stop=1000)
	global bodies
	bodies = [interact(b, bodies) for b in bodies]
end
println(sum(energy, (bodies)))
