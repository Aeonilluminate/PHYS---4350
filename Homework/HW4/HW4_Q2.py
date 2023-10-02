import numpy as np
import math
import matplotlib.pyplot as plt

mu    = [0.1, 1, 10, 8]
A     = [0, 0, 0, 1.2]
omega = [0, 0, 0, 2*np.pi/10]

for i in range(len(mu)):
    mu_i    = mu[i]
    A_i     = A[i]
    omega_i = omega[i]

    def f(r,t):
        x_pos = r[0]
        x_vel = r[1]

        fx = x_vel
        fv = A_i*math.sin(omega_i*t) + mu_i*(1-x_pos**2)*x_vel - x_pos
        return np.array([fx,fv],float)
    
    x0 = 1
    v0 = 0

    t0 = 0
    tf = 150

    h = 0.01
    n = int((tf - t0)/h)

    tpoints = np.linspace(t0,tf,n+1)
    xpoints = []
    vpoints = []
    r=np.array([x0,v0],float)
    for t in tpoints:
        xpoints.append(r[0])
        vpoints.append(r[1])
        k1=h*f(r,t)
        k2=h*f(r+k1/2,t+h/2)
        k3=h*f(r+k2/2,t+h/2)
        k4=h*f(r+k3,t+h)
        r += (1/6)*(k1+2*k2+2*k3+k4)

    plt.plot(tpoints, xpoints)
    plt.title(f'x(t) with $\mu={{{mu_i}}}$, $A={{{A_i}}}$, and $\omega = {{{omega_i}}}$')
    plt.xlabel('t (seconds)')
    plt.ylabel('x(t) (meters)')
    plt.savefig(f'x(t)_mu={mu_i}_A={A_i}_omega={omega_i}.png', dpi=300)

    plt.show()


    plt.plot(xpoints, vpoints)
    plt.title(f'Phase Space with $\mu={{{mu_i}}}$, $A={{{A_i}}}$, and $\omega = {{{omega_i}}}$')
    plt.xlabel('x(t) (seconds)')
    plt.ylabel('v(t) (meters/second)')
    plt.savefig(f'PS_mu={mu_i}_A={A_i}_omega={omega_i}.png', dpi=300)

    plt.show()


print("""
Increasing the parameter mu while holding A at 0 causes the motion of the object to stabilize into a periodic pattern more quickly.
The parameter set given by (d) results in chaotic behavior.""")