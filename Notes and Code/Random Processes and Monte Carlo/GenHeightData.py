import random as rd

file1 = open("height.txt","w")

rd.seed(1)

for _ in range(500):
    a = rd.gauss(69.3, 3.0)
    b=round(a,1)
    file1.write(str(b))
    file1.write("\n")
    
file1.close()
