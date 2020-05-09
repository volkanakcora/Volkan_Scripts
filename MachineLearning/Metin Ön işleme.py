# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 13:31:30 2019

@author: volka
"""

##OLUŞTURMA VE BİÇİMLENDİRME

isimler = ["ali","veli","volkan"]

for i in isimler:
    print("isimler : " , i , sep = "")
    
print(*enumerate(isimler,1))    # data'ya numaralandırma sağlar .

# Dizi içi tip sorgulamaları

print("mvk".isalpha())