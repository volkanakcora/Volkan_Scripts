# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:32:26 2019

@author: volka
"""

myfile = open("myfile.txt")
myfile.read()
print(myfile.seek(0))
contents = myfile.read()
print(contents)

print(myfile.readlines())

myfile.close()


with open("myfile.txt", mode = "r") as file_me:
    contents = file_me
    
with open("myfile.txt", mode = "a") as f:
    f.write("four on four")
    
    
    
with open ("adfadkajs.txt", mode ="w") as f:
    f.write(" I created this file") 
    
with open ("adfadkajs.txt",mode = "r") as f:
    print(f.read())