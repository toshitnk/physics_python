import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
from scipy.integrate import solve_ivp
import ode


def diff(t, x):
    f = x
    return f



if __name__ == "__main__":
    
    t = np.linspace(0, 5, 100)
    x = np.exp(t)
    plt.plot(t, x, label=r"$x = e^t$")
    ode.runge_kutta(diff, 1, 0, 5, 0.01, line=True)
    plt.show()
