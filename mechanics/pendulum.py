import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import ode
from scipy.integrate import solve_ivp

# physics constant
g = 9.8 #[m s^{-2}]
l = 1.0 #[m]

fig, ax = plt.subplots()

# equation of motion

def pendulum(t, y):
    theta = y[0]
    omega = y[1]

    diff1 = omega
    diff2 = -g*np.sin(theta)/l

    return [diff1, diff2]

# initial value

theta_init = 0.5
omega_init = 0.0
y_init = [theta_init, omega_init]

t_span = [0, 20]
t = np.arange(t_span[0], t_span[1], 0.1)


sol = solve_ivp(pendulum, t_span, y_init, t_eval=t)
theta = sol.y[0]

x = l * np.sin(theta)
y = -l * np.cos(theta)

def animate(i):
    plt.cla()
    ax.set_xlim(-l, l)
    ax.set_ylim(-1.2 * l, 0.8 * l)
    ax.set_aspect("equal") 
    x_plot = [0, x[i]]
    y_plot = [0, y[i]]

    ax.plot(x_plot, y_plot, "o-", linewidth=2)


ani = anm.FuncAnimation(fig, animate, frames=20, interval=100)

ani.save("pendulum.gif", writer="imagemagick")
