import yaml
import sys
import matplotlib.pyplot as plt

from functions import fncts
from Particle import *

cfg = yaml.safe_load(open(sys.argv[1], 'r'))

fnctName = cfg['functions']['using']
fnct = fncts[fnctName]
bound = cfg['functions'][fnctName]['bound']

maxevals = cfg['maxevals']
size = cfg['size']
dim = cfg['dim']
omega = cfg['omega']
phip = cfg['phip']
phig = cfg['phig']
lr = cfg['lr']

def funn(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

# fnct = lambda l: funn(l[0], l[1])
bound = 5
(swarm, swarmBest) = createSwarm(size, dim, bound, fnct)
x = np.linspace(-bound, bound, 50)
y = np.linspace(-bound, bound, 50)
x, y = np.meshgrid(x, y)
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
# z = [fnct([x[i], y[i]]) for i in range(1000) ]

plt.contour(x, y, z)
eval = 0
while eval < maxevals:
    print(f'Eval: {eval} - {maxevals}', end='\r')
    for particle in swarm:
        for d in range(dim):
            rp = np.random.uniform()
            rg = np.random.uniform()

            currentPosD = particle.getPositionOnD(d)
            currentVelD = particle.getVelocityOnD(d)
            bestPosD = particle.getBestPositionD(d)

            diffP = bestPosD - currentPosD
            diffB = swarmBest[d] - currentPosD
            new = omega * currentVelD + (phip * rp * (diffP)) + (phig * rg * (diffP))

            particle.setVelocityOnD(d, new)

        particle.setPosition(particle.getPosition() + lr * particle.getVelocity())

        fitnessVal = particle.fitness(fnct)
        bestFitnessVal = particle.bestFitness(fnct)

        if fitnessVal < bestFitnessVal:
            particle.setBestPosition(particle.getPosition())

            if bestFitnessVal < fnct(swarmBest):
                swarmBest = particle.getBestPosition()
    eval += 1
    for particle in swarm:
        plt.annotate("x", particle.position)
    # if eval % 20 == 0:
        # plt.annotate("o", swarmBest)
        # for particle in swarm:

plt.show()
