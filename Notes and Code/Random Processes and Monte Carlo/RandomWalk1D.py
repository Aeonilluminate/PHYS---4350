import random as rd
import matplotlib.pyplot as plt
import numpy as np

nsteps=100
p=0.5
nwalkers=500

print("First let's draw the random walks of 4 walkers.")
plt.figure(1)
for j in range(4):
    x=0
    xvals=[]
    for i in range(nsteps):
        xvals.append(x)
        val=rd.random()
        if(val<p):
            x += 1
        else:
            x -= 1
    plt.plot(xvals,marker="o")


plt.xlabel("step number")
plt.ylabel("x")
plt.title("Random Walks")

plt.show()

plt.figure(2)
print("Now let's consider the average value of x and x^2 at each step for 500 walkers.")
xav=np.zeros(nsteps)
x2av=np.zeros(nsteps)
for j in range(nwalkers):
    x=0
    for i in range(nsteps):
        val=rd.random()
        if(val<p):
            x += 1
        else:
            x -= 1
        xav[i]+=x/nwalkers
        x2av[i] += x**2/nwalkers
        
plt.plot(xav,marker="o",label="average x")
plt.plot(x2av,marker="o",label="average $x^2$")
plt.xlabel("step number")
plt.ylabel("average")
plt.legend()
plt.show()
