"""
CP1404 - Practical
Create a menu that displays the users name and gives options to either choose
hello or goodbye then followed by the users name, or quit the program.

Rhys Simpson
"""

menu = "(H)ello\n(G)oodbye\n(Q)uit\n"
name = input("Enter name: ")
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice.")
    print(menu)
    choice = input(">>> ").upper()
print("Finished.")
