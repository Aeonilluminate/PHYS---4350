import numpy as np

a = np.zeros([2,2],float)
b = np.zeros([2,2],float)

a[0][0] = 2
a[1][0] = 1
a[1][1] = 4
b[0][1] = 2
b[1][1] = 3
b[1][0] = 5

print(a)
print(b)

print("a*b = ")
print(a*b)
print("np.dot(a,b) = ")
print(np.dot(a,b))
    



