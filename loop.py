#range
#ex-list
numbers=list(range(11))
print(numbers)
num=list(range(15,31,2))
#It ---15 is starting no. 31 is end no. and 2 is step diff no.
print(num)
#for loo#ex-string
s1='python'
for value in s1:
    print(value)
for x in range(101):
    print(x)
    #ex table12
for y in range(12,132,12):
    print(y)
#ex-dictionary
people={'john':100,
        'time':200,
        'rohan':300
        }
for x in people:
    print(x) #this print only print the keys
    print(people[x]) #this print only print the value in dictionary

#while loop
count=1
while count<=10:
    count=count+1
    print(count)
#ex:of mobile recharge
bal=int(input("enter the days of recharge you did :"))
while bal>0:
    print(bal)
    bal=bal-1
else:
    print("please recharge")
#while break loop
recharge=30
while recharge>0:
    print(recharge)
    if recharge==20:
        break #-------continue 20 mt print kra loop me jake 21 se print kra that is continue loop
    recharge=recharge-1

#continue
recharge=30
while recharge>0:
      recharge = recharge - 1
      if recharge==20:
         continue
      print(recharge)
#continue
num=1
while num<=10:
    num=num+1
    if(num%2)==0:
        continue
    print(num)