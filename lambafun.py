result=(lambda x:x**3)(2)
print(result)

# positional arg
var=(lambda x,y:x+y)(2,3)
print(var)

#keyword arg
res=(lambda x,y:x+y)(x=3,y=4)
print(res)

#default arg
c=(lambda x,y=10:x+y)(2)
print(c)

#1.. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
#Sample Output:
#25
#48
var=(lambda a:a+15)(10)
print(var)
var=(lambda x,y:x*y)(6,8)
print(var)
#2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
#Sample Output:
#Double the number of 15 = 30
#Triple the number of 15 = 45
#Quadruple the number of 15 = 60
#Quintuple the number 15 = 75
res=(lambda x=15:x*2)(15)
print(res)
res=(lambda x=15:x*3)(15)
print(res)
res=(lambda x=15:x*4)(15)
print(res)
res=(lambda x=15:x*5)(15)
print(res)
