## Central hub to load modules and define high level functions

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gvar as gv
import lsqfit as lsf
import os.path as pth
from OHRbIT_SIMULATOR import *

print(pth.abspath('.'))

def GENERATE_GRIDS():
    use_default_file = input(
        "Generate Grids from " + core_tools.acc_file + " ? [0/1]: "
        )

    if use_default_file:
        full_read = read_accelerations.read_Accel(core_tools.acc_file)
        xg,yg,zg,ax,ay,az = read_accelerations.create_grids(full_read)
    else:
        loop_lock = True
        while loop_lock:
            fname = input("Absolute Path to File: ")
            loop_lock = input("Files Selected: "+fname+"   Change? [0/1]: ")
        full_read = read_accelerations.read_Accel(fname)
        xg,yg,zg,ax,ay,az = read_accelerations.create_grids(full_read)
    return xg, yg, zg, ax, ay, az


default_gridpoint = [ np.array([1,1,1]), np.array([0.5,0.5,0.5]) ]
def interpolate_test(gridpoint= default_gridpoint):
    _, _, _, field, _, _ = GENERATE_GRIDS()
    return core_tools.interpolator.linearInterpolation(gridpoint,field)
