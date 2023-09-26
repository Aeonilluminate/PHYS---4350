import matplotlib.pyplot as plt
import numpy
import math

xmin=0.
xmax=2*math.pi
npoints=500
dx=(xmax-xmin)/npoints
x=numpy.arange(xmin,xmax,dx)
f = numpy.exp(-1.*x)*numpy.sin(10.*x)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) vs x')

plt.plot(x,f, '-',lw=2)
plt.grid(True)
plt.savefig("Exercise1.png")
plt.show()
