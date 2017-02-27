# http://raspberrywebserver.com/gpio/using-interrupt-driven-gpio.html

import time
import RPi.GPIO as GPIO


# handle the button event
def buttonEventHandler (pin):
    print "handling button event"

    # turn the green LED on
    GPIO.output(25,True)

    time.sleep(1)

    # turn the green LED off
    GPIO.output(25,False)



# main function
def main():

    # tell the GPIO module that we want to use 
    # the chip's pin numbering scheme
    GPIO.setmode(GPIO.BCM)

    # setup pin 23 as an input
    # and set up pins 24 and 25 as outputs
    GPIO.setup(23,GPIO.IN)
    GPIO.setup(24,GPIO.OUT)
    GPIO.setup(25,GPIO.OUT)

    # tell the GPIO library to look out for an 
    # event on pin 23 and deal with it by calling 
    # the buttonEventHandler function
    GPIO.add_event_detect(23,GPIO.FALLING)
    GPIO.add_event_callback(23,buttonEventHandler)

    # turn off both LEDs
    GPIO.output(25,False)
    GPIO.output(24,True)

    # make the red LED flash
    while True:
        GPIO.output(24,True)
        time.sleep(1)
        GPIO.output(24,False)
        time.sleep(1)


    GPIO.cleanup()

if __name__=="__main__":
    main()
