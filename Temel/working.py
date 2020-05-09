# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:16:24 2019

@author: volka
"""

my_income = 100

tax_rate = 0.1

my_taxes = my_income * tax_rate



my_string= "hello world"

print(my_string[8])
print(my_taxes)
print(my_string[2:])
print(my_string[2:6])
print(my_string[::2]) # zıplar 2 şer 2 şet

# str does not support item assignment

name = "Sam"

last_name = name[1:]
print(last_name)
print(name.upper())

print(name.split())

#Formatting with the  .format() method

print("this is a string{} ".format(" INSERTED"))

print("the {2} {0} {0} ".format("Fox","brown",'quick'))

result = 5

print("the result {r}".format(r = result))

my_list = ["one","two","three"]
another_list = ["five","six","seven"]
print(my_list+another_list)

newlist = my_list+another_list # liste birleştirme
print(newlist)

newlist[0]="all one caps" # listeye eleman ekleme , bu .append ile de yapılabilir
print(newlist)

newlist.append("six")
print(newlist)

newlist.pop() # it deletes the last item
print(newlist)

