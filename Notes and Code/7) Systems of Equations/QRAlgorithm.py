import numpy as np
import numpy.linalg as la
import sys

def QRDecomp(matrix):
    m, n = matrix.shape
    if m!=n:
        print("Needs to be a square matrix.")
        return matrix, matrix
    u = np.zeros([n,n],float)
    q = np.zeros([n,n],float)
    for i in range(n):
        u[:,i] = matrix[:,i]
        for j in range(i):
            u[:,i] -= np.dot(q[:,j],matrix[:,i])*q[:,j]
        q[:,i] = u[:,i]/la.norm(u[:,i])
    r = np.zeros([n,n],float)
    for i in range(n):
        r[i][i] = la.norm(u[:,i])
        for j in range(i+1,n):
            r[i][j] = np.dot(q[:,i],matrix[:,j])
    return q,r

#define symmetric matrix a
#a = np.array([[1,4,8,4],[4,2,3,7],[8,3,6,9],[4,7,9,2]],float)
a = np.array([[1,2],[2,1]],float)
m, n = a.shape
#make sure a is square
if m!=n:
    print("Needs to be a square matrix.")
    sys.exit()
print(n,"x",n,"matrix")
#make sure a is symmetric
for i in range(n):
    for j in range(i+1,n):
        if abs(a[i][j]- a[j][i])>1e-8:
            print("Needs to be a symmetric matrix.")
            sys.exit()
print(a)
print()

#define threshold for off-diagonal elements
epsilon=1e-8

#create matrix to hold the eigenvectors
v = np.zeros([n,n],float)
#initialize it to the identity matrix
for i in range(n):
    v[i][i] = 1


d=np.copy(a)#copy original matrix to use in the calculation
diagonal=0#will set it to 1 when the matrix is diagonalized
while diagonal==0:
    q,r = QRDecomp(d)
    d = np.dot(r,q)
    v = np.dot(v,q)
    maxval=0
    #find the maximum off-diagonal element
    for i in range(n):
        for j in range(i+1,n):
            if abs(d[i][j])>maxval:
                maxval = abs(d[i][j])
            if abs(d[j][i])>maxval:
                maxval = abs(d[j][i])
    if maxval<epsilon:
        diagonal=1

print("Eigenvectors:")
print(v)
print()
print("Eigenvalues:")
print(d)
print()
print("Check the answer: Does AV = VD?")
print("AV = ")
print(np.dot(a,v))
print("VD = ")
print(np.dot(v,d))
    




