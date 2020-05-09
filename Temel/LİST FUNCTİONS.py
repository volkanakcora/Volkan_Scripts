# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 12:55:11 2019

@author: volka
"""

num_list = [1,4,5,6,2,3]
num_list.sort()
print(num_list)

d = {"k1":["a","b","c"],"k2": 123 , "k3" : [4,4,5]}
print(d)

print(d["k2"])

mylist = d["k1"]
letter = mylist[2]
letter.upper()
print(letter.upper())

#how to change something in dictionary

b = {
     "k1": "new value",
     "k2": "200",
     "k3": "300"}

b["k1"] = "new value2"

d.keys()
d.values()
d.items()