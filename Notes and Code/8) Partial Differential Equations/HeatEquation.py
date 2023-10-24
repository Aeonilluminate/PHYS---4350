import numpy as np
import math
import matplotlib.pyplot as plt

#constants
Thot=50#temp on top
Tcold=0#temp on bottom
Tini=20#inital temp of the interior steel
D = 4.25e-6#thermal diffusivity
L=0.01#thickness of steel
h = 0.0001#time step

#number of grid points, 0-100 in increments of 1 is 101 points
n=101
#grid spacing
a = L/(n-1)

#make the grid
T = np.zeros(n,float)
Tnew = np.zeros(n,float)
x = np.zeros(n,float)
for i in range(n):
    T[i] = Tini
    x[i] += i*a
T[0] = Tcold#bottom
T[n-1] = Thot#top

#time
t=0.0
tend=10.1
#time values we want to plot
tplot = [0.01,0.1,0.4,1.0,10.0]

while t<tend:
    for i in range(n):
        if i==0 or i==n-1:#values on the boundaries are fixed
            Tnew[i] = T[i]
        else:
            Tnew[i] = T[i] + h*D*(T[i+1] - 2*T[i] + T[i-1])/(a**2)
    T=np.copy(Tnew)
    t+=h

    for j in range(len(tplot)):
        if abs(t-tplot[j])<h/1000:#if current time value is (very close) to one we want to plot
            s=str(round(tplot[j],2))+" s"
            plt.plot(x,T,lw=2,label=s)
plt.xlabel("x (m)")
plt.ylabel("T (degrees C)")
plt.legend()
plt.show()



