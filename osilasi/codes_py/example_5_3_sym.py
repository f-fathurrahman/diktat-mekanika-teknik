from sympy import *

C1 = symbols("C_1")
C2 = symbols("C_2")
t = symbols("t", real=True)

ω = symbols("omega", real=True, positive=True)
ω0 = symbols("omega_0", real=True, positive=True)
ω1 = symbols("omega_1", real=True, positive=True)

β = symbols("beta", real=True, positive=True)

A = symbols("A", real=True)
δ = symbols("delta", real=True)

B1 = symbols("B_1")
B2 = symbols("B_2")

xt = A*cos(ω*t - δ) + exp(-β*t) * ( B1*cos(ω1*t) + B2*sin(ω1*t) )
vt = diff(xt, t, 1)

# Initial conditions (symbolic)
x0 = symbols("x_0", real=True)
v0 = symbols("v_0", real=True)

eqn1 = Equality( xt.subs({t: 0.0}), x0 )
eqn2 = Equality( vt.subs({t: 0.0}), v0 )

sols = solve([eqn1, eqn2], [B1, B2])
print("sols = ")
pprint(sols)

print(sols)