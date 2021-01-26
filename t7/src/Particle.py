import sys
import numpy as np
import math

class Particle:

    def __init__(self, dim, blo, bup):
        self.fitnessVal = 0
        self.bestFitnessVal = 0
        self.position = np.random.uniform(low=blo, high=bup, size=dim)
        self.velocities = np.random.uniform(low=blo, high=bup, size=dim)
        self.personalBest = self.position

    def fitness(self, fnct):
        self.fitnessVal = fnct(self.position[0], self.position[1])
        return self.fitnessVal

    def bestFitness(self, fnct):
        self.bestFitnessVal = fnct(self.personalBest[0], self.personalBest[1])
        return self.bestFitnessVal

def createSwarm(size, dim, blo, bup, fnct):
    swarm = []
    swarmBest = np.empty(shape=dim)
    swarmBest.fill(999)

    for _ in range(size):
        p = Particle(dim, blo, bup)
        pFitness = p.fitness(fnct)

        if pFitness < fnct(swarmBest[0], swarmBest[1]):
            swarmBest = p.position

        swarm.append(p)

    return (swarm, swarmBest)
