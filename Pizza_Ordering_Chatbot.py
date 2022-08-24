print("Hello, my name is Alex your virtual assistant. I will help you order a pizza!")
print("I am going to ask you a few questions. After typing an answer, press enter.")
print("\n")
userName = input("Enter your name:  ")

while (len(userName) == 0):
    userName = input("Please enter your name: ")

if userName.lower() == "edward morris":
    print("\nMy creator, " + userName + ". Pleasure to serve you!")
else:
    print("Hello, " + userName + ". Thanks for ordering your pizza with us!")

keepGoing = "y"
while keepGoing.lower() == "y":


    size = input("\nWhat size do you want? Enter small, medium, or large:  ").lower()

    while size != "small" and size != "medium" and size != "large":
        size = input("Invalid value. Please enter small, medium, or large to continue.: ").lower()

    flavor = input("\nEnter the flavor of pizza:  ")

    while (len(flavor) == 0):
        flavor = input("Flavor of pizza is missing. Please enter pizza flavor to continue.: ")

    crustType = input("\nWhat type of crust do you want:  ")

    while (len(crustType) == 0):
        crustType = input("Pizza crust type is missing. Please enter pizza crust type to continue.: ")

    quantity = input("\nHow many of these do you want to order:  ")

    while not quantity.isdigit():
        quantity = input("\nValue not recognized. Please enter a numeric value: ")

    quantity = int(quantity)

    method = input("\nIs this carry out or delivery:  ").lower()

    while method != "delivery" and method != "carry out" and method != "carryout":
        method = input("Invalid value. Please enter carry out or delivery to continue.: ").lower()

    salesTax = 1.1

    if size.lower() == "small":
        pizzaCost = 8.99
    elif size.lower() == "medium":
        pizzaCost = 14.99
    elif size.lower() == "large":
        pizzaCost = 17.99

    if method.lower() == "delivery":
        deliveryFee = 5
    else:
        deliveryFee = 0

    total = (pizzaCost * quantity) * salesTax + deliveryFee
    print("\n----------------")
    print("Thank you,", userName, ", for your order.")
    print("Your", quantity, size, flavor, "pizza with", crustType,"crust costs", "${:,.2f}".format(total) + ".")
    if total >= 50:
        print("\nCongraduations, you've been awared a $10 off coupon for your next order!")
    else:
        print("\nOrders over $50 will receive a free $10 off coupon!")
    print("----------------")

    print("Order has been received. ETA 3 mins!")

    for min in range(3, 1, -1):
        print(min, "minutes remaining")
        for seconds in range(60, 0, -1):
            print(seconds, end = " \r")
            import time
            time.sleep(1)
    print("Order is ready!")

    keepGoing = input("Do you want to place another order? Enter y or n:  ")

