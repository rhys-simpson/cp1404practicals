"""
CP1404 - Practical
Shop calculator that calculates price of items
If the item price is over $100 a 10% discount is applied

Rhys Simpson
"""

total = 0
item = int(input("Number of items: "))
if item < 0:
    print("Invalid Number of items!")
    item = int(input("Number of items: "))

for i in range(item):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9

print("Total price for", item, "items is $", total, sep=' ')
