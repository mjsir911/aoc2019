const Point = CartesianIndex{2}
const State = NamedTuple{(:keys, :pos), Tuple{Set{Char}, Point}}

function State(p::Point)
	State((Set{Char}(), p))
end
function State(ks::Set{Char}, p::Point)
	State((ks, p))
end

const Graph = Dict{Pair{State, State}, Int}

nearby = [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)]
function bfs(start, walkable, lookable)
	Channel() do chan
		seen = Set{Point}()
		cur = Set{Point}((start,))
		for cost in Iterators.countfrom(1)
			for c in copy(cur)
				pop!(cur, c)
				push!(seen, c)
				for near in nearby
					p = c + near
					if ! (p in seen)
					if walkable(p)
						push!(cur, p)
					end
					if lookable(p)
						put!(chan, (p, cost))
					end
					end
				end
			end
			if length(cur) == 0
				return
			end
		end
	end
end


m = Dict{Point, Char}()
for (y, line) in enumerate(readlines())
	for (x, char) in enumerate(line)
		m[Point(x, y)] = char
	end
end

startc = [c for (c, v) in m if v == '@'][1]

function lookable(ks)
	p -> !(m[p] in ks) && islowercase(m[p])
end

function walkable(ks)
	p -> m[p] == '.' || m[p] == '@' || lowercase(m[p]) in ks || (islowercase(m[p]) && m[p] in ks)
end

function reachables(pos, ks)
	return bfs(pos, walkable(ks), lookable(ks))
end
function reachables(s::State)
	return ((State(union(s.keys, [getkey(i[1])]), i[1]), i[2]) for i in reachables(s.pos, s.keys))
end

function getkey(p::Point)
	m[p]
end

possibilities = Graph()
start = State(startc)
println(start)
latest = Set{State}([start])

while length(latest) != 0
	global latest
	s = copy(latest)
	empty!(latest)
	for branch in s
		for i in reachables(branch)
			possibilities[branch=>i[1]] = i[2]
			push!(latest, i[1])
		end
	end
	# println(latest)
end

function distancemap(g, start)
	ret = Dict{State,Int}()
	ret[start] = 0
	t = Pair(Pair(start, start), 0)
	seen = Set([t])
	while true
		a = copy(seen)
		for new in g
			if new in a
				continue
			end
			if new.first.first in getfield.(getfield.(a, :first), :second)
				ret[new.first.second] = min(new.second + ret[new.first.first], get(ret, new.first.second, 100000))
				push!(seen, new)
			end
		end
		if a == seen
			break
		end
	end
	ret
end
println(start)
println(length(possibilities))
allkeys = sort(collect(possibilities), by=(n -> length(n.first.first.keys)))[end].first.second.keys
println([v for v in distancemap(possibilities, start) if v.first.keys == allkeys])
# goals = [g.pos for g in Set(getfield.(keys(possibilities), :second)) if g.keys == allkeys]

# println(allkeys)
# println(goals)
# Ok so technically I think this is a weighted directed acyclic graph but it also a
# single root node
# so, a weighted rooted directed acyclic graph
# wrdag
# drawg
# dwarg
# println(possibilities)
