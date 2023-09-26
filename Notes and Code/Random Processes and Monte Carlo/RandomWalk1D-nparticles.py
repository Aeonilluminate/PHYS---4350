import random as rd
import matplotlib.pyplot as plt
import numpy as np


nsteps=100
p=0.5#probability for positive step
npart=100000#number of particles
x=np.zeros([npart],float)

for i in range(nsteps):#for each step
    for j in range(npart):
        val=rd.random()#choose + step or - step
        if(val<p):
            step = 1
        else:
            step = -1
        x[j] += step

#histogram of each particle's position after nsteps
plt.hist(x)
s="Particle position at t="+str(nsteps)
plt.title(s)
plt.xlabel("x (arbitrary units)")
plt.ylabel("entries")
plt.show()     

