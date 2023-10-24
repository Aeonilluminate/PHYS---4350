import numpy as np

#Define the two relevant matrices
print("Square matrix of x and y coefficients:")
a = np.array([[2,3],[4,-6]],float)
#a = np.array([[-4,1,-1],[2,-5,2],[6,2,-4]],float)
b = np.copy(a)#make a copy of the original matrix for later
print(a)
print()
print("The 1-column matrix, or vector, that is the right-hand side of the equation:")
v = np.array([4,7],float)
#v = np.array([8,10,-3],float)
print(v)
print()

n = len(v)
#loop over each row
for r in range(n):
    diag=a[r][r]#diagonal element
    #divide this row by diagonal element
    a[r,:] /= diag
    v[r] /= diag
    print("After dividing row ",r," by ",diag)
    print(a)
    print()
    print(v)
    print()

    #now loop over rows below
    for i in range(r+1,n):
    #divide lower rows by first element so first element becomes 1
        first=a[i][r]
        a[i,:] /= first
        v[i] /= first
        print("After dividing row ",i," by ",first,"(the first non-zero element)")
        print(a)
        print()
        print(v)
        print()
        
        #now subtract this row (row i) from row r and replace row i with the result
        a[i,:] = a[r,:] - a[i,:]
        v[i] = v[r] - v[i]
        print("After subtracting row ",i," from row ",r," and replacing row ",i)
        print(a)
        print()
        print(v)
        print()

print("Backsubstitution")
x=np.empty([n],float)
for i in range(n-1,-1,-1):#from n-1 to 0 in steps of -1; starts at bottom row and goes up
    x[i] = v[i]
    for j in range(i+1,n):
        x[i] -= a[i][j]*x[j]

print("Solution:")
print(x)
print()

#the original matrix times x should yield the original vector v
print("Check the answer:")
print(np.dot(b,x))
