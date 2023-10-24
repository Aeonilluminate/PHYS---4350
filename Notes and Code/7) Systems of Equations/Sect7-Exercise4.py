import numpy as np
import math

A = np.zeros([2,2],float)
A[0][0] = -4
A[0][1] = 3
A[1][1] = 2
print("A = ")
print(A)

a0 = A[:,0]
#print(a0)
a1 = A[:,1]
#print(a1)

u0 = np.copy(a0)
u0length=math.sqrt(u0[0]**2 + u0[1]**2)
q0=u0/u0length
#print(q0)

u1 = a1-(np.dot(q0,a1))*q0
print("u1 = ",u1)


    



