# http://raspberrywebserver.com/gpio/using-interrupt-driven-gpio.html
# http://razzpisampler.oreilly.com/ch07.html

import time
import RPi.GPIO as GPIO

# Pinout 
button_1 = 3
button_2 = 5
button_3 = 7
button_4 = 10

led_1 = 31
led_2 = 37
led_3 = 35
led_4 = 33

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
        GPIO.add_event_detect  (button_1,GPIO.FALLING, bouncetime=1000)
        GPIO.add_event_callback(button_1,buttonEventHandler)
        GPIO.add_event_detect  (button_2,GPIO.FALLING, bouncetime=1000)
        GPIO.add_event_callback(button_2,buttonEventHandler)
        GPIO.add_event_detect  (button_3,GPIO.FALLING, bouncetime=1000)
        GPIO.add_event_callback(button_3,buttonEventHandler)
        GPIO.add_event_detect  (button_4,GPIO.FALLING, bouncetime=1000)
        GPIO.add_event_callback(button_4,buttonEventHandler)

        GPIO.setup(led_1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(led_2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(led_3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(led_4, GPIO.OUT, initial=GPIO.LOW)

    def led_garland_down(self):
        GPIO.output(led_1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_1, GPIO.LOW)
        GPIO.output(led_2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_2, GPIO.LOW)
        GPIO.output(led_3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_3, GPIO.LOW)
        GPIO.output(led_4, GPIO.HIGH)
        time.sleep(0.5)

    def led_garland_up(self):
        GPIO.output(led_4, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_4, GPIO.LOW)
        GPIO.output(led_3, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_3, GPIO.LOW)
        GPIO.output(led_2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_2, GPIO.LOW)
        GPIO.output(led_1, GPIO.HIGH)
        time.sleep(0.5)

    def led_swich_state(self, led):
        current_state = GPIO.input(led)

        if current_state == GPIO.LOW: 
            new_state = GPIO.HIGH
        else:
            new_state = GPIO.LOW

        GPIO.output(led, new_state)

        return new_state

    def led_blink(self, led, blink_period, blink_nb):
        cpt = 0
        # print('Blink led', led, blink_nb, 'times')
        while cpt < blink_nb:
            cpt += 1
            self.led_swich_state(led)
            time.sleep(blink_period)

    def clear_and_blink_selection(self, button):
        GPIO.output([led_1,led_2,led_3,led_4], GPIO.LOW)
        if   (button == button_1):
            self.led_blink(led_1, 0.1, 20)
        elif (button == button_2):
            self.led_blink(led_2, 0.1, 20)
        elif (button == button_3):
            self.led_blink(led_3, 0.1, 20)
        elif (button == button_4):
            self.led_blink(led_4, 0.1, 20)
        GPIO.output([led_1,led_2,led_3,led_4], GPIO.LOW)

    def led_process(self):
        GPIO.output([led_1,led_2,led_3,led_4], GPIO.LOW)
        while(True):
            self.led_garland_down()
            self.led_blink(led_4, 0.2, 10)
            self.led_garland_up()
            self.led_blink(led_1, 0.2, 10)

    def led_process_test(self):
        while(True):
            print('Garland down')
            time.sleep(1)
            print('Blink led 4')
            time.sleep(0.5)
            print('Garland up')
            time.sleep(1)
            print('Blink led 1')
            time.sleep(0.5)

    def close(self):
        GPIO.cleanup()

if __name__=="__main__":
    gp = init(buttonEventHandler)
    while True:
	test = 1
    gp.close()
