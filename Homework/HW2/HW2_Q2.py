import numpy as np
import math

def f(x):
    return (x**3 + 1)*math.exp(-x)

target_epsilon = 1e-5

a, b = -1, 1
N1 = 2
dx1 = (b - a)/N1

S1 = 0
T1 = 0
for k in range(1, N1+1):
    if k == 1:
        S1 += f(a)
    if k == N1:
        S1 += f(b) 
    if k > 1 and k < N1 and k%2 == 0:
        S1 += 2*f(a + k*dx1)
    if k > 1 and k < N1 and k%2 == 1:
        T1 += 2/3*f(a + k*dx1)
S1 = S1/3
I1 = dx1*(S1 + 2*T1)

N_old, N_new = N1, 0
dx_old, dx_new = dx1, 0
I_old, I_new = I1, 0
S_old, S_new = S1, 0
T_old, T_new = T1, 0
epsilon = 1000.

while epsilon > target_epsilon:
    N_new = N_old*2
    dx_new = dx_old/2
    S_new = S_old + T_old
    for k in range(1, N_new, 2):
        T_new += 2/3*f(a + k*dx_new)  
    I_new = dx_new*(S_new + 2*T_new)
    epsilon = 1/15*(I_new - I_old)
    N_old, dx_old, S_old, T_old, I_old = N_new, dx_new, S_new, T_new, I_new

print(f'''
Final approximation = {I_new},
Number of slices = {N_new},
Error Estimate = {epsilon}''')