import math

print("Let f(x) = x^6 + 5x^3 and evaluate derivative at x=0.2.")

def f(x):
    return (x**6 + 5*x**3)
def fp(x):
    return (6*x**5 + 15*x**2)
def fpp(x):
    return (30*x**4 + 30*x)
def fppp(x):
    return (120*x**3 + 30)

a=0.2

print("True value of derivative = ",fp(a))
print()

C=1e-16
h=0.01
forward=(f(a+h) - f(a))/h
print("Integral estimated by foward difference with h=0.001 = ",forward)

h=math.sqrt(4*C*f(a)/fpp(a))
forward=(f(a+h) - f(a))/h
print("Optimal value of h = ",h)
print("Integral estimated by forward difference with optimal value of h = ",forward)
e = 0.5*h*fpp(a)
r = 2*1e-16*f(a)/h
print("The approximation error is 0.5*h*f''(x) = ",e)
print("The rounding error is ~",r)

print()

h=0.01
central=(f(a+h/2) - f(a-h/2))/h
print("Integral estimated by central difference with h=0.001 = ",central)
h=(24*C*f(a)/fppp(a))**(1/3)
central=(f(a+h/2) - f(a-h/2))/h
print("Optimal value of h = ",h)
print("Integral estimated by central difference with optimal value of h = ",central)
e = (1/24)*(h**2)*fppp(a)
r = 2*1e-16*f(a)/h
print("The approximation error is (1/24)*h^2*f'''(x) = ",e)
print("The rounding error is ~",r)
