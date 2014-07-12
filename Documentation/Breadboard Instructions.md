Assembling Your Breadboard
==========================
######This document will guide you through the process of assembling the breadboard you will use to prototype SimonGPIO2.0. 

![Welcome To Your Doom!](https://raw.githubusercontent.com/FabCamp/SimonGPIO2.0/master/Images/BreadBoard%20Full.png)

Placing the Components
----------------------

Take your 4 buttons, Green, Red, Blue, and Yellow, and place them on the left 2/3 of the breadboard. One the right side, place your breakout board (the blue or black circuit board in your Raspberry Pi kit) with the notched side up. Don't worry if the text is upside-down. 

Now take your LEDs. Place them to the right of your buttons on the breadboard, with the shorter leg, or ground, on the left. This is very important, as LEDs will only work with the current going in one direction, and will block electricity from going in the other direction. Now these LEDs need to be connected to ground, but need a current limiting resistor to keep them from blowing. Take your four 330Ω resistors from your kit, and bend both sides to be at right angles. Use your wire cutters to cut the legs halfway down from the body of the resistor. Use these to connect the ground pins of your LEDs with the ground power rail above. Remember, anything in the same vertical column on one side of the breadboard will be connected, so do not attempt to place the leg of the resistor in the same hole as the LED! Your breadboard should now look like the one below.

![Breadboard conponents only](https://raw.githubusercontent.com/FabCamp/SimonGPIO2.0/master/Images/BreadBoard%20No-Wires.png)

Connecting Components to Ground
-------------------------------

Take out one short jumper cable of each color: Red, Green, Blue, and Yellow. Use these to connect the upper left leg of each button with the Ground rail above. Now we have connected all the buttons to the ground rail, but we still need to connect the ground rail to the ground from our Raspberry Pis. Run a shor black jumper from any of the pins on the breakout board labeled "GND" to the upper ground rail. Your breadboard should look like the one below

![Ground wires only](https://raw.githubusercontent.com/FabCamp/SimonGPIO2.0/master/Images/BreadBoard%20GND-Wires.png)
