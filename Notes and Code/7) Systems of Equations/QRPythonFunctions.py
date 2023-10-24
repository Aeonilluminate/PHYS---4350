import numpy as np
import numpy.linalg as la
import sys



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

d,v = la.eigh(a)

print("Eigenvectors:")
print(v)
print()
print("Eigenvalues:")
print(d)
print()

d2 = la.eigvalsh(a)
print("Eigevalues:")
print(d2)
    




