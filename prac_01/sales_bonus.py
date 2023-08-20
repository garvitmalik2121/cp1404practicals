"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Pseudocode
get sales
while sales >= 0
    if sales <1000
    bonus rate = 10
    else
    bonus rate = 15
    calculate users bonus
    print users bonus
"""
sales = float(input("Enter sales: $"))
while sales >= 0:

    if sales < 1000:
        bonus_rate = 10
    else:
        bonus_rate = 15
    users_bonus = sales*bonus_rate/100
    print(f"your bonus is {users_bonus}")
    sales = float(input("Enter sales: $"))


