from gpiozero import LED, Button
from time import sleep
from random import uniform
from os import _exit
from signal import pause

led = LED(25)
buttonP1 = Button(19)
buttonP2 = Button(26)

p1Name = input("What is player one's name? ")
p2Name = input("What is player two's name? ")
winnerName = None

led.on()
sleep(uniform(1, 2))
led.off()

def pressed(button):
    if button.pin.number == buttonP1.pin.number:
        winnerName = p1Name
    else:
        winnerName = p2Name
    
    print(f"{winnerName} won the game!")

buttonP1.when_pressed = pressed
buttonP2.when_pressed = pressed