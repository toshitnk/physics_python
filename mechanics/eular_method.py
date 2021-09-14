import numpy as np
import matplotlib.pyplot as plt

# exact solution
t_exact = np.linspace(0, 1, 100)
x_exact = np.exp(-2 * (t_exact - 1) ** 2)
plt.plot(t_exact, x_exact, label="Exact")


# euler method

def euler_method(x_inti, t_min, t_max, h, line=False):
    Nmax = int((t_max - t_min)/h)
    t_plot = [t_min]
    x = x_inti
    x_plot = [x_inti]
    for i in range(1, Nmax+1):
        t = t_min + i * h
        x = x + (-4 * (t-1) * x) * h
        
        t_plot.append(t)
        x_plot.append(x)

    if line==True:
        plt.plot(t_plot, x_plot, label="Euler h=%s"%(h))
                
    elif line==False:
        plt.plot(t_plot, x_plot, linestyle="None", marker="o", label="Euler h=%s"%(h))

if __name__ == "__main__":

    euler_method(np.exp(-2), 0.0, 1.0, 0.001, line=True)
    euler_method(np.exp(-2), 0.0, 1.0, 0.01)
    euler_method(np.exp(-2), 0.0, 1.0, 0.1)
    
    plt.legend()
    plt.savefig("Euler_method.png")
