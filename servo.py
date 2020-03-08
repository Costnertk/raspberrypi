import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

def Open():
    p.ChangeDutyCycle(12.5)
def Close():
    p.ChangeDutyCycle(2.5)

def main():
    while True:
        cmd = raw_input("-->")


        if cmd == "open":
            Open()
        elif cmd == "close":
            Close()
        else:
            print("Not a valid command")
    return

main()