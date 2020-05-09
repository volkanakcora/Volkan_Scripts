# -*- coding: utf-8 -*-

studentsSet = {"Engin","Derin","Salih","Ahmet"}
print(studentsSet)

for student in studentsSet :
    print(student)
    
print("Derin" in studentsSet)

if "Derin" in studentsSet :
     print("listede var")
     
studentsSet.add("Ali")
print(studentsSet)

studentsSet.update(["volkan","Ceren"]) # çoklu eklemelerde kullanılır
print(studentsSet)


# eleman silmek için



studentsSet.remove("Salih") # bulamayınca hata vermez.
print(studentsSet)


x = studentsSet.pop() # herhangi bir elemenanı siler.