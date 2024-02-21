def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end=" ")
          # to end the line after each row
        print("\r")
n=5
pattern(n)
#Static
def add():
    a=10
    b=20
    print(a+b)
add()
#dynamic
def add(a,b):
    print(a+b)
add(10,20)
add(287,300)
#Keyword Argument
def add(a,b):  # when we call the funtion that time we have to specify in key value order
    print(a+b)         #value specify krne k liye keyword argument use krte h(ORDER MATTER NHI KRTA HAI)
add(a=10,b=20)     #in key value pair
#default parameter
def add(a=10.4,b=2):
    print(a+b)
add(a=30,b=5)                    #ye override krta h value ko or agr direct call krege bina specify kiye to by default
def my_country(country="India"):          # value ka output deta hai
    print("my country is "+country)
my_country()
my_country("norway")
#arbitary argument
def sum(*numbers):
    result=0                #we have to put variable here to specify the variable
    for num in numbers:
        result=result+num
    print(result)               #Strike(*)-define
sum(37,4,2)           #jb hme nhi pta hota hai ki user kitni value passs krega to hum arbitary operater ka use krte hai
sum(23.3,47)          #Arbitary allows us to pass varying no of values during a function call
#Arbitary keyword argument
def my_function(**fruitsname):   # 2 star is liye hota hai jab humare pass key or value dono ho
    for x in fruitsname:
        print(f"color of fruit {x} is  "+ fruitsname[x])

my_function(banana="yellow" ,apple="red")
my_function(tangerine="orange", green="guava",pink="strawberry")
#use return value to other function
def add(a,b):
    total=a+b
    return total
def update(total):
    update_value=total+50
    return update_value
a1=add(10,20)
print(a1)
#
total=0
def add(a,b):
    total=a+b
    print(total)
add(100,200)
print(total)
#global variable
count=10
def count1():
    count=20
    print(count)
count1()
print(count)
#recursion
def hello():
    print("Hello")
  #  hello()
hello()
#Recursion
def factorial(number):     #this is recursive function
  #condition
    if number==1:
        return 1   #this is call
    else:
        return number*factorial(number-1)
a=factorial(8)
print(a)
# decoraters
def chocolate():           #1st function
    print("chocolate medoldy")
def decoraters(func1):     #2nd function
    def new_func():  # function k andr function
        print("wrapper upside")
        func1()
        print("wrapper downside")
    return new_func
choco=decoraters(chocolate)
choco()

def area(r=6,pi=3.14):
     return r*r*pi
x=area(6)
print(x)




