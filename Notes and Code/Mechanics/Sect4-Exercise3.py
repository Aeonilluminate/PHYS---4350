import numpy as np
import matplotlib.pyplot as plt
import math

l=1
g = 9.81
m=1

def truethetaoft(t):
    th0=0.2
    k=math.sqrt(g/l)
    return th0*math.cos(k*t)

def trueomegaoft(t):
    th0=0.2
    k=math.sqrt(g/l)
    return -1*th0*k*math.sin(k*t)

def truekinetic(t):
    return 0.5*m*(l*trueomegaoft(t))**2

def truepotential(t):
    return m*g*(1-l*math.cos(truethetaoft(t)))

def truetotal(t):
    return (truekinetic(t)+truepotential(t))

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
KEpoints=[]
PEpoints=[]
TotalEpoints=[]
for t in tpoints:
    thetapoints.append(thetaold)
    omegapoints.append(omegaold)
    v=l*omegaold
    ke=0.5*m*v**2
    pe=m*g*(1-l*math.cos(thetaold))
    KEpoints.append(ke)
    PEpoints.append(pe)
    TotalEpoints.append(ke+pe)
    omeganew = omegaold - h*(g/l)*thetaold
    thetanew = thetaold + h*omegaold
    omegaold=omeganew
    thetaold=thetanew

plt.figure(1)
plt.plot(tpoints,KEpoints,lw=2, label="Kinetic Energy")
plt.plot(tpoints,PEpoints,lw=2, label="Potential Energy")
plt.plot(tpoints,TotalEpoints,lw=2, label="Total Energy")

plt.xlabel("time (s)")
plt.ylabel("Energy (J)")
plt.legend()
plt.title("Euler Solution")
plt.savefig("Euler.png")

plt.figure(2)
TKE=list(map(truekinetic,tpoints))
TPE=list(map(truepotential,tpoints))
TT=list(map(truetotal,tpoints))
plt.plot(tpoints,TKE,lw=2,label="Kinetic Energy")
plt.plot(tpoints,TPE,lw=2,label="Potential Energy")
plt.plot(tpoints,TT,lw=2,label="Total Energy")

plt.xlabel("time (s)")
plt.ylabel("Energy (J)")
plt.legend()
plt.title("True Solution")
plt.savefig("True.png")

#draw
plt.show()
