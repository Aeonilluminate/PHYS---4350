import numpy as np
import math
import matplotlib.pyplot as plt
import cmath
import numpy.fft as fft
import sys

Dt = 0.1
N = 128#want a power of 2 since we will use FFT
L = N*Dt
print("Delta-t = ",Dt," and N = ",N," so that the interval length L is ",L)

k=0.7#no longer an integer, number between 0 and N/2
period = L/k
f = 1/period
print("We're going to set k equal to ",k)
print("Let the period of our sine function be T = L/k = ",period)
print("Then the frequency is f = 1/T = ",f)

print("The relevant frequencies are:")
print("sampling freq = 1/Delta-t = ",1/Dt)
print("Nyquist freq = 1/(2*Delta-t) = ",1/(2*Dt))
print("Freq of function = ",f)

#set up t points
t1 = np.linspace(0,L,N)
#caluculate function values
y1 = np.sin(2*math.pi*f*t1)
#calculate coefficients
c1 = fft.rfft(y1)
#magnitude
cmag=abs(c1)

plt.figure(1)
plt.plot(cmag,lw=0,marker="o")
plt.ylabel("$|c_k|$")
plt.xlabel("k")
plt.title("DFT Coefficients")

plt.figure(2)
#get true function
tpoints = np.linspace(0,L,1000)
ytrue = np.sin(2*math.pi*f*tpoints)
#calculate yn based on cn
y2 = fft.irfft(c1)

plt.plot(tpoints,ytrue,lw=2,label="true function",color="blue")
plt.plot(t1,y1,lw=0,marker="o",label="sampling points",color="yellow")
plt.plot(t1,y2,lw=2,marker=".",label="function based on FFT coefficients",color="red")
plt.ylabel("function values")
plt.xlabel("time (s)")
plt.legend()

plt.show()
