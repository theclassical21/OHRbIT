from __main__ import *
def bell(i,x):
    ring_cycle = 1 if len(x) < 20 else round(len(x)/10)
    return not bool(i % ring_cycle)
    
def read_Accel(fname):
    full_read = pd.read_csv(fname,delimiter=',')
    return full_read

def create_grids(full_read):
    X = full_read.groupby('x')
    x = [ key for key in X.groups ]
    
    Y = full_read.groupby('y')
    y = [ key for key in Y.groups ]
    
    Z = full_read.groupby('z')
    z = [ key for key in Z.groups ]
    
    x_grid, y_grid, z_grid = np.meshgrid(x,y,z)
    
    ax = np.zeros(np.shape(x_grid))
    ay = np.zeros(np.shape(y_grid))
    az = np.zeros(np.shape(z_grid))
    
    I,J,K = range(len(x)), range(len(y)), range(len(z))
    for i in I:
        subx = X.get_group(x[i])
        if bell(i,x):
            print('ding')
        for j in J:
            groupy = subx.groupby('y')
            suby = groupy.get_group(y[j])
            for k in K:
                groupz = suby.groupby('z')
                subz = np.array(groupz.get_group(z[k]))[0]
                ax[j][i][k] =  subz[3]
                ay[j][i][k] =  subz[4]
                az[j][i][k] =  subz[5]
    return x_grid,y_grid,z_grid,ax,ay,az
