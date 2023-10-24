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

y1 = np.loadtxt("pitch.txt",float)

c1 = dftcoeff(y1)

#Let's plot y and c
cmag=abs(c1)#can't plot a complex number, so use the magnitude

plt.figure(1)
plt.plot(y1)
plt.ylabel("$y_n$")
plt.xlabel("n")
plt.title("Samples")

plt.figure(2)
plt.plot(cmag)
plt.ylabel("$c_k$")
plt.xlabel("k")
plt.title("DFT Coefficients")

plt.show()

#The signal repeats 16 times over the given range, and the dominant k is k=16
