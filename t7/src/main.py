import yaml
import sys
from Logger import Logger
from functions import fncts
from PSO import pso
import time

cfg = yaml.safe_load(open(sys.argv[1], 'r'))

fnctName = sys.argv[2] or cfg['functions']['using']
fnct = fncts[fnctName]
blo = cfg['functions'][fnctName]['blo']
bup = cfg['functions'][fnctName]['bup']

maxevals = int(sys.argv[3]) if sys.argv[3] else cfg['maxevals']
size = int(sys.argv[4]) if sys.argv[4] else cfg['size']
dim = int(sys.argv[5]) if sys.argv[5] else cfg['dim']
omega = float(sys.argv[6]) if sys.argv[6] else cfg['omega']
phip = float(sys.argv[7]) if sys.argv[7] else cfg['phip']
phig = float(sys.argv[8]) if sys.argv[8] else cfg['phig']
lr = float(sys.argv[9]) if sys.argv[9] else cfg['lr']
nBest = int(sys.argv[10]) if sys.argv[10] else cfg['nBest']
save = int(sys.argv[11]) if sys.argv[11] else False
data = int(sys.argv[12]) if sys.argv[12] else False
gif = int(sys.argv[13]) if sys.argv[13] else False

log = Logger()

best_list = [f'iter-best{i}' for i in range(nBest)] + ['iter-avg']
log.add_dictionaries(best_list)

aux_labels = ['Segunda', 'Tercera', 'Cuarta', 'Quinta', 'Sexta', 'Séptima']
best_list_labels = ['Mejor solución'] + [f'{aux_labels[j]} mejor solución' for j in range(nBest - 1)]

g1Args = {
    'title': f'{nBest} mejores soluciones y promedio',
    'xlabel': 'Número de iteraciones',
    'ylabel': 'Función fitness',
    'labels': best_list_labels + ['Promedio'],
    'id': 'GraphFitness'
}


t1 = time.time()
best = pso(fnct, blo, bup, maxevals, size, dim, omega, phip, phig, lr, gif, data, log, nBest)
t2 = time.time()

log.simpleData = [fnctName, float(blo), float(bup), maxevals, size, dim, omega, phip, phig, lr, t2 - t1, best]
log.gen_graphs(best_list, **g1Args)
if save or data:
    log.save(f'./ejecuciones', save, data)
