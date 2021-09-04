import numpy as np
import matplotlib.pyplot as plt
import random
import time

# # plt.rcParams['font.family'] = 'Arial'
# plt.rcParams['mathtext.fontset'] ='cm'
# plt.rcParams['xtick.labelsize'] = 15
# plt.rcParams['ytick.labelsize'] = 15
# plt.rcParams['xtick.direction'] = 'in'
# plt.rcParams['ytick.direction'] = 'in'
# plt.rcParams['xtick.major.size'] = 12
# plt.rcParams['ytick.major.size'] = 12
# plt.rcParams['xtick.major.pad'] = 18
# plt.rcParams['ytick.major.pad'] = 18
# plt.rcParams['axes.linewidth'] = 1.0
# plt.rcParams['figure.subplot.bottom'] = 0.2
# plt.rcParams['figure.subplot.left'] = 0.2


def montecalro_pi(Nmax):
    cnt = 0
    x_plot = []
    y_plot = []

    for i in list(range(1,Nmax+1)):
        x = random.random()
        y = random.random()

        if x ** 2 + y ** 2 < 1:
            cnt = cnt + 1
        
        # x_plot.append(x)
        # y_plot.append(y)

    # plt.scatter(x_plot, y_plot, label="Monte-carlo N=%i"%(Nmax),marker=".")
    return cnt / Nmax * 4


start = time.time()

Nlist = []
pilist = []
for N in list(range(100, 100000, 100)):
    pi = montecalro_pi(N)
    Nlist.append(N)
    pilist.append(pi)

# 時間を計測
elapsed_time = time.time() - start
print(elapsed_time)


plt.plot(Nlist, pilist)
plt.axhline(np.pi)
# plt.ylim(0,5)
plt.show()



# pi10 = montecalro_pi(10)
# print(pi10)

# pi100 = montecalro_pi(100)
# print(pi100)

# ang = np.arange(0,np.pi/2,0.1)
# x_plot = np.cos(ang)
# y_plot = np.sin(ang)

# plt.plot(x_plot, y_plot, color="red")
# plt.xlim(-0.05,1.5)
# plt.ylim(-0.05,1.5)
# plt.legend()
# plt.show()

