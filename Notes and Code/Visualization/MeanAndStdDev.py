import math
import numpy

x = numpy.loadtxt("grades.txt",float)

print("First, find the mean by summing over values in the list and dividing by the number of entries:")

xsum=0.0
for a in x:
    xsum+=a
mean1=xsum/len(x)
print(mean1)

print("But there's a function that does this automatically! numpy.mean(x)")
print(numpy.mean(x))

print("Now, find the standard deviation by looping over the list and using the formula:")
xsum=0.0
for a in x:
    xsum+=((a - mean1)**2)
sd1=math.sqrt(xsum/(len(x)))
print(sd1)

print("But there's a function that does this automatically! numpy.std(x)")
print(numpy.std(x))

