# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list
# minus all the duplicates.
# Extras:
#    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#    Go back and do Exercise 5 using sets, and write the solution for that in a different function.


def no_duplicates_set(mylist = []):
    return list(set(mylist))


def no_duplicates_loop(mylist = []):
    newlist = []
    [newlist.append(x) for x in mylist if x not in newlist]
    return newlist

    # mylist.sort()
    # print mylist
    # newlist = []
    # newlist.append(mylist[0])
    # for x in range(0, len(mylist)-1):
    #     if mylist[x+1] != mylist[x]:
    #         newlist.append(mylist[x+1])
    # return newlist

    # newlist = []
    # for x in mylist:
    #     if x not in newlist:
    #         newlist.append(x)
    # return newlist


a = [5, 3, 3, 2, 2, 5, 6]
print no_duplicates_loop(a)
print no_duplicates_set(a)