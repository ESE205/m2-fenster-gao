import sys
import time
import RPi.GPIO as GPIO

# SETTING UP GPIO PINS
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LED_PIN = 11
INPUT_PIN = 13
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(INPUT_PIN, GPIO.IN)

# To count number of times light is on
global i
i = 0

# Boolean to track state of switch
SWITCH_IS_ON = False

debug = False

if('-debug' in sys.argv): debug = True

blinkrate = float(input("Enter desired seconds per blink (>.2): "))

secs = int(input("Enter desired runtime in seconds: "))

# When called blinks led once
def blink():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(LED_PIN, GPIO.LOW)


t = time.time()+secs
b = time.time()

# Loop runs for specified amount of time
with open('data.txt', 'w') as data:
    while(time.time()<t):
        if(GPIO.input(INPUT_PIN)!= SWITCH_IS_ON):
            data.write(f'{time.time():1.0f}\t{SWITCH_IS_ON}\n')
        if(GPIO.input(INPUT_PIN)):
            SWITCH_IS_ON = True 
            if(time.time()%b>blinkrate):
                i += 1
                b = time.time()
                blink()
        else: SWITCH_IS_ON = False

        if debug:
            print(f'{time.time():1.0f}\t{i}\t{SWITCH_IS_ON}\n')

# Turning off pins
GPIO.cleanup()
