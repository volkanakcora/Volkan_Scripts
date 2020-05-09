    # -*- coding: utf-8 -*-
sayilar = [1,2,3,4,5]

sayilarkarel = list(map(lambda sayi : sayi*sayi,sayilar)) # map yöntemi

#for sayi in sayilar:
#    sayilarkarel.append(sayi*sayi)   normal yöntem
    

sayilarfiltreli = list(filter(lambda sayi : sayi > 2 , sayilar))
print(sayilarkarel) 
print(sayilarfiltreli)   

from functools import reduce

sayilarFaktoriyel = reduce(lambda x,y : x*y ,sayilar)
print(sayilarFaktoriyel)
