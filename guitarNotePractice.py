
import random as r

notes = ['A','B','C','D','E','F','G']
noteOfDay = notes[r.randint(0,6)]

print "\n|-------------------------------|"
print "|Welcome to Guitar Note Practice|"
print "|-------------------------------|\n"

print "The note of the day is " + noteOfDay +"\n"

userInput = True

print "I'll give you:"
print " 1  A note in scientific pitch notation"
print " 2  A note and the string on which to play it"
print " 3  A new note of the day"
print " 0  Quit\n"

while(userInput):

  try:
    userInput = input( "Enter your selection:\n")

    # shitty switchcase subsitute
    if (userInput == 1):
      print "\nPlay a " + noteOfDay + str(r.randint(1,4)) + "\n"
    elif userInput == 2:
      print "\nPlay a "+noteOfDay+" on the " + \
             str(r.randint(1,6)) + " string\n" 
    elif userInput == 3:
      noteOfDay = notes[r.randint(0,6)]
      print "\n Note of the day changed to " + noteOfDay + "\n"
    elif userInput == 0:
      print "\n Exiting\n" 
    else:
      print "\nInvalid entry, try again"
      print "I'll give you:"
      print " 1  A note in scientific notation"
      print " 2  A note and the string on which to play it"
      print " 3  A new note of the day"
      print " 0  Quit\n"

  except:
    print "\nInvalid entry, try again"
    print "I'll give you:"
    print " 1  A note in scientific notation"
    print " 2  A note and the string on which to play it"
    print " 3  A new note of the day"
    print " 0  Quit\n"


