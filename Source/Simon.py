from gpiozero import LED, Button
from signal import pause
import random
import time

greenLED = LED(17)  #0
redLED = LED(22)    #1
yellowLED = LED(18) #2
blueLED = LED(27)   #3

LEDs = [greenLED, redLED, yellowLED, blueLED]

greenButton = Button(7)
redButton = Button(10)
yellowButton = Button(25)
blueButton = Button(8)
