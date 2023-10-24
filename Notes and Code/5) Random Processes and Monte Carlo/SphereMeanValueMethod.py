import random as rd
import math


def f(x,y,z):
    val=0
    if (x**2 + y**2 + z**2) <= 1:
        val=1
    return val

n=10**5
ax=-1
bx=1
ay=-1
by=1
az=-1
bz=1
factor=(bx-ax)*(by-ay)*(bz-az)/n
s=0
for i in range(n):
    x=rd.uniform(ax,bx)
    y=rd.uniform(ay,by)
    z=rd.uniform(az,bz)
    s += factor*f(x,y,z)

print("True value: ",4*math.pi/3)
print("Answer after ",n,"points = ",s)



