class Product:

    def __init__(self,name,price,color):    #constructor
        self.name=name
        self.price=price
        self.color=color


    def summer_dis(self):                      #method
        self.price=self.price-self.price*5/100   #self.anything=anything

    def winter_dis(self):
        self.price=self.price-self.price*20/100

p1=Product("phone",30000,"blue")
print(p1.price)
p1.summer_dis()
print(p1.price)
p1.winter_dis()    #variable.method(this is call)
print(p1.price)