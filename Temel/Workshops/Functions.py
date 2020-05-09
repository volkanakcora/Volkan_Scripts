# -*- coding: utf-8 -*-

def selamver(isim = "ziyaretçi"):
    print("merhaba = " , isim)
    
    
selamver ("Engin")
selamver ("volkan")
selamver ("arda")    
selamver()
    
def selamver2(isim = "ziyaretçi" , soyisim = "arkadaş"):
    print("merhaba = " , isim , soyisim)
    
    
selamver2("engin")    
selamver2()
#%%
def dikucgenalanihesaplama(a,b):
    return a*b/2

alan = dikucgenalanihesaplama(35,50)


print("hesaplanan alan = " , alan)
#%%
dikucgenalanihesaplama2 = lambda a,b : a*b/2

print(dikucgenalanihesaplama2(2,3))
#%%
