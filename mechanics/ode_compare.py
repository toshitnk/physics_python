import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# exact solution
t_exact = np.linspace(0, 1, 100)
x_exact = np.exp(-2 * (t_exact - 1) ** 2)
plt.plot(t_exact, x_exact, label="Exact")



# given differential function
def diff(t, x):
    f = -4 * (t-1) * x
    return f
# euler method

def euler_method(x_init, t_min, t_max, h, line=False):
    Nmax = int((t_max - t_min)/h)
    t_plot = [t_min]
    x = x_init
    x_plot = [x_init]
    for i in range(1, Nmax+1):
        t = t_min + i * h
        x = x + (diff(t, x)) * h
        
        t_plot.append(t)
        x_plot.append(x)

    if line==True:
        plt.plot(t_plot, x_plot, label="Euler h=%s"%(h))
                
    elif line==False:
        plt.plot(t_plot, x_plot, linestyle="None", marker="o", label="Euler h=%s"%(h))

def heun_method(x_init, t_min, t_max, h, line=False):
    Nmax = int((t_max - t_min)/h)
    t_plot = [t_min]
    x = x_init
    x_plot = [x_init]
    for i in range(1, Nmax+1):
        t = t_min + i * h
        k1 = diff(t, x) * h
        k2 = diff(t, x+k1) * h
        x = x + 0.5 * (k1 + k2)

        t_plot.append(t)
        x_plot.append(x)
    if line==True:
        plt.plot(t_plot, x_plot, label="Heun h=%s"%(h))
                
    elif line==False:
        plt.plot(t_plot, x_plot, linestyle="None", marker="o", label="Heun h=%s"%(h))

def runge_kutta(x_init, t_min, t_max, h, line=False):
    Nmax = int((t_max - t_min)/h)
    t_plot = [t_min]
    x = x_init
    x_plot = [x_init]
    for i in range(1, Nmax):
        t = t_min + i * h
        t_med = t- 0.5 * h

        k1 = diff(t,x) * h
        k2 = diff(t_med, x+0.5*k1) * h
        k3 = diff(t_med, x+0.5*k2) * h
        k4 = diff(t+h, x+0.5*k3) * h

        x = x + (k1 + 2*k2 + 2*k3 + k4)/6

        t_plot.append(t)
        x_plot.append(x)
    if line==True:
        plt.plot(t_plot, x_plot, label="RK h=%s"%(h))
                
    elif line==False:
        plt.plot(t_plot, x_plot, linestyle="None", marker="o", label="RK h=%s"%(h))



if __name__ == "__main__":

    euler_method(np.exp(-2), 0.0, 1.0, 0.01, line=True)
    #euler_method(np.exp(-2), 0.0, 1.0, 0.01)
    #euler_method(np.exp(-2), 0.0, 1.0, 0.1)
    
    heun_method(np.exp(-2), 0.0, 1.0, 0.01, line=True)
    
    runge_kutta(np.exp(-2), 0.0, 1.0, 0.01, line=True)

    
    # scipyをつかう．
    t = np.arange(0.0, 1.0, 0.01)
    x = odeint(diff, np.exp(-2),t )
    plt.plot(t, x, label="scipy RK45")


    plt.legend()
    plt.savefig("ode_compare.png")
