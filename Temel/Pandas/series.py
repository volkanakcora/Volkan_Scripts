# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

data = np.array(["Engin" , "Derin" , "Salih"])
s = pd.Series(data) #data, index = [1,2,3] sıralamayı belirleyebilrisin
print(s)


data2 = {"matematik":10 , "fizik":20 , "beden" : 100}
s2 = pd.Series(data2 , index = ["fizik" , "matematik" ,"beden"])
print(s2)

print(s2[0])  # sonucu 20 verir bunun sebebi indexteyi sırayı takip etmesi

s3 = pd.Series(5,index = [1,2,3,4])
print(s3)