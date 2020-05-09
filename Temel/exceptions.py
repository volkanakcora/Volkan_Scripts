# -*- coding: utf-8 -*-

try :
    sayi = int(input("bir sayi giriniz"))

except ValueError:
    print("bir hata oluştu sayi giriniz")
    
except ZeroDivisionError:
    print("payda sıfır olamaz")

except :
    print("bir hata var")

print("bitti")    