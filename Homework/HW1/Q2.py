import math
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('IAHTemp.txt', float)
n = len(data)

mu = np.mean(data)
sigma = np.std(data)

binwidth = 5.0
b = np.arange(40, 90, binwidth)

w = [1./(n*binwidth) for i in range(n)]

t = 0
T = []
AVG_TEMP = []

while t < len(data):
    avg_temp = sum(data[0:t])/(t + 1)
    AVG_TEMP.append(avg_temp)
    T.append(t)
    t += 1


plt.figure(1)
plt.hist(data, bins=b, edgecolor='black')  # 'bins' determines the number of bins in the histogram
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.figure(2)
plt.hist(data, weights=w, bins=b, edgecolor='black')  # 'bins' determines the number of bins in the histogram
plt.title('Probability Distribution')
plt.xlabel('Value')
plt.ylabel('Probability')

xval = np.arange(40, 90, 0.2)
f = (1./(sigma*math.sqrt(2.*math.pi)))*np.exp(-1.*(xval-mu)**2/(2.*sigma**2))

plt.plot(xval, f, '-', lw=2, color='red')

plt.figure(3)
plt.plot(T, AVG_TEMP)
plt.title('Average Temperature vs Time')
plt.xlabel('Time (months)')
plt.ylabel('Temperature')


plt.show()