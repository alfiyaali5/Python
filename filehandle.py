with open('text.txt','r')as file:
     c=file.read()
     print(c)
#for readline and readlines
with open('text.txt', 'r') as file:
    c1 = file.readline()
    print(c1)
#readlines
with open('text.txt', 'r') as file:
    c2 = file.readlines()        #to read lines one by one this readlines funtion is use
for x in c2:
    print(x)
#readline
with open('text.txt', 'r') as file:
    c = file.readline()
    c1=file.readline()
    print(c)
    print(c1)
#strip
text="       hello world        "
new_text=text.strip()                #lstrip for remove left side space
print(new_text)                      #rstrip for remove right side space
print(text)

