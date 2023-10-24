import numpy as np
import math
import matplotlib.pyplot as plt
import cmath

print("First let's calculate all the coefficients for N even and N odd")

#define function to calculate coefficients c_k given a set of function values y
def dftcoeffall(y):
    N = len(y)
    c = np.zeros(N,complex)
    for k in range(N):
        for n in range(N):
            c[k] += y[n]*cmath.exp(-2j*cmath.pi*k*n/N)#imaginary number in Python is j and it must be paired with a number!
    return c

#First, N even
y = [1,3,4.8,5.3,3.6,2.2,0.9,-0.1,0.2,0.5,1.5,3.2,4.8,5.3,4.7,3.1]
N = len(y)
print("number of values:",N)

c = dftcoeffall(y)
for k in range(N):
    print("coefficient ",k,": ",c[k])

print("For N even, we need to calculate c_0 up to c_(N/2)")
print("Need to calculate (N/2)+1 = ",int((N/2)+1)," coefficients")
print()

#Now, N odd
y = [1,3,4.8,5.3,3.6,2.2,0.9,-0.1,0.2,0.5,1.5,3.2,4.8,5.3,4.7,3.1,1]
N = len(y)
print("number of values:",N)

c = dftcoeffall(y)
for k in range(N):
    print("coefficient ",k,": ",c[k])

print("For N odd, we need to calculate c_0 up to c_(N-1)/2")
print("Need to calculate (N+1)/2 = ",int((N+1)/2)," coefficients")
print()

print("use the // operator")
print("16//2+1 = ",16//2 + 1)
print("17//2+1 = ",17//2 + 1)
print()

print("Now let's define a function which calculate the minimum number of coefficients for N even or N odd")
#define function to calculate coefficients c_k given a set of function values y
def dftcoeff(y):
    N = len(y)
    c = np.zeros(N,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*cmath.exp(-2j*cmath.pi*k*n/N)#imaginary number in Python is j and it must be paired with a number!
    return c
    
#First, N even
y = [1,3,4.8,5.3,3.6,2.2,0.9,-0.1,0.2,0.5,1.5,3.2,4.8,5.3,4.7,3.1]
N = len(y)
print("number of values:",N)

c = dftcoeff(y)
for k in range(N):
    if k<N//2+1:
        print("coefficient ",k,": ",c[k])
    else:
        print("coefficient ",k,": ",np.conj(c[N-k]))

#Now, N odd
y = [1,3,4.8,5.3,3.6,2.2,0.9,-0.1,0.2,0.5,1.5,3.2,4.8,5.3,4.7,3.1,1]
N = len(y)
print("number of values:",N)

c = dftcoeff(y)
for k in range(N):
    if k<N//2+1:
        print("coefficient ",k,": ",c[k])
    else:
        print("coefficient ",k,": ",np.conj(c[N-k]))

plt.plot(y)
plt.ylabel("$y_n$")
plt.xlabel("n")
plt.show()
