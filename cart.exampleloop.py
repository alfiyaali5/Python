'''#first Logic
cart=[]
items=input("enter a value of item that you want to aad to cart:")
cart.append(items)
print(cart)
#for loop to add cart
cart=[]
n=int(input("enter the no of values:"))
for x in range(n):
    items = input("enter the item that you want to aad to cart:")
    cart.append(items)
print(cart)
#while loop is choice given to user that he/she want to buy or not
cart=[]
while True:
    choice=input("do you want to add items?")
    if choice=="yes":
      items = input("enter the item that you want to aad to cart:")
      cart.append(items)
      print(cart)
    else:
     break'''
# creating a list of product
products=[
    {"name":"smartphone","price":40000,"description":"it is nice phone"},
    {"name": "ac", "price": 200000, "description": "it is nice phone"},
    {"name": "lamp", "price": 30000, "description": "it is nice phone"},
    {"name": "laptop", "price": 100000, "description": "it is nice phone"}
]
'''cart=[]
while True:
    choice=input("do you want to add items?")
    if choice=="yes":
        print("here is the list of the product along with their price and descripion")
        for product in products:
            print(f"{product["name"]}:{product["description"]}:{product["price"]}")
        items = input("enter the item that you want to aad to cart:")
        if items==products:
             print("This is available")
        else:
            print("Sorry , the product is unavailable")
            items = input("enter the item that you want to aad to cart other than this:")
        cart.append(items)
        print(cart)
    else:
         break
print("thankyou for shopping here is the final connect of cart is{cart}")'''
#select the value by using index
'''cart=[]
while True:
    choice =input("doyou want to continue shopping?")
    if choice=='yes':
        print("here is the list of the products and their prices:")
        for index,product in enumerate(products):
            print(f"{index}:{product['name']}:{product['description']}:{product['price']}")
        product_id = int(input("enter the product id that you want to add to cart"))
        cart.append(products[product_id])
        print(f"currentcart item are here")
        for product in cart:
            print(f"{product['name']}:{product['price']}")
    else:
            break
print(f"thankyou for shopping here is the final content of cart{cart}")'''
#quantity of the products
'''cart=[]
while True:
    choice =input("doyou want to continue shopping?")
    if choice=='yes':
        print("here is the list of the products and their prices:")
        for index,product in enumerate(products):
            print(f"{index}:{product['name']}:{product['description']}:{product['price']}")
        product_id = int(input("enter the product id that you want to add to cart"))
            #check if product is already present in cart
        if products[product_id] in cart:
           products[product_id]['quantity']+=1 #in this case increase the quantity of product rather than add it to cart
        else:
           products[product_id]['quantity']=1
           cart.append(products[product_id])
           print("Here are the ontents in your cart")
           for product in cart:
             print(f"{product['name']}:{product['price']}:{product['quantity']}")
    else:
        break
print(f"thankyou for shopping here is the final content of cart{cart}")'''
#total of the shopping cart
cart=[]
while True:
    choice =input("doyou want to continue shopping?")
    if choice=='yes':
        print("here is the list of the products and their prices:")
        for index,product in enumerate(products):
            print(f"{index}:{product['name']}:{product['description']}:{product['price']}")
        product_id = int(input("enter the product id that you want to add to cart"))
         # check if product is already present in cart
        if products[product_id] in cart:
            #increase the quantity of the product rather than adding it to cart again
           products[product_id]['quantity']+=1
        else:
           products[product_id]['quantity']=1
           cart.append(products[product_id])

           total=0
           quantity=0
           print("Here are the content in your cart:")
           for product in cart:
             print(f"{product['name']}:{product['price']}:{product['quantity']}")
             total+=product['price']*product['quantity']
             quantity+=product['quantity']
           print(f"cart total is: {quantity} : ${total}")
    else:
        break
print(f"thank you for shopping,Your total bill is : {quantity} : ${total}")

