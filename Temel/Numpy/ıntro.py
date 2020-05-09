# -*- coding: utf-8 -*-

import numpy as np

#havaDurumu = [[12,21,31],[6,17,18],[11,12,13]]
#print(havaDurumu)

a = np.arange(15).reshape(3,5)   # arrange fonksiyon baslangın dahil sonuncu dahil olmayan sayı verir
print(a)
print(type(a))
print("dimension =" + str(a.ndim))


b = np.arange(10)
print(b)
print(b.shape)
print("dimension =" + str(b.ndim))