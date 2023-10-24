import numpy as np
import matplotlib.pyplot as plt
import math

#define initial conditions and constants
x0=1
y0=0
z0=[0,0.001]
t0=0
tf=100
sigma=10
rparam=24.1
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
h=0.01
n=int((tf-t0)/h)

tpoints=np.linspace(t0,tf,n+1)
zpoints0=[]
zpoints1=[]
for j in range(2):
    r0=np.array([x0,y0,z0[j]],float)
    r=np.copy(r0)
    for t in tpoints:
        if j==0:
            zpoints0.append(r[2])
        else:
            zpoints1.append(r[2])
        k1=h*f(r,t)
        k2=h*f(r+k1/2,t+h/2)
        k3=h*f(r+k2/2,t+h/2)
        k4=h*f(r+k3,t+h)
        r += (1/6)*(k1+2*k2+2*k3+k4)

zdiff=np.zeros(len(tpoints))
for w in range(len(zdiff)):
    zdiff[w] = abs(zpoints1[w]-zpoints0[w])

plt.plot(tpoints,zdiff,lw=2)
plt.xlabel("time")
plt.ylabel(r'$\Delta$ z')
plt.title(r'$\Delta$ z vs t')
plt.yscale("log")

#draw
plt.show()
