import random as rd
import matplotlib.pyplot as plt
import numpy as np
import math

nsteps=100
p=0.5
nwalkers=500

rav=np.zeros(nsteps)
r2av=np.zeros(nsteps)
for j in range(nwalkers):
    x=0
    y=0
    z=0
    for i in range(nsteps):
        val=rd.random()#choose + step or - step
        axis=rd.randrange(3)#pick x y or z randomly
        if(val<p):
            if axis==0: x += 1
            if axis==1: y += 1
            if axis==2: z += 1
        else:
            if axis==0: x -= 1
            if axis==1: y -= 1
            if axis==2: z -= 1
        r = math.sqrt(x**2 + y**2 + z**2)
        rav[i]+=r/nwalkers
        r2av[i] += r**2/nwalkers
        
plt.plot(rav,marker="o",label="average r")
plt.plot(r2av,marker="o",label="average $r^2$")
plt.xlabel("step number")
plt.ylabel("average")
plt.legend()
plt.show()
