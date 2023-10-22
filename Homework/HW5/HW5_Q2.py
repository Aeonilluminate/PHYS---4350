import numpy as np
import math
import matplotlib.pyplot as plt
import random as rd

rd.seed(44)

p_distinct = 0.25
ntrials=5
nrolls=2000

for i in range(ntrials):
    P2 = 0
    measured_P = []
    for j in range(1,nrolls):
        val=rd.random()
        if val<p_distinct:
            P2 += 1

        measured_P.append(P2/j)

    s="Trial "+str(i)
    plt.plot(measured_P,label=s)
    print("Final measurement, trial #",i,": ",P2/j)

plt.figure(1)
plt.xlabel("Number of Rolls")
plt.ylabel("Measured probability")
plt.title("Measured probability of Rolling 2 (weighted 6-sided die)")
plt.legend()
plt.show()

print("It seems at least 750 rolls is necessary for the measured probability to converge to the true probability.")

p=0.25
ntrials=1000
nrolls=750
measured_P=[]
for i in range(ntrials):
    P2=0
    for j in range(1,nrolls):
        val=rd.random()
        if(val<p):
            P2+=1
    measured_P.append(P2/nrolls)

b=np.linspace(0.20, 0.30, 15)

plt.figure(2)
plt.hist(measured_P,bins=b)
plt.ylabel("Entries")
plt.xlabel("Measured probability")
plt.ylim(0,300)
plt.title("Results of 1000 pseudo-experiments")
plt.show()

print(f'Mean of Distribution = {sum(measured_P)/len(measured_P)}')
print(f'Standard Deviation = {np.std(measured_P)}')