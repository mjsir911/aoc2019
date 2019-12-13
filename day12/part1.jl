#!/usr/bin/env julia
import StaticArrays

struct Body{DimN}
		pos::StaticArrays.SVector{DimN,Int}
		vel::StaticArrays.SVector{DimN,Int}
end

function gravity(me::Body{N}, others::Vector{Body{N}})::Body{N} where N
	vel = me.vel + sum(sign.(o.pos - me.pos) for o in others)
	return Body(me.pos + vel, vel)
end

function simulate(bs::Vector{Body{N}} where N)
	Channel() do channel
		while true
			bs = [gravity(b, bs) for b in bs]
			put!(channel, bs)
		end
	end
end

function energy(me::Body)
	return sum(abs, me.pos) * sum(abs, me.vel)
end

function Body(pos)
	n = length(pos)
	return Body{n}(pos, zeros(n))
end

function Body(s::String)
	digit="-?[0-9]+"
	return Body(parse.(Int, match(Regex("<x=($digit), y=($digit), z=($digit)>"), s).captures))
end

bodies = Body.(readlines())

if abspath(PROGRAM_FILE) == @__FILE__
import IterTools
	fin = IterTools.nth(simulate(bodies), 1000)
	println(sum(energy, fin))
end
