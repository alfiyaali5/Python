class Parent:

    def __init__(self):
       self.blc=500000

    def display_blc(self):
        print(f"the blc of parent {self.blc}")

class Child:
    def __init__(self):
        self.msg="hello team"

    def hello(self):
        print("hello msg")
p1=Parent()
p1.display_blc()
c1=Child()
c1.hello()



