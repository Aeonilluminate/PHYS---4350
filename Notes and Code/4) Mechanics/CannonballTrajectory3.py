import numpy as np
import matplotlib.pyplot as plt
import math


#define initial conditions and constants
x0=0
y0=0
v0=700
t0=0
g = 9.81
DoverM=4e-5

# choose step size
h=0.1

#a series of different launch angles
thetadeg=45.
theta=np.radians(thetadeg)

#function for variable air density
def fD(y):
    kappa = 1e-4
    DoverM=4e-5
    return DoverM*math.exp(-kappa*y)

#no wind and head or tail wind of 4.5 m/s
vwind=[-4.5,0,4.5]
windlabel=["4.5 m/s head wind","no wind","4.5 m/s tail wind"]

for i in range(len(vwind)):
    xold=x0
    yold=y0
    vxold=v0*math.cos(theta)
    vyold=v0*math.sin(theta)
    vpa=math.sqrt((vxold-vwind[i])**2 + vyold**2)
    xpoints=[]
    ypoints=[]
    while yold>-0.1:
        xpoints.append(xold)
        ypoints.append(yold)
        xnew = xold + h*vxold
        ynew = yold + h*vyold
        vxnew = vxold -h*fD(yold)*vpa*(vxold-vwind[i])
        vynew = vyold -h*g - h*fD(yold)*vpa*vyold
        xold=xnew
        yold=ynew
        vxold=vxnew
        vyold=vynew
        vpa=math.sqrt((vxold-vwind[i])**2 + vyold**2)
    print("range with vwind = ",vwind[i],":",round(xold))
    s=windlabel[i]
    plt.plot(xpoints,ypoints,label=s,lw=2)

plt.legend() 
plt.xlabel("x(t), Horizontal position (m)")
plt.ylabel("y(t), Vertical position (m)")
plt.title("Effect of wind")
plt.xlim(12000,28000)
plt.legend()


#draw
plt.show()
