import random as rd
import matplotlib.pyplot as plt
import numpy as np

nsteps=100
p=0.5
nwalkers=500

print("First let's draw the random walks of 4 walkers.")
plt.figure(1)
for j in range(1):
    x=0
    xvals=[]
    for i in range(nsteps):
        xvals.append(x)
        stepsize=rd.uniform(-1,1)
        x += stepsize
        #print(x,stepsize)
    plt.plot(xvals,marker="o")


plt.xlabel("step number")
plt.ylabel("x")
plt.title("Random Walks")

plt.show()

plt.figure(2)
print("Now let's consider the average value of x and x^2 at each step for 500 walkers.")
xav=np.zeros(nsteps)
x2av=np.zeros(nsteps)
stepav=np.zeros(nsteps)
step2av=np.zeros(nsteps)
for j in range(nwalkers):
    x=0
    for i in range(nsteps):
        xvals.append(x)
        stepsize=rd.uniform(-1,1)
        x += stepsize
        xav[i]+=x/nwalkers
        x2av[i] += x**2/nwalkers
        stepav[i] += stepsize/nwalkers
        step2av[i] += stepsize**2/nwalkers

plt.figure(1)        
plt.plot(xav,marker="o",label="average x")
plt.plot(x2av,marker="o",label="average $x^2$")
plt.xlabel("step number")
plt.ylabel("average")
plt.legend()

plt.figure(2)
plt.plot(stepav,marker="o",label="average step size")
plt.plot(step2av,marker="o",label="average step size squared")
plt.xlabel("step number")
plt.ylabel("average")
plt.legend()
plt.show()
