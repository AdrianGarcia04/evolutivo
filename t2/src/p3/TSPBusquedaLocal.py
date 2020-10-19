import numpy as np

class TSPBusquedaLocal:
    def __init__(self, sol):
        self.sol = sol

    def vecindadCualquierCambio(self, sol):
        combinaciones = []
        for i in range(sol.dim):
            for j in range((i + 1), sol.dim):
                combinaciones.append((i, j))
        return combinaciones

    def vecindadAdjacentes(self, sol):
        combinaciones = []
        for i in range(sol.dim - 1):
            combinaciones.append((i, i + 1))
        combinaciones.append((0, sol.dim - 1))
        return combinaciones

    def explora_vecindad(self, primeraMejora=False, tipo=0):
        best_mov = (None, None)
        best_eval = float("inf")
        combinaciones = []

        if tipo == 0:
            combinaciones = TSPBusquedaLocal.vecindadAdjacentes(self, sol=self.sol)
        elif tipo == 1:
            combinaciones = TSPBusquedaLocal.vecindadCualquierCambio(self, sol=self.sol)

            #TODO
        for (x, y) in combinaciones:
            if self.sol.evaluar_swap(x, y) < best_eval:
                best_mov = (x, y)
                best_eval = self.sol.evaluar_swap(x, y)

        return (best_mov, best_eval)

    def aplicar_swap(self, x, y):
        return self.sol.evaluar_swap(x, y, aplicar=True)

    def busqueda_local(self):
        best_eval = self.sol.eval
        hayMejora = True
        i=0
        while hayMejora:
            i += 1
            print("- Sol Iter: " + str(i) + ", " + str(self.sol))
            hayMejora = False
            ((x, y), eval_mov) = self.explora_vecindad(tipo=1)
            if eval_mov < best_eval:
                best_eval = self.aplicar_swap(x, y)
                hayMejora = True

        return self.sol
