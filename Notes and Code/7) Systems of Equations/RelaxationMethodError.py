import numpy as np
import math

def f(x):
    return math.sqrt(1-math.log(x))
def fprime(x):
    return -1/(2*x*math.sqrt(1-math.log(x)))

#initial guess
x=0.5
target=1e-5
epsilonp=100
n=0
while abs(epsilonp)>target:
    xp=f(x)
    epsilonp=(x-xp)/(1-1/fprime(x))
    x=xp
    n+=1
    print(xp)

print(n," steps")
