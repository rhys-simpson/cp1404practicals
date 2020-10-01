"""
CP1404 - Practical
Calculate electricity bill based on tariff, daily usage and number of
billing days

Rhys Simpson
"""
print("Electricity Bill Calculator 2.0")
TARIFFS = {"TARIFF_11": 0.244618, "TARIFF_12": 0.213456, "13": 0.136928, "14": 0.114678, "15": 0.094567}
print("List of Tariffs: {}".format(TARIFFS))

price = 0
tariff = input("Which tariff? ")
if tariff in TARIFFS:
    price += TARIFFS[tariff]
else:
    print("Invalid tariff")
    exit()

daily_use = float(input("Enter daily use in kWh: "))
if daily_use > 24:  # No more than 24 hours in a day
    print("Enter daily hours less than 24")
    exit()

billing_days = int(input("Enter number of billing days: "))

bill = price * daily_use * billing_days  # Calculate final bill
print("Estimated bill: $", bill, sep=' ')