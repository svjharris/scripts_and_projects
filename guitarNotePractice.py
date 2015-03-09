import sys, random as r

def printTitle():
    print "\n|-------------------------------|"
    print "|Welcome to Guitar Note Practice|"
    print "|-------------------------------|\n"

def printOptions():
    print "I'll give you:"
    print " 1 A note in scientific pitch notation"
    print " 2 A note and the string on which to play it"
    print " 3 A new note of the day"
    print " 4 Some advice"
    print " 0 Quit\n"

def getNote():
    return('ABCDEFG'[r.randint(0,6)])

def printNote(note):
    print "The note of the day is {0}\n".format(note)

def printError():
    print "\nInvalid entry, try again"
    printOptions()

def getUserOptions(note):
    printOptions()
    while(True):
        try:
            userInput = int(input( "Enter your selection:\n"))
        except:
            printError()
        if(userInput == 1):
            print "\nPlay a {0}{1}\n".format(note, str(r.randint(1,4)))
        elif(userInput == 2):
            print "\nPlay a {0} on the {1} string".format(note, str(r.randint(1,6)))
        elif(userInput == 3):
            note = getNote()
            print "\n Note of the day changed to {0}\n".format(note)
        elif(userInput == 4):
            print "Listen to Jerry Garcia"
        elif userInput == 0:
            sys.exit()
        else:
            printError()


note = getNote()
printTitle()
printNote(note)
getUserOptions(note)
