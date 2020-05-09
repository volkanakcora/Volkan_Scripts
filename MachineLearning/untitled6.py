# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:29:06 2019

@author: volka
"""
from numpy.random import randn
plt.plot(randn(30).cumsum(), 'ko--')
plt.show()


fig = plt.figure()
data = np.random.randn(30).cumsum()
# the last argument assigns a name to the series (see legend)
plt.plot(data, 'k--', label='Default')
plt.plot(data, 'k-', drawstyle='steps-post', label='steps-post')
plt.legend(loc='best')
plt.show()


plt.show()
np.random.seed(12348)

df = pd.DataFrame(np.random.rand(6, 4),
                  index=['one', 'two', 'three', 'four', 'five', 'six'],
                  columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df
df.plot.bar()