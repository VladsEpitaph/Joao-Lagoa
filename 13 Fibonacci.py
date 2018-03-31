# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this
# opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the
# sequence to generate.(Hint: The Fibonnaci sequence is a sequence of numbers where the next number in the sequence is
# the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, ...)


def fibonacci(number = 1):
    # Returns the fibonacci sequence of x's number
    fiblist = [1, 1]
    if number == 0:
        return []
    elif number == 1:
        return [1]
    elif number == 2:
        return fiblist
    for x in range(2, number):
        fiblist.append(fiblist[x-1]+fiblist[x-2])
    return fiblist


def ask(text="Pick a number: "):
    # Returns integer value for input. text is displayed text
    return raw_input(text)


print fibonacci(int(ask("How many numbers of the Fibonacci sequence you want generated: ")))
