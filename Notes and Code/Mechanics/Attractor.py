import numpy as np
import matplotlib.pyplot as plt
import math

#define initial conditions and constants
theta0=[0.200,0.201]
omega0=0
t0=0
tf=15000
l=9.81
g = 9.81
BetaOverM = 0.5
F0overlm = [0.5,1.2]
kd=2/3
lb = [[r'$F/\ell m=0.5$,$\theta_0=0.200$',r'$F/\ell m=0.5$,$\theta_0=0.201$'],[r'$F/\ell m=1.2$, $\theta_0=0.200$',r'$F/\ell m=1.2$, $\theta_0=0.201$']]

def f(r,t,fom):
    theta=r[0]
    omega=r[1]
    ftheta=omega
    fomega=fom*math.sin(kd*t)-(g/l)*math.sin(theta) - BetaOverM*omega
    return np.array([ftheta,fomega],float)

# choose step size
h=0.04
n=int((tf-t0)/h)
T = 2*math.pi/kd

figcount=1
tpoints=np.linspace(t0,tf,n+1)
for i in range(len(F0overlm)):
    for j in range(len(theta0)):
        thetapoints=[]
        omegapoints=[]
        r=np.array([theta0[j],omega0],float)
        for t in tpoints:
            if t>30:
                m=int(t/T)
                if abs(t-m*T)<0.01:
                    thetapoints.append(r[0])
                    omegapoints.append(r[1])
            k1=h*f(r,t,F0overlm[i])
            k2=h*f(r+k1/2,t+h/2,F0overlm[i])
            k3=h*f(r+k2/2,t+h/2,F0overlm[i])
            k4=h*f(r+k3,t+h,F0overlm[i])
            r += (1/6)*(k1+2*k2+2*k3+k4)
            if r[0]<-math.pi:
                r[0]+=2*math.pi
            if r[0]>math.pi:
               r[0]-=2*math.pi 
        plt.figure(figcount)
        plt.plot(thetapoints,omegapoints,lw=0,marker="o",markersize=1)
        plt.xlabel(r'$\theta$ (radians)')
        plt.ylabel(r'$\omega$ (radians/s)')
        plt.title(lb[i][j])
        if figcount==1 or figcount==2:
            plt.xlim(-1,1)
            plt.ylim(-1,1)
        figcount+=1

#draw
plt.show()
