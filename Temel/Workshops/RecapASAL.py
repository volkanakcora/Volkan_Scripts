# -*- coding: utf-8 -*

sayi = int(input("lütfen bir sayi giriniz"))
AsalMi = "evet"
for x in range(2,sayi):
    if (sayi % x) == 0:
        AsalMi = "hayir"
        break

if AsalMi =="evet":
    print("bu sayi asaldir")
    
else :
 print("asal değildir")    