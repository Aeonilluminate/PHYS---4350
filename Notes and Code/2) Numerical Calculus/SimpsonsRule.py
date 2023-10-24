import numpy
import matplotlib.pyplot as plt
import math
import sys

#define our function
def f(x):
    return math.sin(x)    

print("If we integrate f(x) = sin(x) from x=pi/4 to x=pi/2 analytically, we get 1/sqrt(2) = ",1/math.sqrt(2))
#-(cos(pi/2) - cos(pi/4)) = -(0-1/sqrt(2)) = 1/sqrt(2)
print("Now let's do it using Simpson's rule:")

#define our integral bounds
a=math.pi/4
b=math.pi/2

#define the number of slices
n = 2
if(n%2==1):
    print("n must be even!")
    sys.exit()

#define Delta-x
dx=(b-a)/n

#create an array for all the points we need to evalute
# with n slices, that's n+1 points
x=numpy.linspace(a,b,n+1)
#creates an array with n+1 points evenly spaced between a and b
print(x)
#x[0] = a, x[1] = a+dx, x[2] = a+2dx, x[3] = a+3dx, ...

sum=0.
for i in range(n+1):#i will take n+1 values from 0 to n
    if i==0 or i==n: #x[0] = a, x[n] = b
        sum+= f(x[i])
    if i>0 and i%2==1: #odd values between 1 and n-1
        sum+= 4*f(x[i])
    if i>0 and i<n and i%2==0: #even values between 2 and n-2
        sum+= 2*f(x[i])
sum = sum*dx/3 # don't forget to multiply by (1/3)Delta-x

val=1/math.sqrt(2)
w=100*(sum-val)/val
       
print("Numerical integral with ",n, "slices is ",sum)
print("Percent difference from true value is:",w,"%")


