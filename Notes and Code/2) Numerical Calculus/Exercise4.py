#here's my list:
a = [5.001, 5.000002, 4.739, 4.999999999999999, 5.28, 4.5, 6.2]
print(a)

#here we search through the list
diff=10
closest=10
for i in a:
    if abs(i-5)<diff:
        diff=abs(i-5)
        closest=i
print("closest value to 5 in this list is: ",closest)


