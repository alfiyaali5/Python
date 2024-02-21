class A:
    def method_a(self):
        print("method of class a")

class B(A):

    def method_b(self):
        print("method of class b")

class C(B,A):
    def method_c(self):
        print("method of class c")

c=C()
c.method_a()
c.method_b()
c.method_c()