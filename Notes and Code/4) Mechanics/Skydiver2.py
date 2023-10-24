import numpy as np
import matplotlib.pyplot as plt
import math

#define constant
g = 9.81

#define initial conditions
y0=3000
v0=0
t0=0
D=0.4
m=80

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
    vi += -h*g + h*D*(vi**2)/m
    
plt.figure(1)

plt.plot(tpoints,ypoints,label="w/ air resistance",lw=2)
plt.plot(tpoints,truey,label="no air resistance",lw=2)
plt.xlabel("t, time (s)")
plt.ylabel("y(t), height (m)")
plt.title("Height vs time")
plt.legend()

plt.figure(2)

plt.plot(tpoints,vpoints,label="w/ air resistance",lw=2)
plt.plot(tpoints,truev,label="no air resistance",lw=2)
plt.xlabel("t, time (s)")
plt.ylabel("v(t), speed (m)")
plt.title("Speed vs time")
plt.legend()

#draw
plt.show()
