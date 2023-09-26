import numpy
import matplotlib.pyplot as plt
import math

#define a function to calculate the area of each slice
def area(f1,f2,dx):
    return 0.5*(f1+f2)*dx

#define our function
def f(x):
    return math.sin(x)

#dfine target accuracy
targetepsilon=0.0001
print("target accuracy = ",targetepsilon)

#define parameters to compute I1
a=0
b=math.pi
n1 = 10
dx1=(b-a)/n1
x1=numpy.arange(a,b,dx1)

I1=0.
for val in x1:
    f1=f(val)
    f2=f(val+dx1)
    I1+=area(f1,f2,dx1)

print("First approximation = ",I1)

#old means (i-1)the term, new means ith term
nold=n1
nnew=0.
dxold=dx1
dxnew=0.
Iold=I1
Inew=0.
epsilon=1000.
while epsilon>targetepsilon:
    nnew=nold*2
    dxnew=dxold/2
    s=0
    for i in range(1,nnew,2):#1,3,5,...nnew-1
       s+=f(a+i*dxnew)
    s*=dxnew
    Inew=0.5*Iold+s
    epsilon=(Inew-Iold)/3
    nold=nnew
    dxold=dxnew
    Iold=Inew

print("Final approximation = ",Inew,"error = ",epsilon)
print("number of final slices = ",nnew)




