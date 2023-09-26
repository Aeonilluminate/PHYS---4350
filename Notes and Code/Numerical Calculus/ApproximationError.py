import numpy
import matplotlib.pyplot as plt
import math

#define a function to calculate the area of each slice
def area(f1,f2,dx):
    return 0.5*(f1+f2)*dx

#define our function
def f(x):
    return math.sin(x)

#define the derivative
def fprime(x):
    return math.cos(x)

print("If we integrate f(x) = sin(x) from x=0 to x=pi analytically, we get 2")
#-cos(pi) - (-cos(0)) = -(-1) - (-1) = 1 + 1 = 2
print("Now let's do it using the trapezoidal rule:")

#define our integral bounds
a=0
b=math.pi

#define our slices
n1 = 10
dx1=(b-a)/n1
x1=numpy.arange(a,b,dx1)
n2=2*n1
dx2=(b-a)/n2
x2=numpy.arange(a,b,dx2)

sum1=0.
for val in x1:
    f1=f(val)
    f2=f(val+dx1)
    sum1+=area(f1,f2,dx1)

sum2=0
for val in x2:
    f1=f(val)
    f2=f(val+dx2)
    sum2+=area(f1,f2,dx2)

print("Numerical integral with ",n1, "slices is ",sum1)
print("Numerical integral with ",n2, "slices is ",sum2)

#Three ways to get error
print("True value - approximation #2:",2-sum2)

epsilon=(1/12)*(dx2**2)*(fprime(a) - fprime(b))
print("Using error formula based on derivatives:",epsilon)

epsilon2=(1/3)*(sum2-sum1)
print("Using error formula based on two results:",epsilon2)


