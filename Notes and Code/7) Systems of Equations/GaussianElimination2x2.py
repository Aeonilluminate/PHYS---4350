import numpy as np

#Define the two relevant matrices
print("2x2 matrix of x and y coefficients:")
a = np.array([[2,3],[4,-6]],float)
print(a)
print("The 2x1 matrix, or just a 2-element vector, that is the right-hand side of the equation:")
v = np.array([4,7],float)
print(v)
print()

print("We can select a single row of matrix with a[0,:] or a[1,:]")
print("First row: ",a[0,:])
print("Second row: ",a[1,:])
print()

#this is the first diagonal element
diag = a[0][0]
#let's divide the first row by this element
a[0,:] /= diag
v[0] /= diag
print("Here's our matrices:")
print(a)
print(v)
print()

#this is the first element in second row
ele = a[1][0]
#divide second row by this
a[1,:] /= ele
v[1] /= ele
print("Here's our matrices:")
print(a)
print(v)
print()

#now subtract second row from the first
a[1,:] = a[0,:] - a[1,:]
v[1] = v[0] - v[1]
print("Here's our matrices:")
print(a)
print(v)
print()

#now divide second row by second element
ele = a[1][1]
a[1,:] /= ele
v[1] /= ele
print("Here's our matrices:")
print(a)
print(v)
print()

#now substitute and solve
x=np.empty([2],float)
x[1] = v[1]
x[0] = v[0] - a[0][1]*x[1]
print("The solution")
print(x)

