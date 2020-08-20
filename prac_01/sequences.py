"""
CP1404 - Practical
Create a menu that takes a users input and displays number sequences -
Shows even numbers between an upper and lower limit
Shows odd numbers between an upper and lower limit
Shows squares between an upper and lower number limit

Rhys Simpson
"""
# Didn't get this one fully working but thought i'd upload it anyway.

print("Number Sequence Generator")
x = int(input("Enter lower limit (x): "))
y = int(input("Enter upper limit (y): "))

menu = "(E)ven\n(O)dd\n(S)qaures\n(Q)uit\n"
print(menu)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "E":
        if x % 2 != 0:
            x = x + 1
        for i in range(x, y + 1, 2):
            print(i, end=" ")
        print()
    elif choice == "O":
        if x % 2 == 0:
            x = x + 1
        for i in range(x, y + 1, 2):
            print(i, end=" ")
        print()
    elif choice == "S":
        for i in range(x, y + 1):
            print(i, end=" ")
        print()
    else:
        print("Invalid Choice!")
    print(menu)
    choice = input(">>> ").upper()
print("Finished.")
