# -*- coding: utf-8 -*-
import sys
liste = [7,'engin',0,3,15,20,7]

for x in liste :
    try:
        print('sayi :' + str(x))
        sonuc = 1/int(x)
        print("sonuc :" + str(sonuc))
    except ValueError :
        print(str(x)+ (" =  ") + ("bu bir sayi degil"))
    except ZeroDivisionError :
        print(str(x)+ (" = ")+ "sıfıra bölme hatası")
    except  :
        print(str(x) +(" ")  +"hesaplanamadi")    
        print("sistem diyor ki : " + str(sys.exc_info()[0]))
        
    finally : 
        