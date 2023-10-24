import numpy
import matplotlib.pyplot as plt
import math

#define a function to calculate the area of each slice
def area(f1,f2,dx):
    a=0.5*(f1+f2)*dx
    return a

#define our function
def f(x):
    mu=100
    sigma=10
    y =(1./(sigma*math.sqrt(2.*math.pi)))*math.exp(-1.*(x-mu)**2/(2.*sigma**2))
    return y   

#define our integral bounds
#can't realistically go from negative infinty to positive infinity
#need to choose bounds that are "far enough" away from the mean
a=50
b=150
#define our slices
n = 5
dx=(b-a)/n
x=numpy.arange(a,b,dx)

sum=0.
for val in x:
    f1=f(val)
    f2=f(val+dx)
    a=area(f2,f2,dx)
    sum+=a

print("Numerical integral from",a,"to",b,"with ",n, "slices is ",sum)

mu=100.
sigma=10.

x1 = numpy.arange(0.,200.,1.)
y1 = (1./(sigma*math.sqrt(2.*math.pi)))*numpy.exp(-1.*(x1-mu)**2/(2.*sigma**2))

plt.plot(x1,y1,"-",lw=2)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gaussian PDF with $\mu=100$ and $\sigma=10$")
plt.text(0,0.035,r'$f(x) = \frac{1}{\sigma \sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$',fontsize=16)
plt.show()
