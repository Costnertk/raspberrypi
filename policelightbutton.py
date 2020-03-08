import RPi.GPIO as GPIO
import time

bluePin1 = 11
redPin1 = 13
bluePin2 = 15
redPin2 =16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def blink(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def redOn():
    blink(redPin1)
    blink(redPin2)

def redOff():
    turnOff(redPin1)
    turnOff(redPin2)

def blueOn():
    blink(bluePin1)
    blink(bluePin2)

def blueOff():
    turnOff(bluePin1)
    turnOff(bluePin2)

def policelights():
    redOn()
    print("WEEEEEEEEE")
    time.sleep(.1)
    redOff()
    blueOn()
    print("WOOOOOOO")
    time.sleep(.1)
    blueOff()

def stripe():
    blink(redPin1)
    time.sleep(.5)
    turnOff(redPin1)
    blink(bluePin1)
    time.sleep(.5)
    turnOff(bluePin1)
    blink(redPin2)
    time.sleep(.5)
    turnOff(redPin2)
    blink(bluePin2)
    time.sleep(.5)
    turnOff(bluePin2)


def main():
    
    while True: # Run forever
        policelights()
main()