# -*- coding: utf-8 -*-
data1 = {
            "id":[1,2,3,4],
            "ad":["engin","derin","salih","mehmet"],
            "soyad":["Demiroğ","Demiroğ","Demiroğ","Kaya"]} 
                        


data2 = {
            "id":[1,3,4,7],
            "ad":["ayşe","ali","ahmet","cemil"],
            "soyad":["Demiroğ","Demiroğ","Demiroğ","Kaya"]
            }

import pandas as pd

data1Df = pd.DataFrame(data1)
data2Df = pd.DataFrame(data2)

print(data1Df)
print(data2Df)

print(pd.merge(data1Df,data2Df, on="id",how="inner"))  # ortakları getirir
print(pd.merge(data1Df,data2Df, on="id",how="left")) # solda olup sağda olmayanlarıda getirir.
print(pd.merge(data1Df,data2Df, on="id",how="right")) # sağda olup solda olmayanlarıda getirir.

print(pd.concat([data1Df,data2Df]))  # axis = 1 eklersek yatay olarak verir.