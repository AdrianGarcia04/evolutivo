import sys
import numpy as np
import math

class Particle:

    def __init__(self, dim, bound):
        self.fitnessVal = 0
        self.bestFitnessVal = 0
        self.position = np.random.uniform(low=-bound, high=bound, size=dim)
        self.velocities = np.random.uniform(low=-bound, high=bound, size=dim)
        self.personalBest = self.position

    def fitness(self, fnct):
        self.fitnessVal = fnct(self.position)
        return self.fitnessVal

    def bestFitness(self, fnct):
        self.bestFitnessVal = fnct(self.personalBest)
        return self.bestFitnessVal

    def getPosition(self):
        return self.position

    def getVelocity(self):
        return self.velocities

    def getBestPosition(self):
        return self.personalBest

    def setPosition(self, new):
        self.position = new

    def setBestPosition(self, new):
        self.personalBest = new

    def setVelocityOnD(self, d, new):
        if 0 <= d < len(self.velocities):
            self.velocities[d] = new

    def getVelocityOnD(self, d):
        if 0 <= d < len(self.velocities):
            return self.velocities[d]
        return None

    def getPositionOnD(self, d):
        if 0 <= d < len(self.position):
            return self.position[d]
        return None

    def getBestPositionD(self, d):
        if 0 <= d < len(self.personalBest):
            return self.personalBest[d]
        return None

def createSwarm(size, dim, bound, fnct):
    swarm = []
    swarmBest = np.empty(shape=dim)
    swarmBest.fill(999)

    for _ in range(size):
        p = Particle(dim, bound)
        pFitness = p.fitness(fnct)

        if pFitness < fnct(swarmBest):
            swarmBest = p.position

        swarm.append(p)

    return (swarm, swarmBest)
