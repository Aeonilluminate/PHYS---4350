import numpy as np
import matplotlib.pyplot as plt
import math

#define initial conditions and constants
theta0=0.200
omega0=0
t0=0
tf=[20,150]
l=1
g = 9.81
BetaOverM = [1,0.1]
F0overlm = 0.2
k=math.sqrt(g/l)
print("Natural frequency, k = ",k)
kd=[2,k*1.01]
lb = [r'$k_d=2<k$',r'$k_d=1.01*k$']
amp=F0overlm/math.sqrt((k**2-kd[1]**2)**2 + (BetaOverM[1]*kd[1])**2)
print("Amplitude at resonance: ",amp)

def f(r,t,od,bom):
    theta=r[0]
    omega=r[1]
    ftheta=omega
    fomega=F0overlm*math.sin(od*t)-(g/l)*theta - bom*omega
    return np.array([ftheta,fomega],float)

# choose step size
h=0.04

for i in range(len(kd)):
    n=int((tf[i]-t0)/h)
    tpoints=np.linspace(t0,tf[i],n+1)
    thetapoints=[]
    omegapoints=[]
    r=np.array([theta0,omega0],float)
    for t in tpoints:
        thetapoints.append(r[0])
        omegapoints.append(r[1])
        k1=h*f(r,t,kd[i],BetaOverM[i])
        k2=h*f(r+k1/2,t+h/2,kd[i],BetaOverM[i])
        k3=h*f(r+k2/2,t+h/2,kd[i],BetaOverM[i])
        k4=h*f(r+k3,t+h,kd[i],BetaOverM[i])
        r += (1/6)*(k1+2*k2+2*k3+k4)
    plt.figure(i+1)
    plt.plot(tpoints,thetapoints,lw=2)
    plt.xlabel("time (s)")
    plt.ylabel(r'$\theta$ (radians)')
    plt.title(lb[i])
    if i==1:
        plt.axhline(y=amp,color="red")
        plt.axhline(y=-amp,color="red")



#draw
plt.show()
