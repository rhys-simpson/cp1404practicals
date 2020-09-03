"""
CP1404/CP5632 Practical
State names in a dictionary

Rhys Simpson
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

# loop to print all state codes and names
for state_code in CODE_TO_NAME:
    print("{:<3} is {}".format(state_code, CODE_TO_NAME[state_code]))


state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
