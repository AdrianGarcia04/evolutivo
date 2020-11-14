import numpy as np
import sys
import math
import arguments
import matplotlib.pyplot as plt
from DataExtract import DataExtract

if __name__ == '__main__':
    fields = {
        "instance": "str",
        "best": "float",
        "init_temp": "float",
        "final_temp": "float",
        "ex_time": "float",
        "iters": "int",
    }

    instances = ["ch130", "xqf131", "xqg237", "a280", "pbl395"]
    lower_bounds = {
        "ch130": 6110,
        "xqf131": 564,
        "xqg237": 1019,
        "a280": 2579,
        "pbl395": 1281,
    }
    data_extract = DataExtract(fields)

    for instance in instances:
        print(f"Instance: {instance}")
        data_extract.read("../ejecuciones/" + instance + "/results.txt")
        best_by_tmp = data_extract.segment("best", "init_temp")

        keys = list(best_by_tmp.keys())
        keys.sort()

        values = []
        lb = lower_bounds[instance]
        for k in keys:
            rel_errors = [(bst - lb) / lb for bst in best_by_tmp[k]]
            print(f"\tPromedio error relativo para T = {k}: {np.average(rel_errors)}")
