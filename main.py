from FDM.source.matrices import *
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def logSomething(x, a, b, c):
    return a + b* np.log(x +c)


Nx = 500
halfPoint = int(Nx/2)
inputVoltages = np.zeros((Nx, Nx))
inputVoltages[halfPoint, 10:90] = 1
inputVoltages[halfPoint+10, 10:90] = -1
solutionVoltages = Solve(inputVoltages)
print(solutionVoltages[halfPoint])
fig, ax = plt.subplots(1, 1)
im = ax.imshow(solutionVoltages)
fig.colorbar(im)
#xData = np.arange(1, halfPoint+1, 1)
#yData = 1 - 0.2556*np.log(xData)
#yData2 = 1/(xData+1)
#ax.plot(xData, solutionVoltages[halfPoint][halfPoint:])
#ax.plot(xData, yData)

#pars, cov = curve_fit(f=logSomething, xdata=xData, ydata=solutionVoltages[halfPoint][halfPoint:], p0=[1, 2, 1], bounds=(-np.inf, np.inf))
#print(f'pars: {pars}\ncov:{cov}')

plt.show()
