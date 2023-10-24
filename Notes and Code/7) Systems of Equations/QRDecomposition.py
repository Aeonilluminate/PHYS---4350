import numpy as np
import numpy.linalg as la
import sys

#define matrix a
a = np.array([[1,4,8,4],[4,2,3,7],[8,3,6,9],[4,7,9,2]],float)

print(a)

m, n = a.shape
if m!=n:
    print("Needs to be a square matrix.")
    sys.exit()
print(n,"x",n,"matrix")
print()

#Define vectors u and q
u = np.zeros([n,n],float)
q = np.zeros([n,n],float)

for i in range(n):
    u[:,i] = a[:,i]
    for j in range(i):
        u[:,i] -= np.dot(q[:,j],a[:,i])*q[:,j]
    q[:,i] = u[:,i]/la.norm(u[:,i])

print("Each column of this matrix is one of the vectors u_i")
print(u)
print("This is matrix Q; Each column of this matrix is one of the vectors q_i")
print(q)
print()

#Now make matrix r
r = np.zeros([n,n],float)
for i in range(n):
    r[i][i] = la.norm(u[:,i])
    for j in range(i+1,n):
        r[i][j] = np.dot(q[:,i],a[:,j])

print("This is matrix R")
print(r)
print()

print("Check to see if QR = A?")
print(np.dot(q,r))

