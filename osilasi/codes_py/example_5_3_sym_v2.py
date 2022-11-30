from sympy import *

t = symbols("t", real=True)

ω = symbols("omega", real=True, positive=True)
ω0 = symbols("omega_0", real=True, positive=True)
ω1 = symbols("omega_1", real=True, positive=True)

β = symbols("beta", real=True, positive=True)

A = symbols("A", real=True)
δ = symbols("delta", real=True)

C1 = symbols("C_1")
C2 = symbols("C_2")

r1 = -β + sqrt(β**2 - ω0**2)
r2 = -β - sqrt(β**2 - ω0**2)

# General case for two different r1 and r2
xt = A*cos(ω*t - δ) + C1*exp(r1*t) + C2*exp(r2*t)

vt = diff(xt, t, 1)

# Initial conditions (symbolic)
x0 = symbols("x_0", real=True)
v0 = symbols("v_0", real=True)


eqn1 = Equality( xt.subs({t: 0.0}), x0 )
eqn2 = Equality( vt.subs({t: 0.0}), v0 )

#dict_nums = {
#    A: 1.0,
#    ω: 1.0,
#    ω0: 1.1,
#    β: 1.0,
#    δ: 0.0,
#    x0: 0.0,
#    v0: 0.0,
#}
#eqn1 = eqn1.subs(dict_nums)
#eqn2 = eqn2.subs(dict_nums)

print("eqn1 = ", eqn1)
print("eqn2 = ", eqn2)

sols = solve([eqn1, eqn2], [C1, C2])
print("sols = ")
pprint(sols)
print(sols)