# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 23:35:52 2019

@author: volka
"""

loc = "cut"

if loc == "Auto Shop":
    print("Cars are cool")
elif loc == "bank":
    print("money is cool")
else:
    print("I do not know much")
    
    
my_iterable = [1,2,3]

for item_name in my_iterable:
    print(item_name)

mylist = [1,2,3,4,5,6,7,8,9,10,11,23,45]

for i in mylist:
    print("hello")    
    
for i in mylist:
    if i%2 == 0:
        print(i)
        
sum_list = 0

for i in mylist:
    sum_list = sum_list + i

print(sum_list )


tup = ("volkan","selam","nasılsın")

for i in tup:
     
    print(i) 
