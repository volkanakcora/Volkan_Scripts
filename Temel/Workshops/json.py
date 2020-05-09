# -*- coding: utf-8 -*-


import json

data = '{"FirstName" : "Volkan" , "LastName" : "akcora"}'


y = json.loads(data)

print(y["FirstName"     ])
print(y["LastName"     ])


customer = {
        
        "firstname" : "engin",
        "e mail": "volkan.akcora@gmail.com"}

customerJson = json.dumps(customer) #pyhton nesnelerini cevirmek icin kullanılır

print(customer)