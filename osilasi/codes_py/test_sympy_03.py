from sympy import *

B1 = symbols("B_1")
B2 = symbols("B_2")

ω0 = symbols("omega_0", real=True, positive=True)
t = symbols("t", real=True)

xt = B1*cos(ω0*t) + B2*sin(ω0*t)
vt = diff(xt, t, 1)

# Initial conditions (symbolic)
x0 = symbols("x_0", real=True)
v0 = symbols("v_0", real=True)

eqn1 = Equality( xt.subs({t: 0.0}), x0 )
eqn2 = Equality( vt.subs({t: 0.0}), v0 )

sols = solve([eqn1, eqn2], [B1, B2])
print("sols = ")
pprint(sols)
