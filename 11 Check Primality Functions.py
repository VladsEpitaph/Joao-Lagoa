# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime
# number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this
# opportunity to practice using functions, described below.
import math


def find_if_prime(number):
    # If prime returns 1, if not returns 0
    for elements in list(range(2, int(math.sqrt(number))))[::-1]:
        if number % elements == 0:
            return 0
    return 1


def ask(text="Pick a number: "):
    # Returns integer value for input. text is displayed text
    return raw_input(text)


if find_if_prime(int(ask("What number you want to know if is prime: "))) == 0:
    print "Your number isn't prime!"
else:
    print "Your number is prime!"
