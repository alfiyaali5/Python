#oops concept
class Product():   #class define
    quantity=5  #optional-this is the class attribute and class atribute is remain same for every object

    def __init__(self,name,price):  #constructor
        self.name=name
        self.price=price



p1=Product('laptop',40000)   #object bna rhe h
print(p1.name)    #print(variable.name)
print(p1.price)
print(p1.quantity)