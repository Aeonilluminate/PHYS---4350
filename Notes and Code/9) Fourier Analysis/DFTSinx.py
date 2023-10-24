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

N = 100
L = 2*math.pi
x1=np.linspace(0,L,N)
y1 = np.sin(x1)

c1 = dftcoeff(y1)
for k in range(N):
    if k<N//2+1:
        print("coefficient ",k,": ",c1[k])
    else:
        print("coefficient ",k,": ",np.conj(c1[N-k]))

#Let's plot y and c
cmag=abs(c1)#can't plot a complex number, so use the magnitude

plt.figure(1)
plt.plot(y1,lw=0,marker="o")
plt.ylabel("$y_n$")
plt.xlabel("n")
label = "Samples of $f(x) = \sin x$, with $L = 2\pi$"
plt.title(label)

plt.figure(2)
plt.plot(cmag,lw=0,marker="o")
plt.ylabel("$c_k$")
plt.xlabel("k")
plt.title("DFT Coefficients")

plt.show()
