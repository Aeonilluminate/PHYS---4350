def f(x):
    return x**5
def fp(x):
    return 5*x**4
def fpp(x):
    return 20*x**3

a=0.5
h=1e-5

forward=(f(a+h) - f(a))/h
e = 0.5*h*fpp(a)
r = 2*1e-16*f(a)/h
t = fp(0.5)

print("Numerical approximation = ",round(forward,8))
print("True value = ",round(t,8))
print("Difference = ",round(forward-t,8))
print("Note that the approximation error is 0.5*h*f''(x) = ",e)
print("The rounding error is much smaller, ~",r)
