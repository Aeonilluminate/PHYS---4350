import numpy as np
import math
import matplotlib.pyplot as plt

a = 5.0
b = 0.05

def f(x, t):
    return a*x - b*x**2

t0, tf = 0, 5
N = 25
h = (tf - t0)/N
x_euler, x_rk4 = 2.0, 2.0

T = np.arange(t0, tf, h)
X_EULER = []
X_RK4 = []

for t in T:
    X_EULER.append(x_euler)
    x_euler += h*f(x_euler,t)

    X_RK4.append(x_rk4)
    k1 = h*f(x_rk4,t)
    k2 = h*f(x_rk4 + 0.5*k1, t + 0.5*h)
    k3 = h*f(x_rk4 + 0.5*k2, t + 0.5*h)
    k4 = h*f(x_rk4 + k3, t + h)
    x_rk4 += (k1 + 2*k2 + 2*k3 + k4)/6


fig, (EULER, RK4) = plt.subplots(nrows = 2, ncols = 1, sharex = True)

EULER.set_title("Euler's Method")
EULER.set_xlabel('t')
EULER.set_ylabel('N(t)')
EULER.plot(T, X_EULER)

RK4.set_title("Fourth-order Runge-Kutta Method")
RK4.set_xlabel('t')
RK4.set_ylabel('N(t)')
RK4.plot(T, X_RK4)

plt.style.use('seaborn')
plt.tight_layout()

plt.show()