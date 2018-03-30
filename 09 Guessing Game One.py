# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
# whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very
# first exercise)
# Extras:
#    Keep the game going until the user types "exit"
#    Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random

print "Guessing Game One!"
randomnumber = int(random.sample(range(1, 10), 1)[0])

i = 1
counter = 0
while i > 0:
    counter += 1
    number = raw_input("Pick a number between 1 and 9 (write 'exit' to finish): ")
    if str(number) == "exit":
        print "Bye"
        break
    elif (int(number) < 1) or (int(number) > 9):
        print "Bad Input!"
    elif int(number) > randomnumber:
        print "Your number is too high!"
    elif randomnumber > int(number):
         print "Your number is too low!"
    elif randomnumber == int(number):
        print "Nice guess!"
        print "It took you", counter,"tries to find it!"
        break
