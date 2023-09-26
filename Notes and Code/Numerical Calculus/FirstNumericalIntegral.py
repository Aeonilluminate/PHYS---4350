import numpy
import matplotlib.pyplot as plt
import math

#define a function to calculate the area of each slice
def area(f1,f2,dx):
    a=0.5*(f1+f2)*dx
    return a

#define our function
def f(x):
    return math.sin(x)    

print("If we integrate f(x) = sin(x) from x=0 to x=pi analytically, we get 2")
#-cos(pi) - (-cos(0)) = -(-1) - (-1) = 1 + 1 = 2
print("Now let's do it using the trapezoidal rule:")

#define our integral bounds
a=0
b=math.pi
#define our slices
n = 4
dx=(b-a)/n
x=numpy.arange(a,b,dx)
if n<10:
    print("These are the left-side boundaries for each slice: ",x)

sum=0.
for val in x:
    f1=f(val)
    f2=f(val+dx)
    a=area(f2,f2,dx)
    sum+=a

print("Numerical integral with ",n, "slices is ",sum)

#draw sin(x) and shade area under the curve
xmin=0
xmax=2*math.pi
npoints = 1000
delta=(xmax-xmin)/npoints
px=numpy.arange(xmin,xmax,delta)
py=numpy.sin(px)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("f(x) = sin(x)")
plt.plot(px,py,"-",lw=2)
plt.axhline(y=0,color="black")
plt.fill_between(px,0,py,where=py>0)
plt.show()
