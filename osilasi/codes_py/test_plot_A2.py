import numpy as np
import matplotlib.pyplot as plt

f0 = 1.0
ω0 = 1.0

ω_grid = np.linspace(0.0, 2.5*ω0, 1000)

plt.clf()

for sc in [0.1, 0.2, 0.3]:
    β = sc*ω0
    A2 = f0**2/( (ω0**2 - ω_grid**2)**2 + 4*β**2 * ω_grid**2 )
    str_label = "β={:.1f}ω0".format(sc)
    plt.plot(ω_grid, A2, label=str_label)

plt.grid(True)
plt.legend()
plt.savefig("IMG_Taylor_5_17.pdf")

