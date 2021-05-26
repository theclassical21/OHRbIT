## Central hub to load modules and define high level functions

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gvar as gv
import lsqfit as lsf
import os.path as pth
from OHRbIT_SIMULATOR import *

print(pth.abspath('.'))


## GENERATE_GRIDS:
### This script generates 6 Nx X Ny X Nz
def GENERATE_GRIDS:
    default_file = core_tools.pathDefinitions.acc_file
    use_default_file = input(
        "Generate Grids from " + default_file + " ? [0/1]: "
        )

    if use_default_file:
        comsol_data_frame = com_grid.read_Accel(default_file)
        xg,yg,zg,ax,ay,az = com_grid.create_grids(comsol_data_frame)
    else:
        loop_lock = True
        while loop_lock:
            fname = input("Absolute Path to File: ")
            loop_lock = input("Files Selected: "+fname+"   Change? [0/1]: ")
        full_read = com_grid.read_Accel(fname)
        xg,yg,zg,ax,ay,az = com_grid.create_grids(full_read)
    return xg, yg, zg, ax, ay, az


default_gridpoint = [ np.array([1,1,1]), np.array([0.5,0.5,0.5]) ]
def interpolate_test(gridpoint= default_gridpoint):
    _, _, _, field, _, _ = GENERATE_GRIDS()
    return core_tools.interpolator.linearInterpolation(gridpoint,field)
