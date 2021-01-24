import sys
import numpy as np
from functions import *

class Particle:

    def __init__(self):
        self.fitness = 0

def createPop(size):
    pop = []

    for _ in range(size):
        pop.append(Particle())

    return pop
