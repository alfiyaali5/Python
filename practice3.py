# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def error(n,d):
    try:
        result=n/d
        print(result)
    except ZeroDivisionError:
        print("zero is not allowed  in this program")
error(70,0)
# # Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
def data():
    try:
        user_data =int(input("enter the integer value :"))
    except ValueError:
        print("The input was not a valid integer.")
data()
#Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
def data2(fname):
    try:
        file=open(fname,'r')
        a=file.read()
        print("file exist")
        print(a)
        file.close()
    except FileNotFoundError:
        print("file not exist")

fname=input("input the file")
data2(fname)

#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    x = int(input("enter the value of x : "))
    y = input("enter the value of y : ")
    result=x+y
    print(x+y)
except TypeError:
         print("the value you enter is type error")
# Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
