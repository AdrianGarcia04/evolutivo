import yaml
import sys
import matplotlib.pyplot as plt

from functions import fncts
from Particle import *

def savefig(i):
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
    plt.clf()

cfg = yaml.safe_load(open(sys.argv[1], 'r'))

fnctName = sys.argv[2] or cfg['functions']['using']
fnct = fncts[fnctName]
blo = cfg['functions'][fnctName]['blo']
bup = cfg['functions'][fnctName]['bup']

maxevals = cfg['maxevals']
size = cfg['size']
dim = cfg['dim']
omega = cfg['omega']
phip = cfg['phip']
phig = cfg['phig']
lr = cfg['lr']

(swarm, swarmBest) = createSwarm(size, dim, blo, bup, fnct)
eval = 0
while eval < maxevals:
    print(f'Eval: {eval} - {maxevals}', end='\r')
    for particle in swarm:
        newVelocity = np.zeros(shape=dim)
        for d in range(dim):
            rp = np.random.uniform()
            rg = np.random.uniform()

            currentPosD = particle.position[d]
            currentVelD = particle.velocities[d]
            bestPosD = particle.personalBest[d]

            diffP = bestPosD - currentPosD
            diffB = swarmBest[d] - currentPosD
            newVelocity[d] = omega * currentVelD + (phip * rp * (diffP)) + (phig * rg * (diffP))


        particle.velocities = newVelocity
        particle.position = particle.position + lr * particle.velocities

        fitnessVal = particle.fitness(fnct)
        bestFitnessVal = particle.bestFitness(fnct)

        if fitnessVal < bestFitnessVal:
            particle.personalBest = particle.position

            if bestFitnessVal < fnct(swarmBest[0], swarmBest[1]):
                swarmBest = particle.personalBest
    eval += 1
    savefig(eval)
