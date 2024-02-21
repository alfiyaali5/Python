class Std:
     def __init__(self,name,rollno):  #THIS IS AN INSTANCE var
         self.name=name
         self.rollno=rollno

     def mth(self):   #instance methon bcoz self.
         print(f"my name is {self.name}")
         print(f"my roll no is {self.rollno}")

     def name_len(self):
         print(len(self.name))



s1=Std("shrishti",11)
s1.mth()
s1.name_len()

#cls method
class Student:
    category="python"
    category2=".net"

    @classmethod
    def info(cls):
        print(f"my class method is {cls.category}")

    @classmethod
    def info2(cls):
        print(f"my class method is {cls.category2}")

Student.info()
Student.info2()

#static method
class Std:

    @staticmethod
    def add(a,b):
        print(a+b)

Std.add(10,20)

#constructor inheritance
class Parent:
    def __init__(self):
        self.bal=500000

    def display_bal(self):
        print(f"this is parent blc {self.bal}")

class Child(Parent):
    pass

mike=Child()                    #this is using parent constructor  that is called constructor inheritance
mike.display_bal()