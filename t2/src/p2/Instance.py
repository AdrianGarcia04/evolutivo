import sys
import numpy as np

class Instance:
    def __init__(self):
        self.name = ""
        self.dim = 0
        self.nodes = np.array([])
        self.distances = np.zeros((self.dim, self.dim), dtype="float64")

    def set_dim(self, dim):
        self.dim = dim
        self.nodes = np.array([None] * dim)
        self.distances = np.zeros((self.dim, self.dim), dtype="float64")

    def add_node(self, id, x, y):
        self.nodes[id - 1] = (x, y)

    def get_node(self, id):
        return self.nodes[id - 1]

    def get_distance(self, id1, id2):
        return self.distances[id1 - 1][id2 - 1]

    def calc_distances(self):
        nodes = self.nodes
        for i in range(self.dim):
            self.distances[i][i] = 0
            for j in range(i):
                dif_x = nodes[i][0] - nodes[j][0]
                dif_y = nodes[i][1] - nodes[j][1]
                distance = np.sqrt(dif_x**2 + dif_y**2)
                self.distances[i][j] = distance
                self.distances[j][i] = distance

    def read_file(file, verbose=False):
        tsp = Instance()
        type_weight = ''
        node_coord = False
        node_weight = False
        with open(file, "r") as data:
            line_num = 0
            line_weight = 0
            for line in data:
                if verbose: print(line, end='')
                line_num += 1
                try:
                    if line.startswith('EOF'): continue
                    if line.startswith('COMMENT'): continue
                    if node_coord:
                        line = line.strip()
                        line = line.replace("   ", " ")
                        line = line.replace("  ", " ")
                        coords = line.split(' ')
                        id = int(coords[0].strip())
                        tsp.add_node(id, float(coords[1].strip()), float(coords[2].strip()))
                    elif node_weight:
                        line = line.strip()
                        line = line.replace("   ", " ")
                        line = line.replace("  ", " ")
                        weights = line.split(' ')
                        for i in range(len(weights)):
                            w = float(weights[i].strip())
                            tsp.distances[line_weight, i] = weights[i]
                        line_weight += 1
                    elif line.startswith('NAME'):
                        tsp.name = line.split(':')[1].strip()
                    elif line.startswith('TYPE'):
                        typeInst = line.split(':')[1].strip()
                        assert typeInst == 'TSP', 'El tipo de instancia debe ser TSP'
                    elif line.startswith('DIMENSION'):
                        tsp.set_dim ( int(line.split(':')[1].strip()) )
                    elif line.startswith('EDGE_WEIGHT_TYPE'):
                        type_weight = line.split(':')[1].strip()
                    elif line.startswith('NODE_COORD_SECTION'):
                        assert tsp.dim > 0, 'Se debe indicar una dimensión mayor a cero'
                        node_coord = True
                        continue
                    elif line.startswith('EDGE_WEIGHT_SECTION'):
                        node_weight = True
                        continue
                except:
                    print("Ocurrió un error al procesar el archivo")
                    print("linea " + str(line_num) + ":")
                    print(line)
                    print("Verifique que el archivo tenga el formato correcto.")
                    print("Unexpected errors:")
                    print(sys.exc_info())
                    return tsp
        assert tsp.dim > 0, 'No se pudo leer los datos de la instancia TSP'
        if node_coord:
            tsp.calc_distances()
        return tsp

    def __str__(self):
        return "Name: {}, Dim: {}".format(self.name, self.dim)
