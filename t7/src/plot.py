import numpy as np
import matplotlib.pyplot as plt

def savefig(i, blo, bup, fnct, swarm):
    x = np.linspace(blo, bup, 100)
    y = np.linspace(blo, bup, 100)
    x, y = np.meshgrid(x, y)
    z = fnct(x, y)

    contours = plt.contour(x, y, z, 3, colors='black')
    plt.clabel(contours, inline=True, fontsize=8)
    plt.imshow(z, extent=[blo, bup, blo, bup], origin='lower',
    cmap='RdGy', alpha=0.5)
    plt.colorbar()
    for particle in swarm:
        plt.annotate("x", particle.position)

    plt.savefig('./figs/{:02}.png'.format(i))
    plt.savefig('./figs/{:02}.png'.format(i + 1))
    plt.savefig('./figs/{:02}.png'.format(i + 2))
    plt.clf()
