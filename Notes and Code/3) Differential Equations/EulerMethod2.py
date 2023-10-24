import numpy as np
import matplotlib.pyplot as plt
import math

print("Our givens: dx/dt=-x^3 + sin(t), x=0 when t=0\n")

#define our function
def f(x,t):
    return -x**3 + math.sin(t)
#define initial conditions
x0=0
t0=0

#choose end point
tf=10

# choose number of steps
n1=10
n2=25
n3=50
n4=1000

h1=(tf-t0)/n1
h2=(tf-t0)/n2
h3=(tf-t0)/n3
h4=(tf-t0)/n4

tpoints1=np.arange(t0,tf,h1)
tpoints2=np.arange(t0,tf,h2)
tpoints3=np.arange(t0,tf,h3)
tpoints4=np.arange(t0,tf,h4)
xpoints1=[]
xpoints2=[]
xpoints3=[]
xpoints4=[]

xi=x0
for ti in tpoints1:
    xpoints1.append(xi)
    xi +=h1*f(xi,ti)

xi=x0
for ti in tpoints2:
    xpoints2.append(xi)
    xi +=h2*f(xi,ti)

xi=x0
for ti in tpoints3:
    xpoints3.append(xi)
    xi +=h3*f(xi,ti)

xi=x0
for ti in tpoints4:
    xpoints4.append(xi)
    xi +=h4*f(xi,ti)

plt.plot(tpoints1,xpoints1,label="n=10")
plt.plot(tpoints2,xpoints2,label="n=25")
plt.plot(tpoints3,xpoints3,label="n=50")
plt.plot(tpoints4,xpoints4,label="n=1000")

plt.xlabel("t, time (s)")
plt.ylabel("x(t), position (m)")
plt.title("Euler Method")
plt.ylim(-1.2,1.5)

#draw
plt.legend()
plt.savefig("Euler.png")
plt.show()
