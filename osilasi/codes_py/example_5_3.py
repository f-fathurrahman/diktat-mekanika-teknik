import numpy as np
import matplotlib.pyplot as plt

ω = 2*np.pi
ω0 = 5*ω
β = ω0/20
f0 = 1000

# Period
τ = 2*np.pi/ω

# Pers. 5.64
A2 = f0**2/( (ω0**2 - ω**2)**2 + 4*β**2 * ω**2 )
A = np.sqrt(A2)
print("A = ", A)

δ = np.arctan( 2*β*ω/(ω0**2 - ω**2) )
print("δ = ", δ)

ω1 = np.sqrt(ω0**2 - β**2)

# Initial conditions
x0 = 0.0
v0 = 0.0

# From book
#B1 = x0 - A*np.cos(δ)
#B2 = ( v0 - ω*A*np.sin(δ) + β*B1 ) / ω1

# From Sympy
B1 = -A*np.cos(δ) + x0
B2 = (-A*ω*np.sin(δ) - β*(A*np.cos(δ) - x0) + v0)/ω1

print("B1 = ", B1)
print("B2 = ", B2)

t = np.linspace(0.0, 5.0, 1000)
f = f0*np.cos(ω*t)
x = A*np.cos(ω*t - δ) + np.exp(-β*t) * ( B1*np.cos(ω1*t) + B2*np.sin(ω1*t) )

plt.clf()
plt.plot(t, f/1000, label="driving force (scaled by 1000)")
plt.plot(t, x, label="displacement")
plt.legend()
plt.grid(True)
plt.savefig("IMG_example_5_3.png", dpi=150)

