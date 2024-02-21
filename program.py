#to write the name in file program
while True:
 with open('name.txt','a')as file:
    name=input("enter your name :")
    file.write(name+'\n')
    choice=input("do you want to enter name?(y/n)")
    if choice=='n':
        break

with open('name.txt') as file:
    lines=file.readlines()
for line in lines:
    print(line.strip().capitalize())