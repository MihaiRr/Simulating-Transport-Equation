import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

c = 1

xmin = 0
xmax = 1

# xmin = 0
# xmax = 0.176


n = 100  # grid points

# x grid of n points
X, dx = np.linspace(xmin, xmax, n, retstep=True)

# CFL of 0.1
dt = 0.1 * dx / c


# initial conditions
def initial_u(x):
    # return np.exp(-0.5*np.power(((x-0.5)/0.08), 2))
    # return np.sin(2 * np.pi * x)
    return np.cos(2*np.pi*x*x)
    # return 3415*np.cos(6.412*x)



# each value of the U array contains the solution for all x values at each timestep
U = []


# euler solution
def euler(x, t):
    if t == 0:  # initial condition
        return initial_u(x)
    uvals = []  # u values for this time step
    for j in range(len(x)):
        if j == 0:  # left boundary
            uvals.append(U[t - 1][j] + c * dt / (2 * dx) * (U[t - 1][j + 1] - U[t - 1][n - 1]))
        elif j == n - 1:  # right boundary
            uvals.append(U[t - 1][j] + c * dt / (2 * dx) * (U[t - 1][0] - U[t - 1][j - 1]))
        else:
            uvals.append(U[t - 1][j] + c * dt / (2 * dx) * (U[t - 1][j + 1] - U[t - 1][j - 1]))
    return uvals


# timesteps
for t in range(5000):
    U.append(euler(X, t))



# plot properties
plt.style.use('dark_background')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# animate
k = 0


def animate(i):
    global k
    x = U[k]
    k += 10
    ax1.clear()
    plt.plot(X, x, color='cyan')
    plt.grid(True)
    plt.ylim([-2, 2])
    plt.xlim([0, 1])
    # plt.ylim([0, 5000])
    # plt.xlim([0, 0.20])


anim = animation.FuncAnimation(fig, animate, frames=360, interval=20)
plt.show()
