# -*- coding: utf-8 -*-
import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns = ["Soyisim","isim","SSN","Test1","Test2"
                  ,"Test3","Test4","Final","Sonuc"]
print(notlar)
print(type(notlar))
print(notlar.head())
print(notlar.tail())
print(notlar["Sonuc"])
print(notlar.iloc[2])
print(notlar[1:5])