struct Body
		 pos::Array{Int,1}
		 vel::Array{Int,1}
end

function newvel(me::Body, other::Body)
	return sign.(other.pos - me.pos)
end

function interact(me::Body, others::Array{Body,1})
	vel = me.vel
	for b in others
		if b == me
			continue
		end
		vel += newvel(me, b)
	end
	return Body(me.pos + vel, vel)
end

function interactpos(me::Body)
	return Body(me.pos + me.vel, me.vel)
end

function energy(me::Body)
	return sum(abs, me.pos) * sum(abs, me.vel)
end

b1 = Body([-13, 14, -7], [0, 0, 0])
b2 = Body([-18, 9, 0], [0, 0, 0])
b3 = Body([0, -3, -3], [0, 0, 0])
b4 = Body([-15, 3, -13], [0, 0, 0])


bodies = [b1, b2, b3, b4]
for i in range(1, stop=1000)
	global bodies
	bodies = [interact(b, bodies) for b in bodies]
end
println((+).(energy.(bodies)...))
