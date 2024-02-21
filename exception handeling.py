#exception erro
n=int(input("enter the value of numerator :"))
d=int(input("enter the value of denominator :"))
result=0
try:
    result=n/d
    print(result)
except ZeroDivisionError:
    print("denominator should be less than numerator and not equal to zero")
#Else block
x=10
y=20
c=0
try :
    c=x+y+z
    print(c)
except NameError:
    print("z value is not defiend")

x=int(input("Enter the value of x :"))
y=int(input("Enter the value of y :"))
z=int(input("Enter the value of z :"))
try :
    c=x+y+z

except NameError:
    print("z is not defined ")
else:
    print(c)
#Finally block
x=10
y=20
z=1
c=0
try:
    c=x+y+z
except NameError:
    print("z is not defined")
else:
    print(c)
finally:
    print("this block execute no matter what")

