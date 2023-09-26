import numpy as np
import matplotlib.pyplot as plt
import math

l=1
g = 9.81

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
    k1=h*f(r,t)
    k2=h*f(r+k1/2,t+h/2)
    k3=h*f(r+k2/2,t+h/2)
    k4=h*f(r+k3,t+h)
    r += (1/6)*(k1+2*k2+2*k3+k4)
plt.plot(tpoints,thetapoints,lw=4, label="RK4")

truepoints=list(map(truethetaoft,tpoints))
plt.plot(tpoints,truepoints,lw=2,label="true")

plt.xlabel("time (s)")
plt.ylabel(r'$\theta$ (radians)')
plt.legend()

#draw
plt.show()
