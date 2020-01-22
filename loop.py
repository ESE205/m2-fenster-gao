import sys
DEBUG = True # Turn on or off debug to help debug program
loopCount = 5 # defaults to 5

if (len(sys.argv) > 1):
    loopCount = int(sys.argv[1])
if (len(sys.argv) > 2): 
    if (int(sys.argv[2])> 0):
        DEBUG = True
    else:
        DEBUG = False

if (DEBUG): print (f"Number of times through loop: {loopCount}")

i = 0
while (i < loopCount):
    i = i + 1
    print (f'Looping: {i}')

loopCount = int(input("Enter new loop count:"))

i = 0
while (i < loopCount):
    i = i + 1
    print (f"Looping: {i}")
