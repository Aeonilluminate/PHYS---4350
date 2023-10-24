import matplotlib.pyplot as plt
import numpy as np

x = np.loadtxt("grades.txt",float)
print(x)

#now the list x is a list of numbers we can use to make a histogram
plt.hist(x,10)#make a histogram with x, 10 bins
plt.xlabel("Grades")#axis labels
plt.ylabel("Entries")
plt.title("Grade Distribution")#title
plt.show()

