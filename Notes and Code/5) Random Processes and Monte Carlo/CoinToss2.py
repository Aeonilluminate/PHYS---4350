import random as rd
import matplotlib.pyplot as plt

p=0.5
ntrials=5
ntosses=2000
for i in range(ntrials):
    k=0
    measuredprob=[]
    for j in range(1,ntosses):
        val=rd.random()
        if(val<p):
            k+=1
        measuredprob.append(k/j)
    s="Trial "+str(i)
    plt.plot(measuredprob,label=s)
    print("Final measurement, trial #",i,": ",k/j)

plt.xlabel("Number of tosses")
plt.ylabel("Measured probability")
plt.title("Measured probability of coin coming up tails")
plt.legend()
plt.show()
