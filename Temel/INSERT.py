# -*- coding: utf-8 -*-

import sqlite3

def selectop():
    connection = sqlite3.connect("chinook.db")
    
    cursor = connection.execute(""" select FirstName,LastName
                                from customers
                                where FirstName like '%ja' """)
    
    for row in cursor:
        print("FirstName = " + row[0])
        print("LastName = "+ row[1])
        print("*****")
     
    connection.close()   
        

#selectop()       


def insertCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""insert into customers
                       (Firstname,LastName,city,email) 
                        values('volkan','akcora','ankara',
                        'volkan.akcora@gmail.com')""")
    connection.commit()
    connection.close()
    
    
#insertCustomer()    


def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers set city='İstanbul'
                       where city='ankara' """)
                       
                       
    connection.commit()
    connection.close()

#updateCustomer()   



def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute(""" delete from customers where CustomerId = 64 """)
    
    connection.commit()
    connection.close()
    
#deleteCustomer()    





def jointop():
    connection = sqlite3.connect("chinook.db")
    
    cursor = connection.execute(""" select albums.Title ,
                                artists.Name from artists
                                inner join albums
                                on Artists.ArtistId = albums.ArtistId """)
    
    for row in cursor:
        print("title = " + row[0] + "Name = "+ row[1] )
        
#        connection.close()
        
jointop()                    
       


               
     