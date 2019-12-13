struct Body
		 pos::Vector{Int}
		 vel::Vector{Int}
end

function newvel(me::Body, other::Body)
	return sign.(other.pos - me.pos)
end

function interact(me::Body, others::Vector{Body})
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

function Body(p::Vector{Int})
	n = length(p)
	return Body(p, zeros(n))
end
b1 = Body([-13, 14, -7])
b2 = Body([-18, 9, 0])
b3 = Body([0, -3, -3])
b4 = Body([-15, 3, -13])


bodies = [b1, b2, b3, b4]
for i in range(1, stop=1000)
	global bodies
	bodies = [interact(b, bodies) for b in bodies]
end
println((+).(energy.(bodies)...))
