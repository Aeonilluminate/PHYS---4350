import numpy as np
import math
import matplotlib.pyplot as plt
import cmath
import numpy.fft as fft
import sys

def func(f,t):
    return np.cos(2*math.pi*f*t)

f = 4#Hz
Dt = 0.1#seconds
#Dt = 0.2#seconds
L = 6.5#seconds

print("freq = ",f)
print("Nyquist freq = ",1/(2*Dt))

plt.figure(1)
#To draw the function
tdraw = np.linspace(0,L,1000)
ydraw = func(f,tdraw)
plt.plot(tdraw,ydraw,lw=2)
#To sample the function
ts = np.linspace(0,L-Dt,int(L/Dt))
ys = func(f,ts)
plt.plot(ts,ys,lw=0,marker="o")
plt.ylabel("f(t)")
plt.xlabel("time")

c1 = fft.rfft(ys)

cmag=abs(c1)

plt.figure(2)
plt.plot(cmag,lw=0,marker="o")
plt.ylabel("$|c_k|$")
plt.xlabel("k")
plt.title("DFT Coefficients")

plt.show()

#compare different frequencies
plt.figure(3)
f2=0.9#Hz
ydraw2 = func(f2,tdraw)
plt.plot(tdraw,ydraw2,lw=4,label="0.9 Hz")
plt.plot(tdraw,ydraw,lw=2, label="4 Hz")
plt.plot(ts,ys,lw=0,marker="o",label="samples")
plt.ylabel("f(t)")
plt.xlabel("time")
plt.legend()

plt.show()
