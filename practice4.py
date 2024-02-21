# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class Circle:
    PI=3.14

    def __init__(self,radius):
        self.radius = radius

    def circle_area(self):
        return (Circle.PI * self.radius * self.radius)

    def circle_perimeter(self):
         return ( 2 * Circle.PI * self.radius)

r= float (input("enter the radius of circle : ") )
c1=Circle(r)
area=c1.circle_area()
perimeter=c1.circle_perimeter()
print(f"area of circle-",area)
print(f"perimeter of circle-",perimeter)

# Write a Python program to create a calculator class Include methods for basic arithmetic operations.
class Calculator:
    def add(self, x,y):
        return(x+y)

    def sub(self, x,y):
        return(x-y)

    def multi(self, x,y):
        return(x*y)

    def divide(self, x,y):
        if y==0:
            print("it can't be divide by 0")
        else:
            return (x/y)
c1=Calculator()
r1=c1.add(12,6)
print("x+y =",r1)
r1=c1.sub(12,6)
print("x-y =",r1)
r1=c1.multi(12,6)
print("x*y =",r1)
r1=c1.divide(12,6)
print("x/y =",r1)

age=int(input("enter the age:"))
if age==18:
    print("you are eligible to vote!")
else:
    print("You are not eligible to vote , u r less than 18")


num=int(input("enter the num:"))
if num %2==0:
    print("then it is even!")
else:
    print("it is odd!")

username=input("enter your user name")
password=(input("enter your password"))
if username== 'admin' and password== 'secret':
 print("you log in succesfully")
else:
    print("your user and password is invalid")

income=int(input("enter your income"))
if income == 10000:
    print("0% tax")
elif income <= 50000:
    print("10% tax ")
elif income <=100000:
    print("20% tax ")
else:
    print("30% tax ")
que:7
weight=int(input("enter your weight"))
height=float(input("enter your height "))
BMI= weight/height*height
if BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("normal")
elif BMI <30:
    print("Overweight")
else:
    print("obese")
que:9
sum=0
for i in range (1,11):
    if i %2 ==0:
        sum += i
print("sum of even num",sum)
# que:10,11
num=5
while num >0:
    print(num)
    num -=1
print("off!")
# que:12
while True:
 password=(input("enter your password"))
 if password=='pass@123':
    print("logg inn!")
    break
else:
    print("incorrect password, try again")

# Que
string= input("enter the string")
if string ==[-1]:
    print("it is not palidrome")
else:
    print("palidrome")






