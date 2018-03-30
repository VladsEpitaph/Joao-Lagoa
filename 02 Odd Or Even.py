# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
# to the user.
# Extras:
# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(raw_input("What is the number you want to divide: "))
check = int(raw_input("What is the divider: "))
if num % 4 == 0:
    print("The number is a multiple of 4.")
if num % check != 0:
    print("The numbers don't divide evenly")
else:
    print("The numbers divide evenly")