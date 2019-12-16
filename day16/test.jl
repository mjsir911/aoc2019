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

function phase(l::Vector{Int})
	ret = Vector{Int}(undef, length(l))
	runsum::Int = 0
	for (i, thing) in Iterators.take(Iterators.reverse(enumerate(l)), Int(floor(length(l)/2)))
		runsum += thing
		runsum %= 10
		ret[i] = runsum
	end
	return ret
end



inp = readline()
s = [parse(Int, c) for c in inp]

s = repeat(s, 10000)
i = parse(Int, inp[1:7])
for _ in 1:100
	global s
	s = phase(s)
	@show s[i+1:i+8]
end
