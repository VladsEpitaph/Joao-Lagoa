# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
# the first and last elements of the given list. For practice, write this code inside a function


def first_last(mylist = [0, 1]):
    if len(mylist) != 0:
        return [mylist[0], mylist[-1]]
        # return [mylist[0], mylist[len(mylist)-1]]
    else:
        return mylist


a = [5, 10, 15, 20, 25]
print first_last(a)