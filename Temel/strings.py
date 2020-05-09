# -*- coding: utf-8 -*-
#substring
mesaj = "MERHABA DUNYA"
print(mesaj[2:5])
yenimesaj = mesaj[2:5]
print(yenimesaj)

#len
print(len(mesaj))
yenimesaj2 = mesaj[len(mesaj)-1 : len(mesaj)]
print(yenimesaj2)

# lower upper

print(mesaj.upper())
#replace
print(mesaj.replace("ü","u"))

#mesaj = mesaj.replace("ü","u")
# split ve strip
bilgi = "Kolpa arda;Demiroğ;33;Ankara".strip()
print(bilgi.split())
print("Adı = " + bilgi.split(";")[0])

#input
ad = input("adınız?")

sayi1 = input("Sayı 1 = ? ")
sayi2 = input("sayı 2 = ? ")

print(int(sayi1) + int(sayi2))

