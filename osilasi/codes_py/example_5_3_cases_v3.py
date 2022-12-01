import numpy as np
import matplotlib.pyplot as plt
import cmath

def calc_auxiliary_roots(ω0, β):
    r1 = -β + cmath.sqrt(β**2 - ω0**2)
    r2 = -β - cmath.sqrt(β**2 - ω0**2)
    return r1, r2

def simulate_harmonic_oscillation(params, tfinal=5.0, NptsPlot=1000):
    # Parameters are a dict
    ω = params["ω"]
    f0 = params["f0"]
    ω0 = params["ω0"]
    β = params["β"]
    # Initial conditions
    x0 = params["x0"]
    v0 = params["v0"]

    r1, r2 = calc_auxiliary_roots(ω0, β)

    print("\nr1 = ", r1)
    print("r2 = ", r2)

    # Handle special case of critically damped
    # we check ω0 and β instead of r1 and r2 as it is easier to do
    SMALL = 1e-10
    CRITICALLY_DAMPED = False
    if np.abs(ω0 - β) <= SMALL:
        print("Oscillation is critically damped")
        CRITICALLY_DAMPED = True

    FORCED_OSCILLATION = False
    if np.abs(f0) > SMALL:
        FORCED_OSCILLATION = True

    if ω0 > β:
        print("Oscillation is underdamped")

    if ω0 < β:
        print("Oscillation is overdamped")

    if β == 0:
        print("Oscillation is not damped")

    A2 = f0**2/( (ω0**2 - ω**2)**2 + 4*β**2 * ω**2 )
    A = np.sqrt(A2)

    δ = np.arctan2( 2*β*ω, ω0**2 - ω**2 )

    if not FORCED_OSCILLATION:
        cond = (np.abs(x0) < SMALL) and (np.abs(v0) < SMALL)
        if cond:
            print("WARNING: x0 and v0 are both close to zeros")

    # From Sympy
    if CRITICALLY_DAMPED:
        C1 = -A*np.cos(δ) + x0
        C2 = -A*ω*np.sin(δ) - A*ω0*np.cos(δ) + ω0*x0 + v0
    else:
        rb2w2 = cmath.sqrt(β**2 - ω0**2)
        denum = 2 * cmath.sqrt(β - ω0) * cmath.sqrt(β + ω0)
        C1 = -(A*β*np.cos(δ) + A*ω*np.sin(δ) + A * rb2w2 * np.cos(δ) - β*x0 - v0 - x0*rb2w2) / denum
        C2 =  (A*β*np.cos(δ) + A*ω*np.sin(δ) - A * rb2w2 * np.cos(δ) - β*x0 - v0 + x0*rb2w2) / denum

    print("C1 = ", C1)
    print("C2 = ", C2)

    t = np.linspace(0.0, tfinal, NptsPlot)
    f = f0*np.cos(ω*t)

    if CRITICALLY_DAMPED:
        x = A*np.cos(ω*t - δ) + C1*np.exp(r1*t) + C2*t*np.exp(r1*t)
        v = A*ω*np.sin(δ - ω*t) + C1*r1*np.exp(r1*t) + C2*r1*t*np.exp(r1*t) + C2*np.exp(r1*t)
    else:
        x = A*np.cos(ω*t - δ) + C1*np.exp(r1*t) + C2*np.exp(r2*t)
        v = A*ω*np.sin(δ - ω*t) + C1*np.exp(r1*t)*r1 + C2*np.exp(r2*t)*r2

    return t, x, v, f


# Main program
params_general = {
    "ω" : 2*np.pi,
    "f0" : 0.0,
    "ω0" : 2*np.pi,
    "β" : 0.0,
    "x0" : 1.0,
    "v0" : 0.0
}

import copy

# Underdamped
params = copy.copy(params_general)

plt.clf()

ω0 = params["ω0"]
for β in [0.1*ω0, 0.5*ω0, ω0, 2*ω0, 10*ω0]:
    params["β"] = β
    t, x, v, _ = simulate_harmonic_oscillation(params, tfinal=5.0, NptsPlot=2000)
    plt.plot(t, np.real(x), label="β={:.4f}".format(params["β"]))

plt.legend()
plt.grid(True)
plt.savefig("IMG_cases_v3_x.png", dpi=150)

