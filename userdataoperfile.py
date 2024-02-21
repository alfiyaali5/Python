def save_userdata():
    name=input("enter the name :")
    roll_no=int(input("enter the roll no :"))
    email=input("enter the email :")
    contact=int(input("enter the number :"))

    user_data=(f"name :{name}\n roll_no :{roll_no}\n email :{email}\n contact :{contact}\n\n")

    with open('user_data','a')as file:
        file.write(user_data)
save_userdata()

def read_userdata():
    with open('user_data','r')as file:
        print(file.read())
read_userdata()




