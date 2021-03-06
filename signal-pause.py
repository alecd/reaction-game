from time import sleep
from random import uniform
import RPi.GPIO as gpio
import signal
import sys

# pin assignments
led = 25
button1 = 26
button2 = 19

# this flag is used in the button handler to ignore premature presses
listening = False

def new_game():
    print("New game!")
    
    # start ignoring button presses
    global listening
    listening = False
    
    # flash the light for random interval
    gpio.output(led, 1)
    sleep(uniform(2, 5))
    gpio.output(led, 0)
    
    # start listening for button presses
    listening = True
    
def button_pressed(channel):
    # ignore premature presses
    global listening
    if not listening:
        print("I'm not listening...")
        return
    
    # stop listening for subsequent presses
    listening = False
    print(f"Channel {channel} wins!")
    sleep(2)
    new_game()

def ctrlc_handler(signo, _frame):
    gpio.cleanup()
    sys.exit()

gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)
gpio.setup(button1, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(button2, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.add_event_detect(button1, gpio.FALLING, callback = button_pressed, bouncetime = 100)
gpio.add_event_detect(button2, gpio.FALLING, callback = button_pressed, bouncetime = 100)

# intercepts the Ctrl+C signal to a method, to allow cleanup
signal.signal(signal.SIGINT, ctrlc_handler)

new_game()
signal.pause()
