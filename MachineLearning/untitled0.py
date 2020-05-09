# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:19:05 2019

@author: volka
"""
import numpy as np
mylist = [ i*i for i in range(10)]
print(mylist)

print(np.arange(2,3,0.1))


import re
m = re.split('(?<=abc)def', 'abcdef',"bra\t")