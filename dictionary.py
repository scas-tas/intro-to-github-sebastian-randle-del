orders = []

another = "yes"

while another == "yes":
    orderD = {}

    orderD["name"] = input("What's your name? ")
    orderD["item"] = input("What item do you wish to order? ")
    orderD["quantity"] = int(input("How many would you like? "))

    orders.append(orderD)

    another = input("Add another order? (yes/no) ")

print(orders)