#!/usr/bin/python

#############################################################
# Des:      Plot scattered figure
# Author:   Dong Haixia
# Version:  v1.0.0
# Date:     28/5/2020
#############################################################

import numpy as np
from matplotlib import pyplot as plt

y = np.linspace(1, 10, 20)
plt.scatter(y, np.cos(y), s=50, c='green')


t = np.random.randn(100)
v = np.random.randn(100)
colors = np.random.rand(100)
size = 1000 * np.random.rand(100)
plt.scatter(t, v, c=colors, s=size, alpha=0.5)
plt.colorbar()