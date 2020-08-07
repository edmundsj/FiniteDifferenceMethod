import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

def gridToColumn(pointGrid):
    return pointGrid.reshape(pointGrid.size, 1)

def columnToGrid(pointColumn):
    sideLength = int(np.sqrt(pointColumn.size))
    return pointColumn.reshape(sideLength, sideLength)

def Dxx(Nx):
    baseMatrix = lil_matrix((Nx*Nx, Nx*Nx))
    baseMatrix.setdiag(-2)
    baseMatrix.setdiag(1, k=1)
    baseMatrix.setdiag(1, k=-1)
    for i in range(Nx-1):
        baseMatrix[(i+1)*Nx -1, (i+1)*Nx] = 0
        baseMatrix[(i+1)*Nx, (i+1)*Nx -1] = 0
    return baseMatrix

def Dyy(Nx):
    baseMatrix = lil_matrix((Nx*Nx, Nx*Nx))
    baseMatrix.setdiag(-2)
    baseMatrix.setdiag(1, k=Nx)
    baseMatrix.setdiag(1, k=-Nx)

    return baseMatrix

def Laplacian(Nx):
    return Dxx(Nx) + Dyy(Nx)

def Solve(inputGridVoltages):
    Nx = inputGridVoltages.shape[0]
    inputColumnVoltages = gridToColumn(inputGridVoltages)
    D2 = Laplacian(Nx)
    nonzeroIndices = np.nonzero(inputColumnVoltages)[0]
    # Force the entire row to be zero except for the center position. This forces the value of that voltage
    # to be 1.
    for index in nonzeroIndices:
        D2[index] = 0 # force the entire row to be zero
        D2[index, index] = 1
    solvedVoltages = spsolve(D2, inputColumnVoltages)
    return columnToGrid(solvedVoltages)
