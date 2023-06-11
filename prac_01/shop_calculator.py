"""CP1404/CP5632 - Practical
shop calculate pseudocode

Threshold price for discount = 100
get number of items
total price = 0
while number of items <0
    print invalid input
    get number of items again
for item price in number of items
    get item price
    total price += item price
        if total price > 100
        discount = total price *0.1
        total price -= discount
print total price for number of items"""


def calculate_total_price():
    number_items = int(input("Number of items: "))
    total_price = 0
    while number_items < 0:
        print("invalid number of items")
        number_items = int(input("Number of items: "))

    for price_of_item in range(number_items):
        price_of_item = float(input("Price of item: "))
        total_price += price_of_item

    if total_price > 100:
        discount = total_price * 0.1
        total_price -= discount

    print(f"Total price for {number_items} items is ${total_price:.2f}")


calculate_total_price()
