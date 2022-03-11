import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import pi

#wave speed
c = 1

#spatial domain
xmin = 0
xmax = 1

# time domain
m = 20000  # num of time steps
tmin = 0
tmax = 500
T = tmin + np.arange(m + 1)

n = 500  # grid points

# x grid of n points
X, dx = np.linspace(xmin, xmax, n + 1, retstep=True)
X = X[:-1]  # remove last point, as u(x=1,t)=u(x=0,t)

# for CFL of 0.3
dt = 0.3 * dx / c


# initial conditions
def initial_u(x):
    # return np.sin(2 * pi * x)
    # return np.exp(-0.5*np.power(((x-0.5)/0.08), 2))
    return np.cos(2*np.pi*x*x)
    # return np.sin(x)*np.sin(x) + np.cos(x)*np.cos(x)
    # return 3415*np.cos(6.412*x)


# each value of the U array contains the solution for all x values at each timestep
U = np.zeros((m + 1, n), dtype=float)
U[0] = u = initial_u(X)


def rugne(t, u, c, dx):
    du = np.zeros(len(u))
    p = c / (2 * dx)
    du[0] = p * (u[1] - u[-1])
    du[1:-1] = p * (u[2:] - u[:-2])
    du[-1] = p * (u[0] - u[-2])
    return du

# timesteps
for k in range(m):
    t = T[k]
    k1 = rugne(t, u, c, dx) * dt
    k2 = rugne(t + 0.5 * dt, u + 0.5 * k1, c, dx) * dt
    k3 = rugne(t + 0.5 * dt, u + 0.5 * k2, c, dx) * dt
    k4 = rugne(t + dt, u + k3, c, dx) * dt
    U[k + 1] = u = u + (k1 + 2 * k2 + 2 * k3 + k4) / 6

# plot properties
plt.style.use('dark_background')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# animate
k = 0


def animate(i):
    global k
    x = U[k]
    k += 25
    ax1.clear()
    plt.plot(X, x, color='cyan')
    plt.grid(True)
    plt.ylim([-2, 2])
    plt.xlim([0, 1])


anim = animation.FuncAnimation(fig, animate, frames=360, interval=20)
plt.show()
