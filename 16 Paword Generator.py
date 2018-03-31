# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
# every time the user asks for a new password. Include your run-time code in a main method.
# Extra:
#    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
import random
import string


def ask(text="Pick a number: "):
    # Returns integer value for input. text is displayed text
    return raw_input(text)


def generate_strong_password(size = 4):
    options = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    return "".join(random.sample(options, size))


def generate_weak_password(size = 4, lowercase = 0, uppercase = 0, num = 0, sym = 0):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = string.digits
    symbol = string.punctuation
    setgroup = ""
    if lowercase == 1:
        setgroup += lower
    if uppercase == 1:
        setgroup += upper
    if num == 1:
        setgroup += number
    if sym == 1:
        setgroup += symbol
    return "".join(random.sample(setgroup, size))


choice = str(ask("What kind of password ('w'eak or 's'trong): "))
if choice == "w":
    size = int(ask("How long: "))
    lowercase = int(ask("Lowercase (0 - no, 1 - yes): "))
    uppercase = int(ask("Uppercase (0 - no, 1 - yes): "))
    num = int(ask("Numbers (0 - no, 1 - yes): "))
    sym = int(ask("Symbols (0 - no, 1 - yes): "))
    print generate_weak_password(size, lowercase, uppercase, num, sym)
elif choice == "s":
    size = int(ask("How long: "))
    print generate_strong_password(size)
