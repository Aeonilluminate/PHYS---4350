import numpy as np

a = np.zeros([2,2],float)

a[0][0] = 1
a[0][1] = 2
a[1][0] = 3
a[1][1] = 4

print("Here's a:")
print(a)
print()

print("Setting b = a")
b = a
print("Changing one element of a")
a[1][0] = 8
print(a)
print(b)
print("Both a and b are changed")
print()

print("Making b a copy of a")
b = np.copy(a)
print("Changing one element of a")
a[1][0] = 15
print(a)
print(b)
print("Now only a is changed")





    



