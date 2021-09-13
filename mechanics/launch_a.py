import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm

fig, ax = plt.subplots()

g = 9.8

def plot():
    plt.cla()

    global g
    
    x = []
    y = []
    imgs = []

    for i in range(20):
        xel = 100 * i
        yel = 100 * i - 0.5 * g * i ** 2

        x.append(xel)
        y.append(yel)

        #ax.set_xlim(0, 20)
        #ax.set_ylim(0, 6)

        img = ax.plot(x[i], y[i], "b-o")
        imgs.append(img)
    return imgs

if __name__ == "__main__":
    imgs = plot()
    ani = anm.ArtistAnimation(fig, imgs, interval=100)
    ani.save("launch.gif", writer="imagemagick")
