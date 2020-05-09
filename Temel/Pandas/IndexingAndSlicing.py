# -*- coding: utf-8 -*-

import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns = ["Soyisim","isim","SSN","Test1","Test2"
                  ,"Test3","Test4","Final","Sonuc"]
print(notlar)
print(notlar.loc[:,"Soyisim"])
print(notlar.loc[:5,"Soyisim"])   # pandas ta 5. yide alır kapsamına
print(notlar.loc[:5,"Soyisim":"Test4"])  # : aralığı verir
print(notlar.loc[:5,["Soyisim","isim","Final"]])  # " , " koyarsak sadece isteneni gösterir
print(notlar.loc[:5,:"Test2"])   # aralğa ":"  koyarsak , verilene kadar olanı gösterir
print(notlar.loc[::-1,"isim"])   # Tersten sıralamaya yarar

