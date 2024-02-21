# #function
num=[1,2,3,4,5]
def square(x):   #without using map func
    return x*x
for i in num:
     print(square(i))

#map
num=[1,2,3,4,5]
def square(x):  # using map funtion
    return x*x
new_list=list(map(square,num))
print(new_list)
#use map function to convert string aas a list integer or float

num=['1','2','3','4','5']
list1=list(map(float,num))#int ,float both takes
print(list1)


#Filter
num=[1,2,3,4,5,6,7,8,9,10]
odd_num=[]        # this is nornaml example using loop
for i in num:
    if i%2 == 1:
        odd_num.append(i)
        print(odd_num)
# example using filter
num=[1,2,3,4,5,6,7,8,9,10]
def odd(x):
    if x%2 == 1:
        return(x)
new1=list(filter(odd,num))
print(new1)
# even ex
def even(x):
    if x%2 != 1:
        return(x)
new1=list(filter(even,num))
print(new1)

#Generaters in python
def fun():
    count=0
    while count <= 10:
        yield count
        count=count+1
a=list(fun())
print(a)
#ex2 even odd
def even(x):
    for i in range(x):
       if i%2 == 0:
           yield i
b=list(even(11))
print(b)
def odd(x):
    for i in range(x):
       if i%2 != 0:
           yield i
b1=list(odd(12))
print(b1)