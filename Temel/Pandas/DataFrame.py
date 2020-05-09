# -*- coding: utf-8 -*-

import pandas as pd
data = [10,20,30,40,50]
df = pd.DataFrame(data)
print(df)

data2 = [["Engin",33,"Ankara"],["Derin",4,"Ankara"],["salih",32,"istanbul"]]
df2 = pd.DataFrame(data2, columns = ["isim","yaş","şehir"], index = [1,2,3])

print(df2)


data3 = {"isim":["Engin","derin","salih"],  # sözlük olarakda kullanılabilir
         "yaş":[33,4,32],
         "şehir":["ankara","ankara","istanbul"]}
df3 = pd.DataFrame(data3, columns = ["isim","yaş","şehir"], index = [1,2,3])

print(df3)
# del df3["şehir"]  herhangi birini silmek istediğinde bunu kullan

#df2.pop()  aynı işlem . nereyi silmek istersen.

#print(df3.loc[2])  sadece grmek istediğin data yı getirir

df4 = df3.append(df2)   # dataları birleştirir
print(df4)

print(df4.head())   # baştaki 5 liyi gösterir
print(df4.tail())  # sondaki 5 data yı verir