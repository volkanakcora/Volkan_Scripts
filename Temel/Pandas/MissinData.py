# -*- coding: utf-8 -*-

import pandas as pd

url = "http://bit.ly/uforeports"

data = pd.read_csv(url)

print(data[["City","Colors Reported",
            "Shape Reported",
            "State",
            "Time"]].head())
print(data.isnull().head())  # bu fonksiyon nan olarak verilen değerleri gösterir.
print(data.isnull().sum())

#print(data[data.City.isnull()]) city dekileri siler

print(data.shape)
#data = data.dropna(how ="all")  # all veya any kullanabiliriz
#data = data.dropna(subset = ["City","Colors Reported"], how = "all")  # all yaparsan 
# iki veri de yok ise uçurur.   any  yaparsan iksinden birinde none varsa sil.
print(data.shape)


data["Shape Reported"].fillna(value="Belirsiz" , inplace = True)
print(data["Shape Reported"].value_counts(dropna=False))