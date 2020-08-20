"""
CP1404 - Practical
Calculate electricity bill based on tariff, daily usage and number of
billing days

Rhys Simpson
"""

print("Electricity Bill Calculator")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
price = 0

tariff = int(input("Which tariff? 11 or 31: "))
# Check which tariff was chosen and if it's valid
if tariff == 11:
    price += TARIFF_11
elif tariff == 13:
    price += TARIFF_31
else:
    print("Invalid tariff (Enter either 11 or 13)")
    exit()

daily_use = float(input("Enter daily use in kWh: "))
if daily_use > 24:  # No more than 24 hours in a day
    print("Enter daily hours less than 24")
    exit()

billing_days = int(input("Enter number of billing days: "))

bill = price * daily_use * billing_days  # Calculate final bill
print("Estimated bill: $", bill, sep=' ')
