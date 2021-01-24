import yaml
import sys
from Particle import *

cfg = yaml.safe_load(open(sys.argv[1], 'r'))

population = Particle.createPop(cfg['size'])

dim = cfg['dim']
# for particle in population:
#     for i in range(dim):
