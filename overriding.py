
print(len(['apple','samsung']))
print(len("hellowirld"))
#method overriding
class Food:
    def type(self):
        print("this is food class")
    def eat(self):
        print("eat healthier food")

class Fruit(Food):                        #child class ise b or parent class ko b call kr skta h override kr skta h
    def type(self):
        print("this is fruit class")

obj=Fruit()
print(obj.type())
print(obj.eat())






