import numpy as np
import matplotlib.pyplot as plt
import math

#define initial conditions and constants
theta0=math.radians(90)
omega0=0
t0=0
tf=10
l=1
g = 9.81
print("Let beta=1 and consider different masses")
beta=1
BetaOverM = [beta/0.1, beta/0.2, beta/1, beta/10, beta/100]
lb = ['m=0.1','m=0.2','m=1','m=10','m=100']

def f(r,t,bom):
    theta=r[0]
    omega=r[1]
    ftheta=omega
    fomega=-(g/l)*math.sin(theta) - bom*omega
    return np.array([ftheta,fomega],float)

# choose step size
h=0.04
n=int((tf-t0)/h)

tpoints=np.linspace(t0,tf,n+1)
for i in range(len(BetaOverM)):
    thetapoints=[]
    omegapoints=[]
    r=np.array([theta0,omega0],float)
    for t in tpoints:
        thetapoints.append(r[0])
        omegapoints.append(r[1])
        k1=h*f(r,t,BetaOverM[i])
        k2=h*f(r+k1/2,t+h/2,BetaOverM[i])
        k3=h*f(r+k2/2,t+h/2,BetaOverM[i])
        k4=h*f(r+k3,t+h,BetaOverM[i])
        r += (1/6)*(k1+2*k2+2*k3+k4)
    plt.plot(tpoints,thetapoints,lw=2,label=lb[i])

plt.xlabel("time (s)")
plt.ylabel(r'$\theta$ (radians)')
plt.title(r'With Damping, fixed $\beta$')
plt.legend()
plt.savefig("ex4.png")

#draw
plt.show()
