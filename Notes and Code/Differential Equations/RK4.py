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
    k1=h1*f(xi,ti)
    k2=h1*f(xi+k1/2,ti+h1/2)
    k3=h1*f(xi+k2/2,ti+h1/2)
    k4=h1*f(xi+k3,ti+h1)
    xi += (1/6)*(k1+2*k2+2*k3+k4)

xi=x0
for ti in tpoints2:
    xpoints2.append(xi)
    k1=h2*f(xi,ti)
    k2=h2*f(xi+k1/2,ti+h2/2)
    k3=h2*f(xi+k2/2,ti+h2/2)
    k4=h2*f(xi+k3,ti+h2)
    xi += (1/6)*(k1+2*k2+2*k3+k4)

xi=x0
for ti in tpoints3:
    xpoints3.append(xi)
    k1=h3*f(xi,ti)
    k2=h3*f(xi+k1/2,ti+h3/2)
    k3=h3*f(xi+k2/2,ti+h3/2)
    k4=h3*f(xi+k3,ti+h3)
    xi += (1/6)*(k1+2*k2+2*k3+k4)

xi=x0
for ti in tpoints4:
    xpoints4.append(xi)
    k1=h4*f(xi,ti)
    k2=h4*f(xi+k1/2,ti+h4/2)
    k3=h4*f(xi+k2/2,ti+h4/2)
    k4=h4*f(xi+k3,ti+h4)
    xi += (1/6)*(k1+2*k2+2*k3+k4)

plt.plot(tpoints1,xpoints1,label="n=10")
plt.plot(tpoints2,xpoints2,label="n=25")
plt.plot(tpoints3,xpoints3,label="n=50")
plt.plot(tpoints4,xpoints4,label="n=1000")

plt.xlabel("t, time (s)")
plt.ylabel("x(t), position (m)")
plt.title("Fourth-order Runge-Kutta")
plt.ylim(-1.2,1.5)

#draw
plt.legend()
plt.savefig("RK4.png")
plt.show()
