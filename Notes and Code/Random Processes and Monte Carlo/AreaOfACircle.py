import random as rd
import math
import matplotlib.pyplot as plt

rd.seed(140134)

asquare=4#area of the square
npoints=[10**2,10**3,10**4,10**5,10**6,10**7]
acircle=[]
for n in npoints:
    k=0
    for i in range(n):
        x=rd.uniform(-1,1)
        y=rd.uniform(-1,1)
        if abs(y) < math.sqrt(1-x**2):#inside the circle
            k+=1
    pcircle=k/n
    acircle.append(pcircle*asquare)

plt.plot(npoints,acircle)
plt.xscale("log")
plt.xlabel("number of points")
plt.ylabel("Area of circle")
plt.axhline(y=math.pi,color="red")
plt.show()

