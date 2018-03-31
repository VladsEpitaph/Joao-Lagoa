# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the
# user the same string, except with the words in backwards order. For example, say I type the string:
#  My name is Michele
# Then I would see the string:
#  Michele is name My
# shown back to me.


def ask(text="Pick a number: "):
    # Returns integer value for input. text is displayed text
    return raw_input(text)


def reverse_world_order(string = []):
    return string.split()[::-1]


def add_spaces(string = []):
    return ' '.join(string)


string = ask("Give me a string so i can reverse it: ")
print add_spaces(reverse_world_order(string))