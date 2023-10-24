import numpy as np
import math
import matplotlib.pyplot as plt
import cmath

#define function to calculate coefficients c_k given a set of function values y
def dftcoeff(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*cmath.exp(-2j*cmath.pi*k*n/N)#imaginary number in Python is j and it must be paired with a number!
    return c

data = np.loadtxt("sunspots.txt",float)
y1=data[:,1]
x1=data[:,0]

c1 = dftcoeff(y1)

#Let's plot y and the power spectrum
power=abs(c1)**2

plt.figure(1)
plt.plot(x1,y1)
plt.ylabel("Number of observed sunspots")
plt.xlabel("Months since January 1749")
plt.title("Observed sunspots over time")

plt.figure(2)
plt.plot(power)
plt.ylabel("$|c_k|^2$")
plt.xlabel("k")
plt.title("Power spectrum")

plt.show()
