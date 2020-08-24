"""
CP1404 - practical
1. Code that asks the user for their name,
then opens a file called "name.txt" and writes that name to it.

2. Code that opens "name.txt" and reads the name (as above) then prints

3. Code that opens "numbers.txt", reads only the first two numbers (numbers are 17,42,400)
and adds them together then prints the result, which should be 59.

4. Code that prints the total for all lines in numbers.txt or a file with any number of numbers.

Rhys Simpson
"""

# 1.
out_file = open("name.txt", 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

# 3.
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

# 4.
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
