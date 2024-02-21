class Test:
    def add(self,a,b):
        return(a+b)
    def add(self,a,b,c):
        return(a+b+c)
    def add(self,a,b,c,d):
        return(a+b+c+d)
t1=Test()
t1.add(2,3)       #jab hum ek hi class me same method lete h to wo achieve nhi krta method overloading it will give error
t1.add(2,3,4)         #python doesnt suport method overloading directly
t1.add(2,4,5,6)

# with default parameter
class Test:
    def add(self,a,b,c=0):
        return(a+b+c)

t1=Test()
print(t1.add(2,3))

# with * args

class Test:
    def add(self,*args):
        total=0
        for i in args:
         total=total+i
        return total
t1=Test()
print(t1.add(2,3))
print(t1.add(2,3,4))