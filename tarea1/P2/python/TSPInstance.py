# -*- coding: utf-8 -*-
"""

"""

import sys
import numpy as np

class TSPInstance:
  def __init__(self):
    self.name = ''
    self.dim = 0
    self.nodes = np.array([])
    self.distancias = np.zeros((self.dim, self.dim), dtype='float64')
  
  def setDim(self, dim):
    self.dim = dim
    self.nodes = np.array([None]*dim)
    self.distancias = np.zeros((self.dim, self.dim), dtype='float64')
    
  def addNode(self, id, x, y):
    assert id > 0 and id <= self.dim, 'Id Incorrecto para la dimensión del problema'
    self.nodes[id-1] = (x,y)   
    
  def getNode(self, id):
    assert id > 0 and id <= self.dim, 'Id Incorrecto para la dimensión del problema'
    return self.nodes[id-1]

  def getDistance(self, id1, id2):
    return self.distancias[id1-1][id2-1]
  
  def calcularDistancias(self):
    nodos = self.nodes
    for i in range(self.dim):
      self.distancias[i][i] = 0
      for j in range(i):
        diffX = nodos[i][0] - nodos[j][0]
        diffY = nodos[i][1] - nodos[j][1]
        self.distancias[i][j] = np.sqrt(diffX*diffX + diffY*diffY)
        self.distancias[j][i] = self.distancias[i][j]
   
  def __str__(self):
    strObj= ""
    strObj += "Name: " + self.name + "\n"
    strObj += "Dim: " + str(self.dim) + "\n"
    return strObj  

  def readFile(fileName, verbose=False):
    tsp = TSPInstance()
    typeWeight = ''
    nodeCoord = False
    with open(fileName, "r") as data:
      lineNumber = 0
      for line in data:
        if verbose: print(line, end='')
        lineNumber += 1
        try:
          if line.startswith('EOF'): continue
          if line.startswith('COMMENT'): continue
          if nodeCoord:
            coords = line.split(' ')
            id = int(coords[0].strip())
            tsp.addNode(id, float(coords[1].strip()), float(coords[2].strip())) 
          elif line.startswith('NAME'): 
              tsp.name = line.split(':')[1].strip()
          elif line.startswith('TYPE'): 
            typeInst = line.split(':')[1].strip()
            assert typeInst == 'TSP', 'El tipo de instancia debe ser TSP'
          elif line.startswith('DIMENSION'): 
            tsp.setDim ( int(line.split(':')[1].strip()) )  
          elif line.startswith('EDGE_WEIGHT_TYPE'): 
            typeWeight = line.split(':')[1].strip() 
          elif line.startswith('NODE_COORD_SECTION'): 
            assert tsp.dim > 0, 'Se debe indicar una dimensión mayor a cero'
            nodeCoord = True
            continue
        except:
          print("Ocurrió un error al procesar el archivo")
          print("linea " + str(lineNumber) + ":")
          print(line)
          print("Verifique que el archivo tenga el formato correcto.") 
          print("Unexpected errors:")
          print(sys.exc_info())
          return tsp
    assert tsp.dim > 0, 'No se pudo leer los datos de la instancia TSP'
    tsp.calcularDistancias()
    return tsp
