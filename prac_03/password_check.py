"""
Check password

Rhys Simpson
"""

MINIMUM_LENGTH = 3


def main():
    #
    #
    password = input("Enter a password: ")
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter a password: ")
    else:
        for i in password:
            print("*", end="")
        print()


main()
