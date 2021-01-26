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

maxevals = cfg['maxevals']
size = cfg['size']
dim = cfg['dim']
omega = cfg['omega']
phip = cfg['phip']
phig = cfg['phig']
lr = cfg['lr']
save = int(sys.argv[3]) if sys.argv[3] else False
data = int(sys.argv[4]) if sys.argv[4] else False
gif = int(sys.argv[5]) if sys.argv[5] else False
nBest = cfg['nBest']

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
pso(fnct, blo, bup, maxevals, size, dim, omega, phip, phig, lr, gif, data, log, nBest)
t2 = time.time()

log.simpleData = [fnctName, float(blo), float(bup), maxevals, size, dim, omega, phip, phig, lr, t2 - t1]
log.gen_graphs(best_list, **g1Args)
log.save(f'./ejecuciones', save, data)
