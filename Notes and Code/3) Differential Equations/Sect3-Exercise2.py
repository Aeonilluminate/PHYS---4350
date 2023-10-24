import numpy as np
import matplotlib.pyplot as plt
import math
import sys

#define our function; in this case g only depends on u
def g(u):
    return (1/(1-u)**2)*math.exp(-2*u/(1-u))
#define initial conditions
x_0=10
t_0=0
u_0 = t_0/(1+t_0)
print("Initial values: x=",x_0," when u=",u_0)

a=0
b=1
N=1000
h=(b-a)/N

upoint=np.arange(a,b,h)
tpoint=[]
xpoint=[]
x=x_0
for u in upoint:
    xval=x+h*g(u)
    tpoint.append(u/(1-u))
    print(u, u/(1-u))
    xpoint.append(xval)
    x=xval

plt.plot(tpoint,xpoint)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.xlim(0,10)
#plt.ylim(0,11)
plt.savefig("Ex2.png")
plt.show()




