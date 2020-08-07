from FDM.source.matrices import *
from matplotlib import pyplot as plt

Nx = 500
halfPoint = int(Nx/2)
inputVoltages = np.zeros((Nx, Nx))
inputVoltages[halfPoint, halfPoint] = 1
solutionVoltages = Solve(inputVoltages)
print(solutionVoltages)
plt.imshow(solutionVoltages)
plt.colorbar()
plt.show()
