class Std:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print(f"the name is {self.name}")
        print(f"the rollno is {self.rollno}")

s1=Std('alfiya',12)   #outside the class that is public in nature:/public modifier
s1.display()

#protected
class Std:
    def __init__(self,name,rollno):
        self._name=name
        self._rollno=rollno

    def _display(self):
        print(f"The name is : {self._name}")
        print(f"The rollno is : {self._rollno}")

class Teachers(Std):

    def __init__(self,name,rollno,marks):
     super().__init__(name,rollno)
     self._marks=marks

    def display(self):
        self._display()
        print(f"The marks is : {self._marks}")

t=Teachers('payal',12,442)   #outside the class taht is protected in nature:/protected modifier
t.display()

#privtate
class Std:
    def __init__(self,name,rollno):
        self.__name=name
        self.__rollno=rollno

    def __display(self):
        print(f"The name is : {self.__name}")
        print(f"The rollno is : {self.__rollno}")

s1=Std('alfiya',12)
s1.__display()             #private method h object create  krne pr attribute error dega

class Teachers(Std):

    def __init__(self,name,rollno,marks):
     super().__init__(name,rollno)
     self._marks=marks

    def display(self):

        self.__display()
        print(f"The marks is : {self._marks}")

t=Teachers('payal',12,442)   #outside the class taht is protected in nature:/protected modifier
t.display()


























