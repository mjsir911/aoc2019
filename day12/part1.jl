import StaticArrays

struct Body{DimN}
		pos::StaticArrays.SVector{DimN,Int}
		vel::StaticArrays.SVector{DimN,Int}
end

function gravity(me::Body, others::Vector{Body{N}})::Body{N} where N
	vel = me.vel + sum(sign.(o.pos - me.pos) for o in others)
	return Body(me.pos + vel, vel)
end

function energy(me::Body)
	return sum(abs, me.pos) * sum(abs, me.vel)
end

function Body(pos)
	n = length(pos)
	return Body{n}(pos, zeros(n))
end
b1 = Body([-13, 14, -7])
b2 = Body([-18, 9, 0])
b3 = Body([0, -3, -3])
b4 = Body([-15, 3, -13])


bodies = [b1, b2, b3, b4]
if abspath(PROGRAM_FILE) == @__FILE__
	for i in range(1, stop=1000)
		global bodies
		bodies = [gravity(b, bodies) for b in bodies]
	end
	println(sum(energy, (bodies)))
end
