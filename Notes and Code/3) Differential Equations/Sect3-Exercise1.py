import numpy as np
import matplotlib.pyplot as plt
import math
import sys

print("Our givens: dx/dt=cos(t), x=0.8415 when t=1.\n")

#define our function; in this case f only depends on t
def f(t):
    return math.cos(t)
#define initial conditions
x_0=0.8415
t_0=1
h=1

print("Find x(2) in one step (h=1)")
xval=x_0 + h*f(t_0)
print(xval)
print()

plt.plot([t_0,t_0+h],[x_0,xval],label="one step",marker="o")
plt.xlabel("t, time (s)")
plt.ylabel("x(t), position (m)")

print("Find x(2) in two steps (h=0.5)")
h=0.5
xval1=x_0 + h*f(t_0)
xval2=xval1 + h*f(t_0+h)
print(xval2)
print()

plt.plot([t_0,t_0+h,t_0+2*h],[x_0,xval1,xval2],label="two steps",marker="o")
plt.xlabel("t, time (s)")
plt.ylabel("x(t), position (m)")

#true curve
def xfunc(t):
    return math.sin(t)
tp=np.arange(0,2*math.pi,0.01)
xp=list(map(xfunc,tp))
plt.plot(tp,xp,label="True x(t)")

#draw
plt.legend()
plt.savefig("Ex1.png")
plt.show()
