import numpy as np
import math
import matplotlib.pyplot as plt
import numpy.random as nprd
import random as rd

nprd.seed(139)

tau=2.3

n=100
tpts=[]
dx=0.5
mybins=np.arange(0,30,dx)
myweights=np.zeros(n,float)
myweights += 1/(n*dx)#make probability density function
xcenters = (mybins[:-1] + mybins[1:]) / 2

#generating decay times based on exponential probability
for i in range(n):
    tpts.append(nprd.exponential(tau))
print(np.mean(tpts))

ytrue=np.exp(-xcenters/tau)/tau#true probability density function

plt.hist(tpts,bins=mybins,weights=myweights)
plt.plot(xcenters,ytrue)
plt.show()

file1 = open("histdata.txt","w")
for i in range(n):
    l = str(round(tpts[i],2)) + "\n"
    file1.write(l)
file1.close()

