import matplotlib.pyplot as plt
import numpy as np

x = np.loadtxt("grades.txt",float)

#now the list x is a list of numbers we can use to make a histogram
plt.hist(x,bins=[0,10,20,30,40,50,60,70,80,90,100])#make a histogram with x, specify the bin edges
plt.xlabel("Grades")#axis labels
plt.ylabel("Entries")
plt.title("Grade Distribution")#title
plt.text(0,40,"Display text on a plot like this!")
plt.show()

#for n bins, there are n+1 bin edges!!
