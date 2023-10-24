import numpy as np
import matplotlib.pyplot as plt
import math

g=9.81
l=1

def f(r,t):
    theta=r[0]
    omega=r[1]
    ftheta=omega
    fomega=-(g/l)*theta
    return np.array([ftheta,fomega],float)

def truethetaoft(t):
    th0=0.2
    k=math.sqrt(g/l)
    return th0*math.cos(k*t)

#define initial conditions and constants
theta0=0.2
omega0=0
t0=0
tf=10

# choose step size
h=0.04
n=int((tf-t0)/h)

tpoints=np.linspace(t0,tf,n+1)
thetapoints=[]
omegapoints=[]
r=np.array([theta0,omega0],float)
for t in tpoints:
    thetapoints.append(r[0])
    omegapoints.append(r[1])
    r += h*f(r,t)
plt.plot(tpoints,thetapoints,lw=2, label="Euler")

truepoints=list(map(truethetaoft,tpoints))
plt.plot(tpoints,truepoints,lw=2,label="true")

plt.xlabel("time (s)")
plt.ylabel(r'$\theta$ (radians)')
plt.legend()

#draw
plt.show()
