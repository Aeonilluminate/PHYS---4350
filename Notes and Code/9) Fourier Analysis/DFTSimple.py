import numpy as np
import math
import matplotlib.pyplot as plt
import cmath

#define our function
def f(x):
    # return np.sin(4*x)
    # return 4*np.sin(x)
    # return np.sin(4*x) + 4*np.sin(10*x)
    # return 50*np.sin(4*x) + np.sin(10*x)
    # return x
    return np.sin(x/2)

#define function to calculate coefficients c_k given a set of function values y
def dftcoeff(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*cmath.exp(-2j*cmath.pi*k*n/N)#imaginary number in Python is j and it must be paired with a number!
    return c

N = 100
L = 4*math.pi
x1=np.linspace(0,L,N)
y1 = f(x1)

c1 = dftcoeff(y1)

#Let's plot y and c
cmag=abs(c1)#can't plot a complex number, so use the magnitude

plt.figure(1)
plt.plot(y1,lw=0,marker="o")
plt.ylabel("$y_n$")
plt.xlabel("n")
label = "Samples of $f(x)$, with $L = 2\pi$"
plt.title(label)

plt.figure(2)
plt.plot(cmag,lw=0,marker="o")
plt.ylabel("$c_k$")
plt.xlabel("k")
plt.title("DFT Coefficients")

plt.show()
