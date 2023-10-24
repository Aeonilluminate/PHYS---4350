import matplotlib.pyplot as plt
import numpy as np

#file contains a two column list of grades
#1st column is final exam grade and 2nd column is semester grade
data = np.loadtxt("grades-2column.txt",float)
#data is a 2D array which has n rows and 2 columns
print(data)

#we need to separate out each column as its own list to use in scatter
x = data[:,0]#takes every row, first column
y = data[:,1]#takes every row, second column
print(x)
print(y)

#first, a scatterplot
plt.figure(1)#use this to make two separate plots
plt.scatter(x,y,marker="o",s=15)
plt.xlabel("Final Exam Grade")#axis labels
plt.ylabel("Semester Grade")
plt.title("Scatterplot: Semester Grade vs Final Exam Grade")#title

#now, a 2d histogram
b = np.arange(0,100,5)
plt.figure(2)
plt.hist2d(x,y,bins=b)
plt.xlabel("Final Exam Grade")#axis labels
plt.ylabel("Semester Grade")
plt.title("2D Histogram: Semester Grade vs Final Exam Grade")#title
plt.colorbar()#show the scale for the colors on the side

plt.show()

