# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:50:43 2019

@author: volka
"""

import pandas as pd 

data = pd.read_csv("spam.csv" , sep = ("\t")

data = data.split("\n")

v = pd.Series(data)
data = v[1:len(v)]
print(metin_vektoru)


DATA = pd.DataFrame(data , columns = ["messages"])
