import random as rd
import math


def f(x,y):
    val=0
    if (x**2 + y**2) <= 1:
        val=1
    return val

n=10**5
ax=-1
bx=1
ay=-1
by=1
factor=(bx-ax)*(by-ay)/n
s=0
for i in range(n):
    x=rd.uniform(ax,bx)
    y=rd.uniform(ay,by)
    s += factor*f(x,y)

print("True value: ",math.pi)
print("Answer after ",n,"points = ",s)



