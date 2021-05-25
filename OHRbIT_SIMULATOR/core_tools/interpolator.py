from __main__ import *
## Interpolates values of a field between defined lattice by various methods


###############################################################################


#### Interpolates field via average of nearest points weighted by proximity,
#####   edge cases treated with periodic boundaries.
##### Input: list and array
#####           List contains the position indicies and fractional distance
#####         [  np.array([j,i,k ]) , np.array([fx,fy,fz]) ]
#####
#####           Array contains the field as a three dimensional numpy array

def linearInterpolation(grid_position,field):
    indicies, f_vector = grid_position
    dimensions = np.shape(field)
    next_indicies = [ (indicies[i] + 1) % dimensions[i] for i in [0,1,2] ]
    return 0.5*( field[indicies] + np.dot(f_vector,field[next_indicies]) )
###############################################################################
