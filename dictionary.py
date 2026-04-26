orders = []

another = "yes"

while another == "yes":
    orderD = {}

    orderD["name"] = input("What's your name? ")
    orderD["item"] = input("What item do you wish to order? ")
    orderD["quantity"] = int(input("How many would you like? "))

    orders.append(orderD)

    another = input("Add another order? (yes/no) ")

<<<<<<< HEAD
print(orders[0])
=======
print(orders)
>>>>>>> eb05419db7a3a3ce0553efbedfdce6d82ec405da
