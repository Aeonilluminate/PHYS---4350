import numpy as np
import matplotlib.pyplot as plt
import math

#define constant
g = 9.81

#define initial conditions
y0=3000
v0=0
t0=0

#choose end point
tf=15

# choose step size
h=0.1
n = int((tf-t0)/h+1)

tpoints=np.linspace(t0,tf,n)
vpoints=[]
ypoints=[]

truey = y0 - 0.5*g*tpoints**2
truev = -g*tpoints

yi=y0
vi=v0
for ti in tpoints:
    vpoints.append(vi)
    ypoints.append(yi)
    yi += h*vi#have to calculate this first because it depends on previous vi
    vi += -h*g
    
plt.figure(1)

plt.plot(tpoints,ypoints,label="Euler",lw=6)
plt.plot(tpoints,truey,label="true",lw=2)
plt.xlabel("t, time (s)")
plt.ylabel("y(t), height (m)")
plt.title("Height vs time, no air resistance")
plt.legend()

plt.figure(2)

plt.plot(tpoints,vpoints,label="Euler",lw=6)
plt.plot(tpoints,truev,label="true",lw=2)
plt.xlabel("t, time (s)")
plt.ylabel("v(t), speed (m)")
plt.title("Speed vs time, no air resistance")
plt.legend()

#draw
#plt.savefig("Euler.png")
plt.show()
