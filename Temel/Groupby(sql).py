# -*- coding: utf-8 -*-


import sqlite3

connection = sqlite3.connect("chinook.db")


cursor = connection.execute("""select city,count(*) from
                           customers group by city having count(*) > 1 order by city desc """) ###order by = sırala , asc , desc sıralama birimleri^###
 

for row in cursor:
    print("city = " + row[0])
    print("count= " + str(row[1])) 
    print("\n")
    print("**********")

connection.close()