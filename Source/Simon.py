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

playerPattern = list()
computerPattern = list()
pause = 1
score = 0

def pressButton(color):
    playerPattern.append(color)
    LEDs[color].blink(1, 0, 1, True)
  
greenButton.when_pressed = lambda: pressButton(0)
redButton.when_pressed = lambda: pressButton(1)
yellowButton.when_pressed = lambda: pressButton(2)
blueButton.when_pressed = lambda: pressButton(3)

while (True):
    time.sleep(1)
    print("computer's turn")
    
    playerPattern = list()
    computerPattern.append(random.randint(0, 3))
    for color in computerPattern:
        LEDs[color].blink(pause, 0, 1, False)
        time.sleep(0.1)

    time.sleep(1)    
    print("your turn")
          
    while (len(playerPattern) != len(computerPattern)):
        time.sleep(0.1)

    if (playerPattern != computerPattern):
        print("your score is " + str(score))
        break

    score = score + 1 
    pause = pause * 0.9
