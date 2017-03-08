# http://raspberrywebserver.com/gpio/using-interrupt-driven-gpio.html

import time
import RPi.GPIO as GPIO

# Pinout 
button_1 = 3
button_2 = 5
button_3 = 7

# handle the button event
def buttonEventHandler (pin):
    if   pin == button_1:
        print("handling button 1 event")
    elif pin == button_2:
        print("handling button 2 event")
    elif pin == button_3:
        print("handling button 3 event")
    else:
        print("unhandled gpio event")

class init(object):
  
    def __init__(self):
        # tell the GPIO module that we want to use 
        # the chip's pin numbering scheme
        GPIO.setmode(GPIO.BCM)

        # setup buttons as an inputs
        GPIO.setup(button_1,GPIO.IN)
        GPIO.setup(button_2,GPIO.IN)
        GPIO.setup(button_3,GPIO.IN)

        # tell the GPIO library to look out for an 
        # event on button's pins and deal with it by calling 
        # the buttonEventHandler function
        GPIO.add_event_detect  (button_1,GPIO.FALLING)
        GPIO.add_event_callback(button_1,buttonEventHandler)
        GPIO.add_event_detect  (button_2,GPIO.FALLING)
        GPIO.add_event_callback(button_2,buttonEventHandler)
        GPIO.add_event_detect  (button_3,GPIO.FALLING)
        GPIO.add_event_callback(button_3,buttonEventHandler)


    def close(self):
        GPIO.cleanup()

if __name__=="__main__":
    main()
