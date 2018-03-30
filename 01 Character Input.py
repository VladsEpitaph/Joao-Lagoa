# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# 1. Add on to the previous program by asking the user for another number and printing out that many copies of
# the previous message.
# 2. Print out that many copies of the previous message on separate lines.

name = raw_input("What is your name: ")
age = int(raw_input("How old are you: "))
year = str((2018 - age)+100)
multiplePrints = int(raw_input("How many times do you want the message printed: "))
while multiplePrints:
    multiplePrints -=1
    print(name + " will be 100 years old in the year " + year+"\n")
