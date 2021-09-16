import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# solve_ivpに渡す関数

def Fun(t, y, a, b):
    x = y[0]
    v = y[1]

    F1 = v
    F2 = -x - a*v + b*np.cos(t)

    return [F1, F2]

t_init = 0
y_init = [3, 0]

t_end = 20
t_span = [t_init, t_end]
t_list = np.linspace(t_init, t_end, 21)

a = 0.5
b = 0.2

sol = solve_ivp(Fun, t_span, y_init, t_eval=t_list, args=(a,b))

plt.plot(sol.t, sol.y[0])
plt.show()
