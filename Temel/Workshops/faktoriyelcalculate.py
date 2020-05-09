# -*- coding: utf-8 -*-


sayi = int(input("sayi : "))

faktoriyel =  1 

if sayi < 0:
    print("negatif sayi olmaz")
    
elif sayi == 0:
    print("faktoriyel =  1 " )
    
    
else:
    for i in range(1,sayi+1):
        
        faktoriyel = faktoriyel * i 
        
    print("faktoriyel = ",faktoriyel)
  
    
0