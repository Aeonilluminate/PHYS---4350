import numpy as np
import matplotlib.pyplot as plt
import math

#define initial conditions and constants
theta0=0.200
omega0=0
t0=0
tf=60
l=9.81
g = 9.81
BetaOverM = 0.5
F0overlm = [0,0.5,1.2,2]
kd=2/3
lb = [r'$F/\ell m=0$',r'$F/\ell m=0.5$',r'$F/\ell m=1.2$',r'$F/\ell m=2$']

def f(r,t,fom):
    theta=r[0]
    omega=r[1]
    ftheta=omega
    fomega=fom*math.sin(kd*t)-(g/l)*math.sin(theta) - BetaOverM*omega
    return np.array([ftheta,fomega],float)

# choose step size
h=0.04
n=int((tf-t0)/h)

tpoints=np.linspace(t0,tf,n+1)
for i in range(len(F0overlm)):
    thetapoints=[]
    omegapoints=[]
    r=np.array([theta0,omega0],float)
    for t in tpoints:
        thetapoints.append(r[0])
        omegapoints.append(r[1])
        k1=h*f(r,t,F0overlm[i])
        k2=h*f(r+k1/2,t+h/2,F0overlm[i])
        k3=h*f(r+k2/2,t+h/2,F0overlm[i])
        k4=h*f(r+k3,t+h,F0overlm[i])
        r += (1/6)*(k1+2*k2+2*k3+k4)
    plt.figure(1)
    plt.plot(tpoints,thetapoints,lw=2,label=lb[i])
    plt.figure(2)
    plt.plot(tpoints,omegapoints,lw=2,label=lb[i])

plt.figure(1)
plt.xlabel("time (s)")
plt.ylabel(r'$\theta$ (radians)')
plt.title("Driven Pendulum")
plt.legend()

plt.figure(2)
plt.xlabel("time (s)")
plt.ylabel(r'$\omega$ (radians/s)')
plt.title("Driven Pendulum")
plt.legend()

#draw
plt.show()
