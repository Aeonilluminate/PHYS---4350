import numpy as np
import matplotlib.pyplot as plt
import math

print("Our givens: dx/dt=gt, x=10 m when t=1 s\n")

#define our function; in this case f only depends on t
def f(t):
    return 9.81*t
#define initial conditions
x_0=10
t_0=1

print("Let's find x(t_0 + h) = x(t_0) + hf(t_0)")
h=0.01
#Euler's method
xval1=x_0 + h*f(t_0)
print(xval1)
print()

print("Let's find x(t_0 + 2h) = x(t_0+h) + hf(t_0+h)")
xval2=xval1 + h*f(t_0+h)
print(xval2)
print()

print("We can repeat this process to map out the function x(t)")
tend=5.5
tpoints=np.arange(t_0,tend,h)
xpoints=[]
xi=x_0
for ti in tpoints:
    xpoints.append(xi)
    xi +=h*f(ti)

plt.plot(tpoints,xpoints,label="Euler")
plt.xlabel("t, time (s)")
plt.ylabel("x(t), position (m)")

#true curve
def xfunc(t):
    return (0.5*9.81*(t**2) + 5.095)
tp=np.arange(t_0,5,0.01)
xp=list(map(xfunc,tp))
plt.plot(tp,xp,label="True x(t)")

#draw
plt.legend()
plt.show()
