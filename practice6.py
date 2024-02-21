# #prime no
# num=int(input("Enter the num : "))
# if num >1:
#     for i in range(2,num//2):
#         if num % i == 0:
#             print(num,"it is not prime no")
#             break
#     else:
#         print(num,"it is prime no ")
# else:
#     print("it is not prime no")
#
# #fibonacci series
#
# n = int(input ("Enter the number you want to print: "))
#
# a = 0
# b = 1
# for i in range(0,n):
#     print(a, end = " ")             # a:0;    a:1;       a:2
#     c = a+b                     #c=0+1=1; c= 1+1=2;  c=1+2=3
#     a = b               #a=1    ; a=1;       a=2
#     b = c               #b=1    ; b=2;       b=3
#
#
# #same
#
# num=int(input("enter the num : "))
# n1=0
# n2=1
# for i in range(0,num):
#     print(n1,end=" ")
#     c = n1+n2
#     n1 = n2
#     n2 = c

# #right angle pattern
#
# row=int(input("enter the no of row"))
# for i in range(row):
#     for j in range(i):
#         print('*',end=" ")
#     print("")
#
# #downward
# row = int(input("enter the num of row"))
# for i in range(row):
#     for j in range(i,row):
#         print('*',end=" ")
#     print("")
#
# #no rightangle pattern
# row=int(input("enter the no of row"))
# for i in range(row):
#     for j in range(i):
#         print(j+1,end=" ")
#     print("")
#
#
# #downwward no
# row = int(input("enter the num of row"))
# for i in range(row):
#     for j in range(i,row):
#         print(j+1,end=" ")
#     print("")

# #alphabate
# row=int(input("enter the no"))
# ascii_value=65
# for i in range(row):
#     for j in range(i+1):
#         alphabate = chr(ascii_value)
#         print(alphabate,end=" ")
#     ascii_value +=1
#     print("")

