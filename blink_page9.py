import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import sys

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

ITER_COUNT = 20
DEBUG = False
if "-debug" in sys.argv:
    DEBUG = True

LED_PIN = 11
LED_IS_ON = False

GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

with open("data.txt", "w") as data:
    for i in range(0,ITER_COUNT): # loop through 30 times
        GPIO.output(LED_PIN, LED_IS_ON)
        data.write(f"{time.time()*1000:1.0f} {LED_IS_ON}\n")
        if DEBUG:
            print(f"LED is on: {LED_IS_ON}")
        LED_IS_ON = not(LED_IS_ON)
        time.sleep(1)

GPIO.cleanup()
