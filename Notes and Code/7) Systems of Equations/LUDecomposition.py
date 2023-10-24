import numpy as np
import numpy.linalg as la

#2x2 example
a = np.array([[2,3],[4,-6]],float)
v = np.array([4,7],float)

#3x3 example
#a = np.array([[-4,1,-1],[2,-5,2],[6,2,-4]],float)
#v = np.array([8,10,-3],float)

#3x3 with zeroes
#a = np.array([[0,1,4],[0,5,2],[-2,0,-4]],float)
#v = np.array([-9,4,0],float)

print(a)
print()
print(v)
print()


x = la.solve(a,v)
print("Solution is:")
print(x)
print()

#the original matrix times x should yield the original vector v
print("Check the answer:")
print(np.dot(a,x))
