student=[]
#we take this as a loop
for i in range(5):
    marks=int(input("marks of english: "))
    #append to put marks in student
    student.append(marks)
    print(student)
    print("after sorting the marks")
    student.sort()
    print(student)
    
# another example
m1=int(input("enter the marks of 1st student:"))
m2=int(input("enter the marks of 2nd student:"))
m3=int(input("enter the marks of 3rd student:"))
m4=int(input("enter the marks of 4rth student:"))
m5=int(input("enter the marks of 5th student:"))
mark=[m1,m2,m3,m4,m5]
print(mark)
print("ater sorting in accending order")
#method of sorting (sorting formula)
mark.sort()
print(mark)

