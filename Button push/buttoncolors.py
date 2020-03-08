import RPi.GPIO as GPIO
import time

redPin = 11
greenPin = 13
bluePin = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

def blink(pin):
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def redOn():
    blink(redPin)
    time.sleep(.1)
    turnOff(redPin)

def greenOn():
    blink(greenPin)
    time.sleep(.1)
    turnOff(greenPin)

def blueOn():
    blink(bluePin)
    time.sleep(.1)
    turnOff(bluePin)

def main():
    
    while True: # Run forever
        if GPIO.input(8) == GPIO.HIGH and GPIO.input(10) == GPIO.HIGH:
            blueOn()
        elif GPIO.input(8) == GPIO.HIGH:
            redOn()
        elif GPIO.input(10) == GPIO.HIGH:
            greenOn()

main()