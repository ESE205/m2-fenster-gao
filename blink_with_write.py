import sys
import time
import RPi.GPIO as GPIO

# SETTING UP GPIO PINS
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LED_PIN = 11
INPUT_PIN = 13
GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(INPUT_PIN, GPIO.IN)

# To count number of times light is on
i = 0

# Boolean to track state of switch
SWITCH_IS_ON = False

debug = False

if('-debug' in sys.argv): debug = True

blinkrate = float(input("Enter desired seconds per blink (>.2): "))

secs = int(input("Enter desired runtime in seconds: "))

# When called blinks led once
def blink():
    i+=1
    GPIO.output(pin1, GPIO.HIGH)
    time.sleep(.2)
    GPIO.output(pin1, GPIO.LOW)


t = time.time()+secs
b = time.time()

# Loop runs for specified amount of time
while(time.time()<t):
    if(GPIO.input(INPUT_PIN)):
        SWITCH_IS_ON = True 
        if(time.time()%b>blinkrate): blink()
    else: SWITCH_IS_ON = False

    with open('data.txt', 'w') as data:
        if(debug): data.write(f'{time.time():1.0f}\t{SWITCH_IS_ON}\n')

# Turning off pins
GPIO.cleanup()