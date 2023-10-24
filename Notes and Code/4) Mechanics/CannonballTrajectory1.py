import numpy as np
import matplotlib.pyplot as plt
import math


#define initial conditions and constants
x0=0
y0=0
v0=700
t0=0
g = 9.81


# choose step size
h=0.1

#a series of different launch angles
thetadeg=[30.,35.,40.,45.,50.,55.]
theta=np.radians(thetadeg)

print("First, let's consider no air resistance, i.e. D=0")
DoverM=0
plt.figure(1)

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
plt.title("No air resistance")
plt.legend()



print("Now including air resistance, with D/m = 4e-5")
DoverM=4e-5
plt.figure(2)

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
plt.title("With air resistance")
plt.legend()


#draw
plt.show()
