import numpy as np
import matplotlib.pyplot as plt
import math

#define initial conditions and constants
r0=np.array([0,1,0],float)
t0=0
tf=400
sigma=10
rparam=25
b=8/3

def f(r,t):
    x=r[0]
    y=r[1]
    z=r[2]
    fx=sigma*(y-x)
    fy=rparam*x-y-x*z
    fz=x*y-b*z
    return np.array([fx,fy,fz],float)

# choose step size
h=0.0001
n=int((tf-t0)/h)

tpoints=np.linspace(t0,tf,n+1)
ypoints=[]
zpoints=[]
r=np.copy(r0)
for t in tpoints:
    if t>30:
        if abs(r[0])<0.01:
            ypoints.append(r[1])
            zpoints.append(r[2])
    k1=h*f(r,t)
    k2=h*f(r+k1/2,t+h/2)
    k3=h*f(r+k2/2,t+h/2)
    k4=h*f(r+k3,t+h)
    r += (1/6)*(k1+2*k2+2*k3+k4)


plt.plot(ypoints,zpoints,lw=0,marker="o",markersize=1)
plt.xlabel("y")
plt.ylabel("z")
plt.title("Phase space, z vs y")
plt.ylim(0,30)
plt.savefig("LorenzAttractor.png")


#draw
plt.show()
