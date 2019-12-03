#!/usr/bin/env julia


function piecewise(m::Dict{Function,Function}, default=x -> throw(DomainError(x)))
	return x -> get(Dict(map(f -> Pair(first(f)(x), last(f)), collect(m))), true, default)(x)
end


r = [1,0,0,0,99]
# x = r[1] + r[2]
# x ∈ {1, 100, 0}
f1(x) = x

r = [1,1,1,4,99,5,6,0,99]
# x = r[1] + r[2]
# x ∈ {1, 2, 99}
f2 = piecewise(Dict(
	(x -> x==1 ) => (x -> 5 + 6),
	(x -> x==2 ) => (x -> 5 * 6),
	(x -> x==99) => (x -> 1),
))
# println(f2(99))

r = Array{Union{Int,Symbol}}(map(x -> parse(Int, x), split(readline(), ",")))
r[2] = :n
r[3] = :v
@show r

opcodes = Dict(
	1 => +,
	2 => *,
	99 => !
)

function thing(op, arg1, arg2, dest)
	if typeof(arg1) == Int
		arg1 += 1
	end
	if typeof(arg2) == Int
		arg2 += 1
	end
	if typeof(dest) == Int
		dest += 1
	end
	return :(r[$(dest)] = $(opcodes[op])(r[$(arg1)], r[$(arg2)]))
end

solution = Expr(:toplevel, Iterators.map(l -> thing(l...), Iterators.filter(l -> length(l) == 4, Iterators.partition(r, 4)))...)

function expand(e::Expr, l::Dict{Expr,Expr})
	if haskey(l, e)
		e = l[e]
		Expr(e.head, e.args[1], (e.args[2:end] |> args -> map(arg -> expand(arg, l), args))...)
	else
		e
	end
end

dep = Dict(solution.args |> s -> map(a -> Pair(a.args...), s))


# this could all be done with a symbolic library, but I want to do it myself
import Base: +,*
+(a::Int, b::Symbol) = if a == 0 b else Expr(:call, :+, a, b) end
+(a::Symbol, b::Int) = +(b, a)

*(a::Int, b::Symbol) = if a == 1 b else Expr(:call, :*, a, b) end
*(a::Symbol, b::Int) = *(b, a)


+(a::Int, b::Expr) = 
if a == 0 b 
elseif b.args[1] == :+ Expr(:call, :+, reduce(+, vcat(a, filter(s -> typeof(s) == Int, b.args[2:end]))), filter(s -> typeof(s) != Int, b.args[2:end])...)
else Expr(:call, :+, a, b) end
+(a::Expr, b::Int) = +(b, a)

+(a::Symbol, b::Expr) = if b.args[1] == :+ Expr(:call, :+, a, b.args[2:end]...) else Expr(:call, :+, a, b) end
+(a::Expr, b::Symbol) = +(b, a)

*(a::Int, b::Expr) = 
if a == 1 b 
elseif b.args[1] == :* Expr(:call, :*, reduce(*, vcat(a, filter(s -> typeof(s) == Int, b.args[2:end]))), filter(s -> typeof(s) != Int, b.args[2:end])...)
elseif b.args[1] == :+ Expr(:call, :+, (a * b.args[2:end])...)
else Expr(:call, :*, a, b) end
*(a::Expr, b::Int) = *(b, a)

function realize(expr::Expr)
	function find_freev(expr::Expr)
		vcat(filter(s -> typeof(s) == Symbol, expr.args[2:end]), foldl(vcat, map(find_freev, filter(e -> typeof(e) == Expr, expr.args[2:end])), init=[]))
	end
	freev = find_freev(expr)
	eval(Expr(:function, Expr(:tuple, Expr(:parameters, freev...)), Expr(:block, expr)))
end

@show f = realize(@show eval(expand(:(r[1]), dep)))
@show f(n=12, v=2)

# x = r[1] + r[2]
#=
some more rules:
the destination operator never modifies future instructions
thats a party poopr

	3	1	0	2
0	r[3] =	r[0]	+	r[0]
4	r[3] =	r[1]	+	r[2]
8	r[3] =	r[3]	+	r[4]
16	r[3] =	r[5]	+	r[0]
20	r[19] =	r[1]	*	r[13]
24	r[23] =	r[9]	+	r[19]
28	r[27] =	r[6]	+	r[23]
32	r[31] =	r[27]	*	r[9]
36	r[35] =	r[6]	*	r[31]
40	r[39] =	r[5]	+	r[35]
44	r[43] =	r[10]	+	r[39]
48	r[47] =	r[43]	+	r[13]
52	r[51] =	r[47]	+	r[9]
56	r[55] =	r[51]	+	r[9]
62	r[59] =	r[55]	+	r[9]
66	r[63] =	r[9]	*	r[59]
	r[67] =	r[9]	*	r[63]
	r[71] =	r[5]	+	r[67]
	r[75] =	r[13]	*	r[71]
	r[79] =	r[6]	+	r[75]
	r[83] =	r[10]	+	r[79]
	r[87] =	r[6]	*	r[83]
	r[91] =	r[87]	+	r[5]
	r[95] =	r[91]	+	r[9]
	r[99] =	r[95]	+	r[10]
	r[103] =	r[9]	*	r[99]
	r[107] =	r[5]	+	r[103]
	r[111] =	r[5]	+	r[107]
	r[115] =	r[111]	*	r[10]
	r[119] =	r[6]	+	r[115]
	r[123] =	r[10]	*	r[119]
	r[127] =	r[6]	+	r[123]
	r[131] =	r[127]	+	r[5]
	r[135] =	r[9]	*	r[131]
	r[139] =	r[5]	+	r[135]
	r[143] =	r[139]	+	r[10]
	r[147] =	r[143]	+	r[2]
	r[0] =	r[147]	+	r[5]
	r[14] =	r[2]	END	r[0]
	r[] =	r[]		r[]

=#
