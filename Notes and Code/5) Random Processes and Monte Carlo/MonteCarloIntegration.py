import random as rd
import math
import matplotlib.pyplot as plt

def f(x):
    return (math.sin(1/(x*(2-x))))**2

rd.seed(88)

abox=2#area of the region 0<x<2,0<y<1
n=10**6
npoints=[]
a=[]
k=0
for i in range(1,n):
    x=rd.uniform(0,2)
    y=rd.uniform(0,1)
    if y < f(x):
        k+=1
    p=k/i
    npoints.append(i)
    a.append(p*abox)

print("Answer after ",n,"points = ",p*abox)

plt.plot(npoints,a)
plt.xscale("log")
plt.xlabel("number of points")
plt.ylabel("Area underneath the curve")
plt.show()

