# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:36:55 2019

@author: volka
"""

import numpy as np
np.random.seed(12345)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4, suppress=True)



fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)


cumsum = np.random.randn(50)
cumsum
cumsum= cumsum.cumsum()
cumsum
plt.plot(cumsum, 'k--')
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
# As you can notice `np.random.radn()` returns a sample (or samples) from the “standard normal” distribution
ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
plt.show()