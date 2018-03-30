# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string
# that reads the same forwards and backwards.)

wrd = str(raw_input("Please enter a word: "))
rvs = wrd[::-1]
print(rvs)

if wrd.lower() == rvs.lower():
    print "This word is a palindrome"
else:
    print "This word is not a palindrome"