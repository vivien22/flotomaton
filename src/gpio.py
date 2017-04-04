# http://raspberrywebserver.com/gpio/using-interrupt-driven-gpio.html
# http://razzpisampler.oreilly.com/ch07.html

import time
import RPi.GPIO as GPIO

# Pinout 
button_1 = 3
button_2 = 5
button_3 = 7
button_4 = 8

# handle the button event
def buttonEventHandler (pin):
    if   pin == button_1:
        print("TEST : handling button 1 event")
    elif pin == button_2:
        print("TEST : handling button 2 event")
    elif pin == button_3:
        print("TEST : handling button 3 event")
    elif pin == button_4:
        print("TEST : handling button 4 event")
    else:
        print("TEST : unhandled gpio event")

class init(object):
  
    def __init__(self, buttonEventHandler):
        # tell the GPIO module that we want to use 
        # the chip's pin numbering scheme
        GPIO.setmode(GPIO.BOARD)

        # setup buttons as an inputs
        GPIO.setup(button_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(button_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(button_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(button_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # tell the GPIO library to look out for an 
        # event on button's pins and deal with it by calling 
        # the buttonEventHandler function
        GPIO.add_event_detect  (button_1,GPIO.FALLING, bouncetime=500)
        GPIO.add_event_callback(button_1,buttonEventHandler)
        GPIO.add_event_detect  (button_2,GPIO.FALLING, bouncetime=500)
        GPIO.add_event_callback(button_2,buttonEventHandler)
        GPIO.add_event_detect  (button_3,GPIO.FALLING, bouncetime=500)
        GPIO.add_event_callback(button_3,buttonEventHandler)
        GPIO.add_event_detect  (button_4,GPIO.FALLING, bouncetime=500)
        GPIO.add_event_callback(button_4,buttonEventHandler)

    def close(self):
        GPIO.cleanup()

if __name__=="__main__":
    gp = init(buttonEventHandler)
    while True:
	test = 1
    gp.close()
