import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
import time   
import sys
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering



ITER_COUNT = 15
DEBUG = False
if '-debug' in sys.argv:
   DEBUG = True  

LED_PIN = 11
INPUT_PIN = 13

# CHECK IF SWITCH IS ON
GPIO.setup(INPUT_PIN, GPIO.IN) # sets pin as input
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW) # Sets led pin to output and led to low

# INFINITE LOOP WHERE IF SWITCH IS CONNECTED LED IS ON
while True:
    if(GPIO.input(INPUT_PIN)):  GPIO.output(LED_PIN, 1)
    else: GPIO.output(LED_PIN, 0)



GPIO.cleanup() 
