# -*- coding: utf-8 -*-

ogrenciler = ["engin","volkan","kamil"]

print(ogrenciler)

ogrenciler.append("selim")
ogrenciler[0] = "veli"
print(ogrenciler[3])

ogrenciler.remove("veli")

print(ogrenciler)

# list constructer

sehirler = list(("ankara","istanbul" , "ankara"))

print(sehirler)

#diger fonksiyonlar
#print(sehirler.clear())
print("ankara sayisi = " + str(sehirler.count("ankara")))
print("ankara indexi = " + str(sehirler.index("ankara")))
sehirler.pop(1)     # bir birimi çıkarma     insert = ekleme
sehirler.insert(0,"istanbul")
sehirler.reverse()
print(sehirler)

sehirler3 = sehirler.copy()

sehirler2 = sehirler

sehirler2[0] = "izmir"

print(sehirler) 
print(sehirler2)
print(sehirler3)

sehirler.extend(sehirler3)
sehirler.sort()  # sıralamya yarar
print(sehirler)

