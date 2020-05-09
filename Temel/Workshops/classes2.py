# -*- coding: utf-8 -*-

class person:
    def __init__(self,firstName,LastName,Age):
        self.firstName = firstName
        self.LastName = LastName 
        self.Age = Age
        
person1 = person("volkan", "akcora" , 22)
print(person1.Age)


class worker (person):
    def __init__(self ,salary):
        self.salary = salary
        
        
class customer(person) :
      def __init__(self , creditcardnumber):
          self.creditcardnumber = creditcardnumber
          
          
class marriage (person) :
      def __init__(self , status):
        self.status = status

volkan = marriage()
          
          
ahmet = worker()

mehmet = customer()



          