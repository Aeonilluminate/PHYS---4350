import numpy as np
import math
import matplotlib.pyplot as plt

# PART A -----------------------------------------------
c=2

def f(x):
    return 1-math.exp(-c*x)
def fprime(x):
    return c*math.exp(-c*x)

#initial guess
x=0.5
target=1e-6
epsilonp=100
n=0
while abs(epsilonp)>target:
    xp=f(x)
    epsilonp=(x-xp)/(1-1/fprime(x))
    x=xp
    n+=1
    print(f'x_p = {xp}, epsilonp = {epsilonp}')

print(n," steps")

# END --------------------------------------------------


# PART B -----------------------------------------------

def f(x, c):
    return 1-math.exp(-c*x)
def fprime(x, c):
    return c*math.exp(-c*x)

C = []
X = []

for c in np.arange(0, 3, 0.01):

    C.append(c)
    
    #initial guess
    x=0.5
    target=1e-6
    epsilonp=100
    n=0
    while abs(epsilonp)>target:
        xp=f(x, c)
        epsilonp=(x-xp)/(1-1/fprime(x, c))
        x=xp
        n+=1

    X.append(x)


plt.plot(C, X)
plt.title(r'Solutions to $x=1-e^{-cx}$ for given $c$')
plt.xlabel(r'values of $c$')
plt.ylabel(r'$x$')