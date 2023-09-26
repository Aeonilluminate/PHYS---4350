import random as rd
import math


def f(x):
    return (math.sin(1/(x*(2-x))))**2

rd.seed(5)

n=10**6
a=0
b=2
s=0
for i in range(n):
    x=rd.uniform(a,b)
    s += ((b-a)/n)*f(x)

print("Answer after ",n,"points = ",s)



