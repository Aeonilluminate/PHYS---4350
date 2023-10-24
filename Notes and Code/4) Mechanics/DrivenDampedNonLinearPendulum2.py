import numpy as np
import matplotlib.pyplot as plt
import math

#define initial conditions and constants
theta0=[0.2,0.201]
omega0=0
t0=0
tf=100
l=9.81
g = 9.81
BetaOverM = 0.5
F0overlm = 1.2
kd=2/3
lb = [r'$\theta_0=0.200$',r'$\theta_0=0.201$']

def f(r,t):
    theta=r[0]
    omega=r[1]
    ftheta=omega
    fomega=F0overlm*math.sin(kd*t)-(g/l)*math.sin(theta) - BetaOverM*omega
    return np.array([ftheta,fomega],float)

# choose step size
h=0.04
n=int((tf-t0)/h)

tpoints=np.linspace(t0,tf,n+1)
for i in range(len(theta0)):
    thetapoints=[]
    omegapoints=[]
    r=np.array([theta0[i],omega0],float)
    for t in tpoints:
        thetapoints.append(r[0])
        omegapoints.append(r[1])
        k1=h*f(r,t)
        k2=h*f(r+k1/2,t+h/2)
        k3=h*f(r+k2/2,t+h/2)
        k4=h*f(r+k3,t+h)
        r += (1/6)*(k1+2*k2+2*k3+k4)
    plt.plot(tpoints,thetapoints,lw=2,label=lb[i])

plt.xlabel("time (s)")
plt.ylabel(r'$\theta$ (radians)')
plt.title("Driven Pendulum")
plt.legend()


#draw
plt.show()
