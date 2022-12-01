import numpy as np
import matplotlib.pyplot as plt

from harmonic_oscillator import *

# Main program
params = {
    "ω" : 2*np.pi,
    "f0" : 1000.0,
    "ω0" : 10*np.pi,
    "β" : 0.5*np.pi,
    "x0" : 0.0,
    "v0" : 0.0
}

plt.clf()
t, x, v, _ = simulate_harmonic_oscillation(params, tfinal=5.0, NptsPlot=1000)
plt.plot(t, np.real(x), label="x(t)")

plt.legend()
plt.grid(True)
plt.savefig("IMG_cases_v4.png", dpi=150)

