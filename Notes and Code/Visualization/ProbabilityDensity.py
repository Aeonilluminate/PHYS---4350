import matplotlib.pyplot as plt
import numpy as np
import math

x = np.loadtxt("height.txt",float)
n = len(x)

#Get mean and standard deviation
mu=np.mean(x)
sigma=np.std(x)

#set desired bin width
binwidth=2.0
#makes a list of numbers 60,62,64,...80 to use as the bin edges
b=np.arange(60.,80.,binwidth)

#to make a probability density, we need to weight each entry by 1/(n*binwidth)
#this is equivalent to divide the content in each bin by n and the binwidth
w=[1./(n*binwidth) for i in range(n)]#this command makes a list where every entry is 1/(n*binwidth)

#create the histogram
plt.hist(x,weights=w,bins=b)

#to compare to a Gaussian with the same parameters
xval = np.arange(60.,80.,0.2)#sets x values
#evaluate Gaussian function at each x value, using the mu and sigma previously defined
f = (1./(sigma*math.sqrt(2.*math.pi)))*np.exp(-1.*(xval-mu)**2/(2.*sigma**2))

#create the graph
plt.plot(xval,f, '-',lw=2,color="red")

#Label axes
plt.xlabel("Height (in)")
plt.ylabel("Probability Density")

#save the figure
plt.savefig("ProbabilityDensity.png")

#draw the plot
plt.show()
