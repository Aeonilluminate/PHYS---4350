import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return math.sqrt(x*math.sin(x))

def fp(x):
    return (math.sin(x) + x*math.cos(x))/(2*math.sqrt(x*math.sin(x)))

def central_difference(f, x, h):
    return (f(x + h/2) - f(x - h/2))/h

def error(x, h, f, fp):
    return abs(fp(x) - central_difference(f=f, x=x, h=h))


N = 10000
INTERVAL = [-3, 3]
h = 0.1
X = np.linspace(-3, 3, N)
Y  = [f(x) for x in X]
Yp = [fp(x) for x in X]

epsilon = error(x=-3, h=h, f=f, fp=fp)

while epsilon > 1e-5:
    h *= 0.99999
    epsilon = error(x=-3, h=h, f=f, fp=fp)

approx_fp = central_difference(f=f, x=-3, h=h)
actual_fp = fp(x=-3)

print(f'''
Central Difference Result: {approx_fp}
True Value: {actual_fp}
Approximate Error: {epsilon}
Value of h: {h}''')


fig, (F, Fp) = plt.subplots(nrows = 2, ncols = 1, sharex = True)

F.set_title(r'$f(x)$')
F.set_xlabel(r'$x$')
F.set_ylabel(r'$\sqrt{x\sin (x)}$')
F.plot(X, Y)


Fp.plot(X, Yp)
Fp.set_title(r"$f'(x)$")
Fp.set_xlabel(r'$x$')
Fp.set_ylabel(r'$\frac{\sin (x) + x\cos (x)}{2\sqrt{x\sin (x)}}$')

plt.style.use('seaborn')
plt.tight_layout()

plt.show()