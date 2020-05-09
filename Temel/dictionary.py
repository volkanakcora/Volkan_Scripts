# -*- coding: utf-8 -*-

sozluk = {
        "book" : "kitap" ,
        "table" : "masa"
        
        }

sozluk2 = dict( kitap = "book" , masa = "table")
sozluk["book"] = "kitap1"  # to be able to change the name or value of dict.
sozluk["pencil"] = "kalem"
del(sozluk["book"])
print(sozluk)
