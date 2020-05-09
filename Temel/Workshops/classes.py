# -*- coding: utf-8 -*-


class matematik :
    def topla(self ,sayi1,sayi2):
        return sayi1 + sayi2
    
    def cıkar(self ,sayi1,sayi2):
        return sayi1 - sayi2
    
    def carpim(self ,sayi1,sayi2):
        return sayi1 * sayi2
    
    def bol(self ,sayi1,sayi2):
        return sayi1/sayi2
    


sayi1 = int(input("lütfen sayi giriniz"))

sayi2 = int(input("ikinci sayi giriniz")) 

islem = input("yapmak istediğiniz islem")



if islem == "+" :
    (matematik.topla(sayi1,sayi2))
    
if islem == "-" :
    (matematik.cıkar(sayi1,sayi2))
    
if islem ==" /" :
    (matematik.bol(sayi1,sayi2))
    
if islem == "*" :
    (matematik.carpim(sayi1,sayi2))
    
      
matematik = matematik()  
print("sonuc =" + str(matematik()(sayi1+sayi2))  )