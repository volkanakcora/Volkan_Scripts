# -*- coding: utf-8 -*-

sehirler = ["Ankara" , "İstanbul" , "izmir" , "Adana"]

for sehir in sehirler:
    if sehir != "Ankara":    # ünlem gelirse unless olur
        
        # you could put here "break" which will cause stop the loop till find the mentioned answer.
        # you could put continue and which will cause passing the  specified command. like " istanbul"
        print( sehir + " için kod = " +   sehir[0:3])
        
        print("++++")    
#        For range
for x in range(100):
  print(x)        
  
  
for y in range(1,100,3):
    print(y)