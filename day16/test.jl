# function phase(l::Vector{Int}, p)
# 	test = Iterators.drop(Iterators.cycle(p), 1)
# 	return abs(sum([(n * m) for (n, m) in Iterators.zip(l, test)])) % 10
# end
# 
# function mul_iter(i::Vector{Int}, n::Int)
# 	Channel() do channel
# 		for thing in i
# 			for _ in 1:n
# 				put!(channel, thing)
# 			end
# 		end
# 	end
# end

# only calculates at most length(l)/2:length(l)
function phase(l::Vector{Int})
	runsum::Int = 0
	for (i, thing) in Iterators.reverse(enumerate(l))
		runsum += thing
		runsum %= 10
		s[i] = runsum
	end
end



inp = readline()
i = parse(Int, inp[1:7])

@show i
s = [parse(Int, c) for c in inp]

# len s = len(inp) - (i % length(inp)) + floor((10000 * length(inp) - i) / length(inp))
s = [s[i % length(inp) + 1:end];
     repeat(s, Int(floor(((10000 * length(inp)) - i) / length(inp))))]
@time for _ in 1:100
	phase(s)
end
@show s[1:8]
@show s[1:8] == [1, 9, 4, 2, 2, 5, 7, 5]
