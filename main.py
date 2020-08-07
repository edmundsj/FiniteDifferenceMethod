from FDM.source.matrices import *
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def logSomething(x, a, b):
    return a + b* np.log(x)


Nx = 100
halfPoint = int(Nx/2)
inputVoltages = np.zeros((Nx, Nx))
inputVoltages[halfPoint, halfPoint] = 1
solutionVoltages = Solve(inputVoltages)
print(solutionVoltages[halfPoint])
fig, ax = plt.subplots(1, 1)
#im = ax[0].imshow(solutionVoltages)
xData = np.arange(1, halfPoint+1, 1)
yData = 1 - 0.2556*np.log(xData)
yData2 = 1/(xData+1)
ax.plot(xData, solutionVoltages[halfPoint][halfPoint:])
ax.plot(xData, yData)

pars, cov = curve_fit(f=logSomething, xdata=xData, ydata=solutionVoltages[halfPoint][halfPoint:], p0=[1, 2], bounds=(-np.inf, np.inf))
print(f'pars: {pars}\ncov:{cov}')

plt.show()
