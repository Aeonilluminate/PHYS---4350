import numpy
import math

a=math.pi/2.
print("a is a number, a = ",a)
print("\n")

b=[0,math.pi/4.,math.pi/2.,3*math.pi/4.]
print("b is a list of numbers, b = ",b)
print("\n")

c = numpy.array([0,math.pi/4.,math.pi/2.,3*math.pi/4.],float)
print("c is an array, c = ",c)
print("\n")

d=math.sin(a)
print("To find the sine of a number use math.sin")
print("math.sin(a) = ",d)
print("\n")

print("To use math.sin for a list, you have to loop over each individual entry in the list:")
f=[]
for i in b:
    y=math.sin(i)
    print("Taking sin(",i,") = ",y)
    f.append(y)
print("Now we have a list of the sin values:",f)
print("\n")

print("This also works on an array:")
h = numpy.zeros(4,float)
for i in range(len(c)):
    y=math.sin(c[i])
    print("Taking sin(",c[i],") = ",y)
    h[i] = y
print("Now we have an array of the sin values:",h)
print("\n")

print("Or, you can use map to do the same thing: list(map(math.sin,b)) returns the list of sin values:")
g = list(map(math.sin,b))
print(g)
print("\n")


print("Another way to find the sine of a list or an array is to use numpy.sin")
print("numpy.sin(b) returns an array")
j=numpy.sin(b)
print(j)
print("numpy.sin(c) also returns an array")
k=numpy.sin(c)
print(k)
print("Also you can use numpy.sin on a number! numpy.sin(a) = ",numpy.sin(a))

