# #Write a Python program to read an entire text file.
def func():
    file=open('C://Users//user//OneDrive//Desktop//python2.txt')
    a=file.read()
    print(a)
    a.close()
func()
#Write a Python program to read first n lines of a file.
def func2():
  file=open('C://Users//user//OneDrive//Desktop//python2.txt')
  x=file.readline()
  print(x)
  file.close()
func2()
#Write a Python program to append text to a file and display the text.
file=open('name2.txt','a')
v1=input("\n enter whatever you want :")
c=file.write(v1)
print(c)
#Write a Python program to read last n lines of a file.
def func3():
 file=open('name2.txt','r')
 c1= file.readlines()[-1]    #it works for all -1,-2,-3
 print(c1)
 file.close()
func3()
#2nd example of append
file=open('name.txt','a')
name=input("enter whatever")
file.write(name+'\n')
with open('name.txt','r')as file:
 c=file.realines()
for x in c:
  print(c)

file=open('name2.txt','r')
c_list=file.readlines()
for x in c_list:
 print(x)
try :
    name=input("enter the name:")
    rollno=int(input("enter the rollno"))
    email=input("enter the email")
    student_list=[name,rollno,email]
    print(student_list)
except AttributeError:
    print("Error: check the atributes in the code!")
try:
    encoding=input("input the incode in the file(0,1233,567)")
    file=open(fname,'r')
    a=file.read()
    print(a)
except UnicodeError:
#     print("Error:check the code!")
try:
   dividend=float(input ("enter the value of dividend:"))
   divisor=int(input("enter the value of divisor:"))
   result=dividend/divisor
   print(result)
except ArithmeticError:
        print("check the operation u put in the code")

with open('name.txt', 'a')as file:
    v = ("my name is mahi live at nagpur")
    file.write(v)

