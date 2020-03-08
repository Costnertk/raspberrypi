import RPi.GPIO as GPIO
import time

redPin = 11
greenPin = 13
bluePin = 15

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

def redOff():
    turnOff(redPin)

def greenOn():
    blink(greenPin)

def greenOff():
    turnOff(greenPin)

def blueOn():
    blink(bluePin)

def blueOff():
    turnOff(bluePin)

def yellowOn():
    blink(redPin)
    blink(greenPin)

def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)

def cyanOn():
    blink(greenPin)
    blink(bluePin)

def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)

def magentaOn():
    blink(redPin)
    blink(bluePin)

def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)

def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)

def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)

def redNotification():
    redOn()
    time.sleep(.5)
    redOff()
    time.sleep(1)
    redOn()
    time.sleep(.5)
    redOff()
    time.sleep(1)
    redOn()
    time.sleep(.5)
    redOff()

def blueNotification():
    blueOn()
    time.sleep(.5)
    blueOff()
    time.sleep(1)
    blueOn()
    time.sleep(.5)
    blueOff()
    time.sleep(1)
    blueOn()
    time.sleep(.5)
    blueOff()

def greenNotification():
    greenOn()
    time.sleep(.5)
    greenOff()
    time.sleep(1)
    greenOn()
    time.sleep(.5)
    greenOff()
    time.sleep(1)
    greenOn()
    time.sleep(.5)
    greenOff()

def rgbNotification():
    redOn()
    time.sleep(.1)
    redOff()
    time.sleep(.2)
    blueOn()
    time.sleep(.1)
    blueOff()
    time.sleep(.2)
    greenOn()
    time.sleep(.1)
    greenOff()
    time.sleep(3)
    redOn()
    time.sleep(.1)
    redOff()
    time.sleep(.2)
    blueOn()
    time.sleep(.1)
    blueOff()
    time.sleep(.2)
    greenOn()
    time.sleep(.1)
    greenOff()
    time.sleep(3)
    redOn()
    time.sleep(.1)
    redOff()
    time.sleep(.2)
    blueOn()
    time.sleep(.1)
    blueOff()
    time.sleep(.2)
    greenOn()
    time.sleep(.1)
    greenOff()

def main():
    while True:
        cmd = raw_input("-->")


        if cmd == "red on":
            redOn()
        elif cmd == "red off":
            redOff()
        elif cmd == "green on":
            greenOn()
        elif cmd == "green off":
            greenOff()
        elif cmd == "blue on":
            blueOn()
        elif cmd == "blue off":
            blueOff()
        elif cmd == "yellow on":
            yellowOn()
        elif cmd == "yellow off":
            yellowOff()
        elif cmd == "cyan on":
            cyanOn()
        elif cmd == "cyan off":
            cyanOff()
        elif cmd == "magenta on":
            magentaOn()
        elif cmd == "magenta off":
            magentaOff()
        elif cmd == "white on":
            whiteOn()
        elif cmd == "white off":
            whiteOff()
        elif cmd == "red notification":
            redNotification()
        elif cmd == "blue notification":
            blueNotification()
        elif cmd == "green notification":
            greenNotification()
        elif cmd == "rgb notification":
            rgbNotification()
        else:
            print("Not a valid command")
    return

main()