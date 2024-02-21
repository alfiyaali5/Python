string=input("enter the string : ")
if string == string[::-1]:
    print(" It is palindrome ")
else:
    print("it isn't palindrome")

# ************************************

num = int (input("enter the no "))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(num,"it is not prime no !")
        else:
            print(num,"it is prime no !")
        break
    else:
        print(num,"it is not prime no ")

# *************************************************

num=7
factorial=1
if num<0:
    print("sorry we aint give the factorial of negetive number")
elif( num == 0):
    print("factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        fact= factorial*i
    print(fact)

#***************************************************

num=(100,567,677)
print(max(num))

#****************************************************

num=int(input("enter the num you want to factorise"))
factorial=1
if num<0:
    print("sry we aren't give the factorial of the negetive no")
elif num ==1:
    print("the factrial of o is 1")
else:
    for i in range(1,num +1):
        factorial=factorial *i
        print(num,factorial)

#***********************************

num=int(input("enter the num "))
if num > 1:
  for i in range(2,num):
      print("not prime-no")
      if num % i == 1:
            print("prime-no")
      break


