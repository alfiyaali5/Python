class Product: #parent class
    def __init__(self,name,price):
        self.name=name
        self.price=price


    def get_data(self):
        self.name=input("enter the product name :")
        self.price=input("enter the product price")

    def display_data(self):
        print(self.name)
        print(self.price)

class Digitalproduct(Product):    #child class me inherit kr rhe h parent class ko

    def __init__(self, link):
        self.link=link

    def get_link(self):
        self.name=input("enter the link :")

    def display_link(self):
        print(self.link)
p1=Digitalproduct("")
p1.get_data()
p1.display_data()
p1.get_link()
p1.display_link()


