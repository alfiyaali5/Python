class Parent:
    def __init__(self):
        self.bal=500000

    def display_bal(self):
        print(f"this is parent blc {self.bal}")

class Child(Parent):
    pass

mike=Child()                    #this is using parent constructor  that is called constructor inheritance
mike.display_bal()