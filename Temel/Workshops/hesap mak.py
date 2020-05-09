# -*- coding: utf-8 -*-
import matematikModul as mm


print("toplam  : + ")
print("Cıkarma : - ")
print("Bölme   : / ")
print("carpma  : * ")

sayi1 = int(input("sayi 1 giriniz"))
 
sayi2 = int(input("sayi 2 giriniz"))

islem = input("islemi giriniz")


if islem == "+":
    print("toplam = " + str(mm.topla(sayi1,sayi2)))
    
if islem == " -":
    print("Cıkarma=" + str(mm.cıkar(sayi1,sayi2)))
    
if islem == "/" :
    print("Bölme= " +  str(mm.bol(sayi1,sayi2)))
    
if islem == " * ":
    print("carpma = " +  str(mm.carp(sayi1,sayi2)))
    
    
    


 
 