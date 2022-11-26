from sympy import *

C1 = symbols("C_1")
C2 = symbols("C_2")

ω0 = symbols("omega_0", real=True, positive=True)
t = symbols("t", real=True)

xt = C1*exp(I*ω0*t) + C2*exp(-I*ω0*t)
vt = diff(xt, t, 1)

# Initial conditions (symbolic)
x0 = symbols("x_0", real=True)
v0 = symbols("v_0", real=True)

# Initial conditions (numerical)
#x0 = 1.0
#v0 = 0.0
# x0 and v0 cannot be both 0.0

eqn1 = Equality( xt.subs({t: 0.0}), x0 )
eqn2 = Equality( vt.subs({t: 0.0}), v0 )

sols = solve([eqn1, eqn2], [C1, C2])
print("sols = ")
pprint(sols)
