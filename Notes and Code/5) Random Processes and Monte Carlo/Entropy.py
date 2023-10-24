import random as rd
import matplotlib.pyplot as plt
import numpy as np
import math

nsteps=6*(10**6)
p=0.5#probability for positive step
npart=400#number of particles
r=np.zeros([2,npart],float)#r[0]=x and r[1]=y for each particle
#initialize the particle positions to be in a 20x20 grid centered around x,y=0,0
for i in range(npart):
    r[0][i] = (int(i/20))-10
    r[1][i] = i%20 - 10

b = np.linspace(-100,100,9)#bin edges for histogram
entropy=[]

plt.figure(1)
for i in range(nsteps):#for each step
    particle=rd.randrange(npart)#choose a particle at random
    flag=0
    while(flag==0):
        val=rd.random()#choose + step or - step
        if(val<p):
            step = 1
        else:
            step = -1
        axis=rd.randrange(2)#pick x or y randomly

        if abs(r[axis][particle] + step)>100:#would taking this step push the particle outside the boundary?
            flag=0#if yes, then don't take the step; consider another random step for this particle by executing the while loop again
        else:#if no, then take the step; and don't execute while loop again
            r[axis][particle] += step
            flag=1
    if i==0 or i==10**6 or i==2*10**6 or i==3*10**6 or i==4*10**6 or i==5*10**6:
        (h, xe, ye, patches) = plt.hist2d(r[0],r[1],bins=b)
        S = 0
        for j1 in range(8):
            for j2 in range(8):
                pi=h[j1][j2]/npart
                if pi>0: S+=pi*math.log(pi)
        S=S*-1
        entropy.append(S)

#gets the last step, where i=nsteps-1, which is approx 6*10**6
(h, xe, ye, patches) = plt.hist2d(r[0],r[1],bins=b)
S = 0
for j1 in range(8):
    for j2 in range(8):
        pi=h[j1][j2]/npart
        if pi>0: S+=pi*math.log(pi)
S=S*-1
entropy.append(S)

plt.figure(2)
time=[0,1,2,3,4,5,6]
plt.plot(time,entropy,lw=2)
plt.xlabel("time steps (x10^6)")
plt.ylabel("Entropy")
plt.savefig("EntropyVsTime")
plt.show()



