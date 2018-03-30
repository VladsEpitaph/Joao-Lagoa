# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a
# message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
#    Rock beats scissors
#    Scissors beats paper
#    Paper beats rock
import random
print "Welcome to Rock Paper Scissors"

infintvariable = 1
while infintvariable> 0:
    i = 1
    while i > 0:
        pcchoice = str(raw_input("Choice (R, P, S): "))
        choices = ["R", "P", "S"]
        for element in choices:
            if pcchoice == element:
                i = 0
                break
            elif element == "S":
                print "Bad input!!!"
                break

    npcchoice = str(choices[int(random.sample(range(0, 3), 1)[0])])

    print "PC chose: "+npcchoice

    if (pcchoice == "R" and npcchoice == "R") or (pcchoice == "P" and npcchoice == "P") or (pcchoice == "S" and npcchoice == "S"):
        print "It's a draw!"
    elif (pcchoice == "R" and npcchoice == "S") or (pcchoice == "S" and npcchoice == "P") or (pcchoice == "P" and npcchoice == "R"):
        print "Player Won!"
    else:
        print "Player Lost!"

    i = 1
    while i > 0:
        repeat = str(raw_input("Do you want to play again? (Y, N): "))
        choices = ["Y", "N"]
        if repeat == "N":
            print "Until a next time!"
            infintvariable = 0
            break
        elif repeat == "Y":
            print "Let's Go!"
            break
        else:
            print "Bad input!!!"
