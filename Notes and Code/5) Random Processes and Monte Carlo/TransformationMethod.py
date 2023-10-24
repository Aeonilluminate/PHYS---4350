import random as rd
import math
import matplotlib.pyplot as plt
import numpy as np

mu=1
n=10000

#define true function
def p(x):
    return mu*math.exp(-mu*x)
def x(z):
    return (-1/mu)*math.log(1-z)

xrand=[]
for i in range(n):
    zval=rd.random()
    xval=x(zval)
    xrand.append(xval)

binwidth=0.1
b=np.arange(0,8,binwidth)
w=[1./(n*binwidth) for i in range(n)]
plt.hist(xrand,weights=w,bins=b)

xpoints=np.arange(0,8,0.1)
ypoints=list(map(p,xpoints))
plt.plot(xpoints,ypoints)

plt.xlabel("x")
plt.ylabel("Probability density")
plt.show()

