import numpy as np
import math
import matplotlib.pyplot as plt

#constants
v=0.5#speed
L=0.1#length of string
A=0.1#amplitude of initial displacement
h = 0.0001#time step

#number of grid points, 0-100 in increments of 1 is 101 points
n=101
#grid spacing
a = L/(n-1)

#make the grid
Phi = np.zeros(n,float)
Phinew = np.zeros(n,float)
beta = np.zeros(n,float)
betanew = np.zeros(n,float)
x = np.zeros(n,float)
for i in range(n):
    x[i] += i*a
    Phi[i] = A*math.sin(2*math.pi*x[i]/L)
#print(x,Phi)

#time
t=0.0
tend=0.75
#time values we want to plot
tplot = [0.002,0.1,0.7,0.72]

while t<tend:
    for i in range(n):
        if i==0 or i==n-1:#values on the boundaries are fixed
            Phinew[i] = Phi[i]
            betanew[i] = beta[i]
        else:
            Phinew[i] = Phi[i] + h*beta[i]
            betanew[i] = beta[i] + h*(v**2)*(Phi[i+1] - 2*Phi[i] + Phi[i-1])/(a**2)
    Phi=np.copy(Phinew)
    beta=np.copy(betanew)
    t+=h

    for j in range(len(tplot)):
        if abs(t-tplot[j])<h/1000:#if current time value is (very close) to one we want to plot
            s=str(round(tplot[j],3))+" s"
            plt.plot(x,Phi,lw=2,label=s)
plt.xlabel("x (m)")
plt.ylabel("Phi (m)")
plt.legend()
#plt.savefig("waveeqn-ftcs.png")
plt.show()



