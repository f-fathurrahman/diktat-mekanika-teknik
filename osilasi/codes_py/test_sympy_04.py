from sympy import *

A = symbols("A")
δ = symbols("delta")

ω0 = symbols("omega_0", real=True, positive=True)
t = symbols("t", real=True)

xt = A*cos(ω0*t - δ)
vt = diff(xt, t, 1)

# Initial conditions (symbolic)
x0 = symbols("x_0", real=True)
v0 = symbols("v_0", real=True)

eqn1 = Equality( xt.subs({t: 0.0}), x0 )
eqn2 = Equality( vt.subs({t: 0.0}), v0 )

sols = solve([eqn1, eqn2], [A, δ])
print("sols = ")
pprint(sols)
