import random as rd
import matplotlib.pyplot as plt
import numpy as np

rd.seed(25)

p=0.5
ntrials=1000
ntosses=2000
measuredprob=[]
for i in range(ntrials):
    k=0
    for j in range(1,ntosses):
        val=rd.random()
        if(val<p):
            k+=1
    measuredprob.append(k/ntosses)

b=np.linspace(0.44,0.56,15)
plt.hist(measuredprob,bins=b)
plt.ylabel("Entries")
plt.xlabel("Measured probability")
plt.ylim(0,300)
plt.title("Results of 1000 pseudo-experiments")
plt.show()
