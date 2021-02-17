#!/usr/bin/python

#############################################################
# Des:      Visualize Date
# Author:   Dong Haixia
# Version:  v1.0.0
# Date:     26/5/2020
#############################################################

import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np 
import random 

# Generate a random series
mat = np.random.random((100, 100)) * 255
mat = np.array(mat, dtype=np.uint8)

plt.figure(figsize=(10, 10))

plt.subplot(1, 2, 1)
plt.axis('off')
plt.imshow(mat)

plt.subplot(1, 2, 2)
sns.lineplot([x for x in range(100)], [random.random()*x for x in range(100)])
plt.show()