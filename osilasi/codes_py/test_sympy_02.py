from sympy import *

C1 = symbols("C_1")
C2 = symbols("C_2")

ω0 = symbols("omega_0", real=True, positive=True)
t = symbols("t", real=True)

xt = C1*exp(I*ω0*t) + C2*exp(-I*ω0*t)
vt = diff(xt, t, 1)

# Initial conditions (numerical)
x0 = 1.0
v0 = 0.1
# x0 and v0 cannot be both 0.0

eqn1 = Equality( xt.subs({t: 0.0}), x0 )
eqn2 = Equality( vt.subs({t: 0.0}), v0 )

sols = solve([eqn1, eqn2], [C1, C2])
print("sols = ")
pprint(sols)

import numpy as np
import matplotlib.pyplot as plt

ω0_num = 2*np.pi
T0_num = 2*np.pi/ω0_num # period or cycle
NptsPlot = 1000
t_array = np.linspace(0.0, 4*T0_num, NptsPlot)
x_array = np.zeros(NptsPlot, dtype=np.complex128)
v_array = np.zeros(NptsPlot, dtype=np.complex128)

dict_subs = {C1: sols[C1], C2: sols[C2], ω0: ω0_num}
xt_eval = xt.subs(dict_subs)
vt_eval = vt.subs(dict_subs)

for i in range(NptsPlot):
    xx = xt_eval.subs({t: t_array[i]})
    x_array[i] = np.complex128(xx)
    vv = vt_eval.subs({t: t_array[i]})
    v_array[i] = np.complex128(vv)

plt.clf()
plt.plot(t_array, np.real(x_array), label="x(t)")
plt.plot(t_array, np.real(v_array), label="v(t)")
plt.legend()
plt.grid(True)
plt.savefig("IMG_simple_01.png", dpi=150)
