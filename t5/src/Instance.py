import sys
import numpy as np

class Instance:
    def __init__(self, name="", num_items=0, wmax=0, items=[], maxiters=0, pop_size=0):
        self.name = ""
        self.num_items = num_items
        self.wmax = wmax
        self.items = items
        self.maxiters = maxiters
        self.pop_size = pop_size

    def from_file(file, maxiters=0, pop_size=0):
        file = open(file, "r")
        (num_items, wmax) = file.readline().strip().split(' ')

        items = []
        for line in file:
            items.append(line.strip().split(' '))

        kwargs = {
            "name" : file,
            "num_items": num_items,
            "wmax": wmax,
            "items": items,
            "maxiters": maxiters,
            "pop_size": pop_size
        }
        
        return Instance(**kwargs)
