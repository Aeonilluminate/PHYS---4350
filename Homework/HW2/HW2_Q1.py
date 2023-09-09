import numpy as np
import math

def trap_area(y1, y2, h):
    return 0.5*(y1 + y2)*h

def simp_area(y, h, k):
    if k%2 != 0:
        return 4*y*h
    else:
        return 2*y*h

data = np.loadtxt('hw2.txt', float)
X2 = data[:, 0]
X1 = X2[::2]
Y2 = data[:, 1]
Y1 = Y2[::2]

dx2 = X2[1] - X2[0]
dx1 = X1[1] - X1[0]
I_trap1, I_trap2 = 0, 0
I_simp1, I_simp2 = 0, 0

N2, N1 = len(Y2) - 1, len(Y1) - 1

# Trapezoidal Approximation
y_prev = Y2[0]
for y in Y2[1:]:
    I_trap2 += trap_area(y1=y_prev, y2=y, h=dx2)
    y_prev = y

y_prev = Y1[0]
for y in Y1[1:]:
    I_trap1 += trap_area(y1=y_prev, y2=y, h=dx1)
    y_prev = y

trap_error = 1/3*(I_trap2 - I_trap1)

# Simpson Approximation
for k, y in enumerate(Y2):
    if k == 0 or k == N2:
        I_simp2 += y 
    if k > 0 and k%2 == 1:
        I_simp2 += 4*y
    if k > 0 and k < N2 and k%2 == 0:
        I_simp2 += 2*y
I_simp2 = I_simp2*dx2/3

for k, y in enumerate(Y1):
    if k == 0 or k == N1:
        I_simp1 += y 
    if k > 0 and k%2 == 1:
        I_simp1 += 4*y
    if k > 0 and k < N1 and k%2 == 0:
        I_simp1 += 2*y
I_simp1 = I_simp1*dx1/3

simp_error = 1/15*(I_simp2 - I_simp1)

print('Trapezoidal Approximation = ', I_trap2, '\t Error Estimate = ', trap_error)
print('Simpson Approximation = ', I_simp2, '\t Error Estimate = ', simp_error)