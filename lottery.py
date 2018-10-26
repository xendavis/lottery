import random, easygui, locale # imports random number generator, the GUI program, and a comma seperator
locale.setlocale(locale.LC_ALL, 'en_US') # sets language to english
TEST = False # set True for testing purposes only

maxResults = 47 # the max number the user can pick
maxPicks = 5 # the max number of times the user puts in input
userpicks = []  # we start with blanks for the values

potClean = random.randint (500000, 100000000) # generates a random amount of money to put in the pot
potDivisors = [0, 16000, 8000, 320, 32] # divides pot depending on matches
pot = locale.format_string("%d", potClean, grouping=True) # puts comma seperators in the pot
title = "Lottery"
okBox = "Continue"

def match_lists(list1, list2): # match list function
    """to find the number of matching items in each list use sets"""
    set1 = set(list1)
    set2 = set(list2)
    set3 = set1.intersection(set2) # set3 contains all items common to set1 and set2
    return set3 # return number of matching items

def winning_numbers(): # generate winning numbers function
    results = [] # results of the random generator
    if TEST:
        results = [1, 2, 3, 4, 5]
    else:
        for _ in range (0, maxPicks): # loop to pick the winning numbers
            computerPick = random.randint (1, maxResults)
            while computerPick in results:
                computerPick = random.randint (1, maxResults)
            results.append(computerPick) # picks numbers in this line and makes sure it picks it in the range of numbers it can pick1
    results = sorted(results) # sorts the picks of the computer from least to greatest
    return results
computerResults = winning_numbers()

msg = "Todays Jackpot: $" + str(pot) + ".\n\nNumbers must be between 1 to 47 and no entrees must repeat!\n\nEnter your winning numbers"
fieldNames = ["1st Number","2nd Number","3rd Number","4th Number","5th Number"]

validatePicks = True
while validatePicks: # loop until we have valid picks
    userpicks = easygui.multenterbox(msg, title, fieldNames, userpicks)
    validPicks = []
    print(userpicks)
    if userpicks == None: # if there is no user input break
        print("No user input")
        exit
    errmsg = "" # start with empty error message
    for i in range(0, len(fieldNames)):
        userPick = int(userpicks[i].strip())
        print("len =  ",len(fieldNames),"i  =  ",i,"userPick  = ", userPick)
        if userPick >= 1 and userPick <= maxResults and userPick not in validPicks:
            validPicks.append(userPick)
            print("userPick ", userPick, " is valid")
        else:
            errmsg = errmsg + ('"%s" must be an number between 1 and %s and no entrees must repeat!.\n\n' % (fieldNames[i], maxResults))
    if len(validPicks) == len(userpicks): break
    msg = errmsg 

print("Reply was:", validPicks)
validPicks = sorted(validPicks) # sorts the picks of the user from least to greatest

resultbox1 = "Your Numbers: " + str(validPicks)
easygui.msgbox(resultbox1, title, okBox) # i

resultbox2 = "Winning Numbers: " + str(computerResults)
easygui.msgbox(resultbox2, title, okBox) # prints the computerResults list

matches = match_lists(validPicks, computerResults) # compares the two lists to see if the user has any matches against the winning numbers

winbox1Plural = "You matched the numbers: " + str(list(matches))
winbox2Plural = "You have " + str(len(matches)) + " winning numbers"

winbox1Single = "You matched the number: " + str(list(matches))
winbox2Single = "You have " + str(len(matches)) + " winning number"

# determine number of matches and winnings and display to user
if len(matches) > 0 and len(matches) <= 4:
    winnings = potClean / potDivisors[len(matches)]
    winningsFORMAT = locale.format("%d", winnings, grouping=True)
    winMsg = "Congrats! You won $" + str(winningsFORMAT) + " because you matched " + str(len(matches)) + " number!\n\nThe grand total was $" + str(pot)
    print("potDivisor  = ", potDivisors[len(matches)])
    print("winnings  = ",  winningsFORMAT)

if len(matches) > 1 and len(matches) < 5:
    easygui.msgbox(winbox1Plural, title, okBox)
    easygui.msgbox(winbox2Plural, title, okBox)
    easygui.msgbox(winMsg, title, okBox)
elif len(matches) == 5:
    jackpot = "JACKPOT! You matched all 5 numbers."
    winningsJackpot = "You won the grand total of: $" + str(pot)
    easygui.msgbox(jackpot, title, okBox)
    easygui.msgbox(winningsJackpot, title, okBox)
elif len(matches) == 1:
    easygui.msgbox(winbox1Single, title, okBox)
    easygui.msgbox(winbox2Single, title, okBox)
    easygui.msgbox(winMsg, title, okBox)
elif len(matches) == 0:
    losebox = "You did not match any numbers.\n\nNot every ticket is a winner!"
    easygui.msgbox(losebox, title, okBox)