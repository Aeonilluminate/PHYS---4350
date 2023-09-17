import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G = 9.81 # m/s^2

MASS = 1.0 # kg
v0 = 10.0 
THETA = math.radians(45)
v0x, v0y = v0*math.cos(THETA), v0*math.sin(THETA)

def Acceleration(t):
    return [0.0, -G, 0.0]

def Velocity(t):
    return [v0x, -G*t + v0y, 0.0]

def Position(t):
    return [v0x*t, -0.5*G*t**2 + v0y*t, 0.0]


t, dt = 0.0, 1e-3
T = [t]
                  
A = [Acceleration(t)]
V = [Velocity(t)]
R = [Position(t)]

i = 0
while R[i][1] > 0 or i < 1:
    t += dt
    T.append(t)

    A.append(Acceleration(t))
    V.append(Velocity(t))
    R.append(Position(t))

    i += 1

fig, ax = plt.subplots()

ax.set(xlim = (0 - 1, R[-1][0] + 1), ylim = (0 - 1, max([e[1] for e in R]) + 1))
line, = ax.plot([], [])

def animate(i):
    line.set_data([e[0] for e in R[:i]], [e[1] for e in R[:i]])
    return line,

anim = FuncAnimation(fig, animate, frames=len(R) + 1, interval=6)
plt.show()