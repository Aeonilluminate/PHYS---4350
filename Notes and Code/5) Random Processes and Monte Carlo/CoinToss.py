import random as rd

p=0.5
nheads=0
for i in range(100):
    val=rd.random()
    #print(val)
    if(val<p):
        nheads+=1

print("Heads with p=0.5:",nheads)

p=0.3
nheads=0
for i in range(100):
    val=rd.random()
    #print(val)
    if(val<p):
        nheads+=1

print("Heads with p=0.3:",nheads)
