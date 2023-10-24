import numpy as np
import matplotlib.pyplot as plt

#constants
N=5
#N=26
C=1
m=1
k=6
omega=2
alpha = 2*k - omega**2

#define matrices
a = np.zeros([N,N],float)
for i in range(N):
    if i==0 or i==N-1:
        a[i][i] = alpha - k
    else:
        a[i][i] = alpha
    if i>0:
        a[i][i-1] = -k
    if i<N-1:
        a[i][i+1] = -k

v = np.zeros(N,float)
v[0] = C

print(a)
print()
print(v)
print()

#save a copy of a for later
b = np.copy(a)

#loop over each row
for r in range(N):
    diag=a[r][r]#diagonal element
    #divide the diagonal element and the element to its right by zero
    a[r,r] /= diag
    if r<N-1:#doesn't apply to last row
        a[r,r+1] /= diag
    v[r] /= diag
    if N<6:
        print("After dividing row ",r," by ",diag)
        print(a)
        print()
        print(v)
        print()

    if r<N-1:#doesn't apply to last row
        #divide the next row by first element so first element becomes 1
        first=a[r+1][r]
        a[r+1][r] /= first
        a[r+1][r+1] /= first
        if r!=N-2:
            a[r+1][r+2] /= first
        if N<6:
            print("After dividing row ",r+1," by ",first,"(the first non-zero element)")
            print(a)
            print()
            print(v)
            print()
        
        #now subtract this row (row i) from row r and replace row i with the result
        a[r+1][r] = a[r][r]-a[r+1][r]
        a[r+1][r+1] = a[r][r+1] - a[r+1][r+1]
        if r!=N-2:
            a[r+1][r+2] = a[r][r+2] - a[r+1][r+2]
        v[r+1] = v[r] - v[r+1]
        if N<6:
            print("After subtracting row ",i," from row ",r," and replacing row ",i)
            print(a)
            print()
            print(v)
            print()

print("Backsubstitution")
x=np.empty([N],float)
for i in range(N-1,-1,-1):#from n-1 to 0 in steps of -1; starts at bottom row and goes up
    if i==N-1:
        x[i] = v[i]
    else:
        x[i] = v[i] - a[i][i+1]*x[i+1]

print("Solution:")
print(x)
print()

#the original matrix times x should yield the original vector v
print("Check the answer:")
print(np.dot(b,x))

if N>20:
    plt.plot(x,lw=2,marker="o")
    plt.xlabel("i (ith mass)")
    plt.ylabel("x_i (amplitude of ith mass displacement)")
    plt.show()
    
