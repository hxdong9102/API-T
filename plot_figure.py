#!/usr/bin/python

#############################################################
# Des:      Plot sin and cos figure and save the figure.
# Author:   Dong Haixia
# Version:  v1.0.0
# Date:     28/5/2020
#############################################################

import numpy as np
from matplotlib import pyplot as plt

# %matplotlib inline

x = np.linspace(0, 10, 100)

fig = plt.figure()
plt.plot(x, np.sin(x), "--", label='sinx')
plt.plot(x, np.cos(x), 'o', color='red', label='cosx')
plt.legend(loc=0)
fig.savefig(r"D:\Learning-File\pythonFile\Scripts\sin_cos.png")

# Put sin and cos in seperate picture
plt.subplot(1, 2, 1)
plt.plot(x, np.sin(x), "--")
plt.subplot(1, 2, 2)
plt.plot(x, np.cos(x))


# xlim, ylim are used to limit the value range
y = np.linspace(1, 10, 20)
plt.plot(y, np.sin(y), "-p", color="blue", markersize=15, linewidth=3, markeredgecolor='red', markeredgewidth=1)
plt.xlim(2, 8)
plt.ylim(-0.8, 0.8)
