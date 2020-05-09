# -*- coding: utf-8 -*-

ogrenciler = [ "Engin" , "Fatma" ,"ayse" , "müge"      
        ]

fileToAppend = open("ogrenciler.txt" , "a")

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")
    
print(ogrenciler)