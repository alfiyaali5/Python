#if else condition
age=int(input("enter your age: "))
if age>=18:
          print("you can vote")
else    :
        print("you can't vote")
#if elif else condition
marks=int(input("enter your mark:"))
if marks>=90:
            print("you are passed with grade A")
elif marks>=70:
            print("you are passed with grade B")
elif marks>=40:
            print("you are passed with grade c")
else :
            print("you are failed")
#Nested if
username=input("enter username:-")
password=input("enter password:-")
if username=='alfiya':
    if(password=="1234"):
        print("login successfully")
    else:
         print("invalid password")
else:
    print("invalid username")
#and
a=5
b=2
c=6
if a>b and b>c:
    print("its true if this is applicable")
else:
    print("check the condition")
#or
a=3
b=6
c=4
if a>b or b>c:
    print("it's true")


