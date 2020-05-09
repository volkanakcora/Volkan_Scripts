# -*- coding: utf-8 -*-

import sqlite3

def selectoperasyonlari():
#connection = sqlite3.connect("chinook.db")

#cursor = connection.execute("""select FirstName,LastName from
#                            customers where LastName like '%ja' """) ###order by = sırala , asc , desc sıralama birimleri^###
##  bir adet % olur ise  adı a ile bitenler .
 for row in cursor:
    print("First Name = " + row[0])
    print("Last Name = " + row[1])
    print("\n")
    print("**********")

connection.close()


selectoperasyonlari()