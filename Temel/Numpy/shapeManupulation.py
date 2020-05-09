# -*- coding: utf-8 -*-

import numpy as np


a = np.floor(10*np.random.random((3,4)))

print(a)
print(a.shape)
print(a.ravel())
print(a)    
a = a.ravel() # düzleştirir matrisi
print(a)
print(a.shape) # boyut bilgisi verir
print(a.reshape(2,6))
a = a.reshape(2,6)
print(a.T)