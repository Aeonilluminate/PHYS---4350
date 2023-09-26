import numpy as np
import matplotlib.pyplot as plt
import math

l=1
g = 9.81

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

thetaold=theta0
omegaold=omega0
thetanew=0
omeganew=0
tpoints=np.linspace(t0,tf,n+1)
thetapoints=[]
omegapoints=[]
for t in tpoints:
    thetapoints.append(thetaold)
    omegapoints.append(omegaold)
    omeganew = omegaold - h*(g/l)*thetaold
    thetanew = thetaold + h*omegaold
    omegaold=omeganew
    thetaold=thetanew

plt.figure(1)
plt.plot(tpoints,thetapoints,lw=2, label="Euler")

truepoints=list(map(truethetaoft,tpoints))
plt.plot(tpoints,truepoints,lw=2,label="true")


plt.xlabel("time (s)")
plt.ylabel(r'$\theta$ (radians)')
plt.legend()

plt.figure(2)
plt.plot(tpoints,omegapoints,lw=2)
plt.xlabel("time (s)")
plt.ylabel(r'$\omega$, angular velocity (rad/s)')

#draw
plt.show()
