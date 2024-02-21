class A:

    def method_a(self):
        print("method of class a")

class B:

    def method_b(self):
        print("method of class b ")

class Class(A,B):

    def method_c(self):
        print("method of class c")
a=Class()
a.method_a()
a.method_b()
a.method_c()


