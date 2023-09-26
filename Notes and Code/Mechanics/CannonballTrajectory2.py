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
thetadeg=[30.,35.,40.,45.,50.,55.]
theta=np.radians(thetadeg)

plt.figure(1)
print("Trajectory with constant air density")


for i in range(len(theta)):
    xi=x0
    yi=y0
    vix=v0*math.cos(theta[i])
    viy=v0*math.sin(theta[i])
    vi=v0
    ti=t0
    xpoints=[]
    ypoints=[]
    while yi>-0.1:
        xpoints.append(xi)
        ypoints.append(yi)
        xi += h*vix
        yi += h*viy
        vix += -h*DoverM*vi*vix
        viy += -h*g - h*DoverM*vi*viy
        vi = math.sqrt(vix**2 + viy**2)
    s=str(thetadeg[i])+"$^{\circ}$"
    plt.plot(xpoints,ypoints,label=s,lw=2)

plt.legend() 
plt.xlabel("x(t), Horizontal position (m)")
plt.ylabel("y(t), Vertical position (m)")
plt.title("Constant air density")
plt.xlim(-1000,27000)
plt.legend()

plt.figure(2)
print("Trajectory with variable air density")

def fD(y):
    kappa = 1e-4
    DoverM=4e-5
    return DoverM*math.exp(-kappa*y)

for i in range(len(theta)):
    xold=x0
    yold=y0
    vxold=v0*math.cos(theta[i])
    vyold=v0*math.sin(theta[i])
    vold=v0
    xpoints=[]
    ypoints=[]
    while yold>-0.1:
        xpoints.append(xold)
        ypoints.append(yold)
        xnew = xold + h*vxold
        ynew = yold + h*vyold
        vxnew = vxold -h*fD(yold)*vold*vxold
        vynew = vyold -h*g - h*fD(yold)*vold*vyold
        vnew = math.sqrt(vxnew**2 + vynew**2)
        xold=xnew
        yold=ynew
        vxold=vxnew
        vyold=vynew
        vold=vnew
    s=str(thetadeg[i])+"$^{\circ}$"
    plt.plot(xpoints,ypoints,label=s,lw=2)

plt.legend() 
plt.xlabel("x(t), Horizontal position (m)")
plt.ylabel("y(t), Vertical position (m)")
plt.title("Variable air density")
plt.xlim(-1000,27000)
plt.legend()


#draw
plt.show()
