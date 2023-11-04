import numpy as np
import math
import matplotlib.pyplot as plt
import cmath
import numpy.fft as fft

#define function to calculate coefficients c_k given a set of function values y
def dftcoeff(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*cmath.exp(-2j*cmath.pi*k*n/N)#imaginary number in Python is j and it must be paired with a number!
    return c

y1 = np.loadtxt("Notes and Code\9) Fourier Analysis\pitch.txt",float)

plt.figure(1)
plt.plot(y1)
plt.ylabel("$y_n$")
plt.xlabel("n")
plt.title("Samples")

#using our DFT function
c1 = dftcoeff(y1)
cmag=abs(c1)

plt.figure(2)
plt.plot(cmag)
plt.ylabel("$c_k$")
plt.xlabel("k")
plt.title("DFT Coefficients")

#using the built-in FFT function
c2 = fft.rfft(y1)
cmag2=abs(c2)

plt.figure(3)
plt.plot(cmag2)
plt.ylabel("$c_k$")
plt.xlabel("k")
plt.title("FFT Coefficients from numpy.fft.rfft")

#using the built-in FFT function
c3 = fft.fft(y1)
cmag3=abs(c3)

plt.figure(4)
plt.plot(cmag3)
plt.ylabel("$c_k$")
plt.xlabel("k")
plt.title("FFT Coefficients from numpy.fft.fft")

plt.show()
