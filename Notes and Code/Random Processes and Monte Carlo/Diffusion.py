import random as rd
import matplotlib.pyplot as plt
import numpy as np
import math

nsteps=10**5
p=0.5#probability for positive step
npart=400#number of particles
r=np.zeros([2,npart],float)#r[0]=x and r[1]=y for each particle
#initialize the particle positions to be in a 20x20 grid centered around x,y=0,0
for i in range(npart):
    r[0][i] = (int(i/20))-10
    r[1][i] = i%20 - 10

#plot initial positions
plt.figure(1)
plt.scatter(r[0],r[1])
plt.title("t=0")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("square")
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.show()

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

#plot particle positions again
plt.figure(2)
plt.scatter(r[0],r[1])
s="t="+str(nsteps)
plt.title(s)
plt.xlabel("x")
plt.ylabel("y")
plt.axis("square")
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.show()     

