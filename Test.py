import time
import random
from multiprocessing import Queue
#from twython import Twython
from msvcrt import getch
import keyboard

#Add python to PATH, PIP install Twython, Idna


API_KEY = "SktkXmOAq0E4eCjYnsfg9eBEX"
API_SECRET = "xNs5SCkoTInipoPX3cl24RDsekhEWgF7e2VeeLVasLtj0D03WM"
ACCESS_TOKEN = "727874160446214144-lTjQOJCFmLIkLQfUMmG8BVnWYKCuNbD"
ACCESS_TOKEN_SECRET = "xjhblJyMsYPoMfddL0UXV8ZeBSpyzWv99atFJA5rY2SF6"

#twitter_client = Twython(API_KEY,API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


Tweet_f = open("Tweet_Strings.txt")

File_String = Tweet_f.readlines()

prev_f = open("Previously_Stored_String.txt", "r+")

Previous_String = prev_f.readlines()

prev_Next = open("Next_Prev.txt", "r+")

Next_Prev = prev_Next.readlines()

prev_Final = open("Final_Prev.txt", "r+")

Final_Prev = prev_Final.readlines()

#randomString = random.choice(File_String)

# twitter_client.update_status(status='What  a great day for a walk!')


#repeatString = 0

#heldString = ""

PreviouslyRecorded = 0

randomString = random.choice(File_String)
heldString = random.choice(Previous_String)

def testForPrev (string):
    if string == randomString:
#        if string == Next_Prev:
            print("Error")
#        else:
 #           print("Next_Prev Passed.")
    else:
        print(randomString)
        prev_f = open('Previously_Stored_String.txt', 'w').close()
        prev_f = open('Previously_Stored_String.txt', 'r+')
        prev_f.write(randomString + '\n')



heldString = ""




true = 1

#while True:
while true < 100:
        if keyboard.is_pressed('d'):
            testForPrev(heldString)
            #keyboard.press('enter')
            true = true + 1
            randomString = random.choice(File_String)
            time.sleep(5)
        if true == 100:
            true = 0



    #break


















#        else:
#            pass


#print (heldString)

#if heldString == randomString:
#    print ("Error")
#   PreviouslyRecorded + 1
 #   print(PreviouslyRecorded)





















#randomString = random.choice(File_String)
#heldString = heldString

#if heldString == randomString:
#    print (heldString, "Repeated")


# Prints from File with randomization
