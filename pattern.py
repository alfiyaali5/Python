def triangle(n):
    # number of spaces
    k = n - 1

    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

        # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print(" * ", end="")

        # ending line after each row
        print("\r")
n = 5
triangle(n)
#*************************************************

row=int (input("enter the num of row"))
for i in range (row):
    for j in range(i+1):
        print("* " , end="")
    print("")

#************************************

row=int (input("enter the num of row"))
for i in range (row , 0 , -1):
    for j in range(0 , i):
        print(" *" , end=" ")
    print("\n")

# *******************************

row=int(input("enter the num of row"))
for i in range (row +1,1 ):
    for j in range(1, row +1,1):
        print(" *" , end=" ")
    print("\n")

row=int(input("enter the no of row"))
for i in range(row):
    for j in range(i+1):
        print("A",end="")
    print("")

def fibonacci(n):
    if n<0:
        print("incorrect no")
    elif n==0:
        return 0
    elif n==1 and n==2:
        return 1
    else:
        result= fibonacci(n-1)+fibonacci(n-2)
        print (result)

fibonacci(9)

row=int(input("enter the row : "))
for i in range(row):
    for j in range(i):
        print('*',end=' ')
    print('\r')


def right_angle_triangle(height):
    for i in range(1, height + 1):
        # Print spaces before the '*'
        print(' ' * (height - i), end='')

        # Print '*' for each row
        print('*' * i)

num=int(input('no of row'))
# Example: Create a right-angled triangle with height 5
right_angle_triangle(5)

row=int(input("Enter the no of row : "))
for i in range(row):
    for j in range(i):
        print('* ', end='')
    print('\r')

row=int(input("enter the no of row"))
for i in range(1, row + 1):
    # Print spaces before the asterisks
    for _ in range(row - i):
        print(" ", end=" ")

    # Print the asterisks
    for _ in range(i):
        print("*", end=" ")

    # Move to the next line after each row
    print()



