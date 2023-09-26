import math
import matplotlib.pyplot as plt

def prob(n,k):
    nfac=math.factorial(n)
    kfac=math.factorial(k)
    nmkfac=math.factorial(n-k)
    return (nfac/(kfac*nmkfac))/2**n


print(prob(100,50))

