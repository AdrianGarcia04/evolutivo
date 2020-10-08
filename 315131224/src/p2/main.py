from Instance import Instance
import sys
import os
import numpy as np
from itertools import tee

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def main(argv):
    assert len(argv) != 0 , 'Se requiere el nombre del archivo'
    assert os.path.isfile(argv[0]), 'El archivo no existe'
    tspInstance = Instance.readFile(argv[0])
    assert tspInstance, 'Error al leer la instancia'

    num_nodes = len(tspInstance.nodes)
    rand_index = list(np.random.choice(num_nodes, size=num_nodes, replace=False))
    rand_index.append(rand_index[0])

    sum = 0
    for a, b in pairwise(rand_index):
        sum = sum + tspInstance.getDistance(a, b)

    print(sum)

if __name__ == "__main__":
    main(sys.argv[1:])
