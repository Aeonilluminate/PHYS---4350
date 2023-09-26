import random as rd
import math
import numpy as np
import matplotlib.pyplot as plt

N0=1000#number of atoms we started with
tau=16.3
h=1#time-step in seconds
p=1-math.exp(-h/tau)
tmax=100

tpoints=np.arange(0,tmax,h)
npoints=[]

N=N0
for t in tpoints:
    npoints.append(N)

    #in this time step, how many decay?
    decays=0
    for i in range(N):#cycle over remaining atoms
        if rd.random()<p:#does this atom decay?
            decays+=1
    N-=decays#number of atoms left after this time step

plt.plot(tpoints,npoints)
plt.xlabel("time (s)")
plt.ylabel("Number of atoms")
plt.show()
