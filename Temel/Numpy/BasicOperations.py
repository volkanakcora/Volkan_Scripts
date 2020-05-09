# -*- coding: utf-8 -*-

import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4)

c = (a-b)
d = b**2
e = 10* np.sin(a)
print(e<7)
print(a*b)
print(a@b)   # matris çarpımlarını verir.


f = np.ones((2,4)) # birlerden oluşan matris
g = np.zeros((2,4))  # 0 olardan oluşan matris
h = np.random.random((2,4))
i = np.sum((2,4)) # toplam
j = np.min(b)  # en kucuk deger
l = np.sqrt(b)  # kare kökü