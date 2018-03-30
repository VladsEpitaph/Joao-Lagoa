# Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.
# Extras:
#    Randomly generate two lists to test this
#    Write this in one line of Python (dont worry if you cant figure this out at this point - well get to it soon)

import random

low = 0
high = 20

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = random.sample(range(low, high), 10)
b = random.sample(range(low, high), 10)
print a
print b
print list(set(a) & set(b))
# finallist = []
# a.sort()
# b.sort()
# tmp1 = -1
# tmp2 = -1
# for elementsa in a:
#     if tmp1 == elementsa:
#         continue
#     tmp1 = elementsa
#
#     for elementsb in b:
#         if tmp2 == elementsb:
#             continue
#         tmp2 = elementsb
#
#         if cmp(elementsa,elementsb) == 0:
#             finallist.append(elementsa)
#             break


