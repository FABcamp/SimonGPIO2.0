Writing The Code
================
######This page will guide you through writing the code for your simon game in the Scratch programming environment

_Teachers: Before giving these instructions, make sure you have [covered all the skills necessary!](https://github.com/FABcamp/SimonGPIO2.0/blob/master/Documentation/Topics-to-Cover-Teaching-Scratch.md)_

![finished code](https://raw.githubusercontent.com/cineboxandrew/SimonGPIO2.0/master/Images/Scratch.gif)

Setting Up
----------

When you start up the raspberry pi, you will see a desktop. The raspberry pi uses an operating system called Linux, which is similar to your Windows or Mac computers at home. To open ScratchGPIO, doubleclick on its icon on the desktop. If you open the normal Scratch, you will not be able to interface with your circuit. 

Once you have opened ScratchGPIO, go to file>new to clear the canvas and start a new project.

Beginning the Script
--------------------

First, we must have our script start when we begin the program. From the “control” tab on the upper left, drag into the canvas the first block, which should say “when (flag) clicked”. this will mean the block of code are creating will run as soon as we hit either the little green flag on the upper right, or hit the “enter” key on the keyboard. 

Now we need to set up our variables. in the variables tab, click `add variable` to create a variable called `score`, and another called `time`. In the lower half of this tab, click `add list` and create 2 lists called `CPU_tones` and  `player_tones` in the same way. Bring in 2 `set variable` blocks. change one to the `score` variable, and the other to the `time` variable. Set `score` to `0` and `time` to `1`. We must also reset our list of computer-created tones, so bring down the `delete () of []` block, setting it to **delete all of `CPU_tones`**. Now add a “forever” loop from the control tab. This will run *indefinitely* until we stop our script. Add another `delete` block to **delete all of `Player_tones`** inside the forever loop.

In our project, we also have a variable called `human_player`. This keeps track of when the player is in control of the simon game. first, the game must tell the player what the pattern is, so it is not the human player’s turn right now. add a block to **set `human_player` to `false`**. We should also have the game add numbers to this pattern, which will be between 1 and 4. each number will refer to one button or light on the board. under the variables tab, add a block to **add a value to `CPU_tones`**. In the value slot, drag in the block from the Operators tab to **create a random value** and change the second value to 4, not 10. 

Now the cumputer must play back the list of tones it has generated. This will step through each item in our list of `CPU_tones` and play each one out. Scratch doesnt have a function to do this for us, so we need to write it ourselves. Create a new variable called `index` to keep track of which item in our `CPU_tones` list we are playing. Add a block to **set `index` to 1** and add a block from the control tab to **repeat (value)**. For this value, add a block from variables for `Length of [CPU_tones]` Inside this, we will play the tone. Add a block to **broadcast a value**. for this value, bring in a block for `Item (x) of [CPU_tones]` and add the variable `index` for the item number. Now add a block to **wait 0.1 seconds**, and another to **change `index` by 1. How does this work? What we are saying, is first to run this chunk of code the same number of times as there are lights to turn on. on each of these, we are saying to play item x of the list, so if x is 1, we are broadcasting the first item, if x is 2, we are broadcasting the second item. Then we change x by 1 so the next value is used the next time the chunk of code runs. 

Now the human player must play back the pattern on the buttons. add another block to **set `human_player` to `true`**. For the human to be able to play the pattern, we must have the code detect when buttons are pressed, so we must work on another code block to do that. 

Reading the Button Inputs
-------------------------

Drag in another "When (flag) clicked" block from the control tab. under it, **add a forever loop**, and inside it, **add an if block from the control tab**. This will check if a condition is met. add another if block inside it. These blocks have to check:
  1. *if* it is the players turn to push the buttons 
  2. *if* the button is being pushed. 

From the Operators tab, **drag an "equals" block into each of the hexagonal sockets on the 2 if blocks.** in the first one, drag `human_player` into the first half of the `=` and type “true” into the second half. In the second if, drag a "sensor value" block from the sensing tab, and select `pin26`, the pin for our green button, from its drop down menu. Type “0” into the second half. In our circuit, the buttons are connected to ground, or 0, when they are pressed

Inside these 2 Ifs, add a yellow "broadcast block "from the control tab. in its drop down menu, select `new` and type in “1”. this will tell the red light to turn on later in the script. from the variables tab **add a block to add “1” to `player_tones.`** Under it, from the control tab, add a new block to "wait until <>". right click on the green equals on your bottom if, select duplicate, then drag it into the hexagonal socket on your Wait Until block. change the second value to “1”. this waits for the button to be released before allowing it to trigger again.

Duplicate this block 3 times, and change the pin values, broadcast values, and values to add to player_tones to match the 4 buttons on your board using the following table:

Deciding Wins and Losses
------------------------

|color |number|pin name|
|:-----|:----:|:-------|
|green |1     |pin26   |
|red   |2     |pin19   |
|blue  |3     |pin24   |
|yellow|4     |pin22   |

to let you press the buttons, go back to your first, main block of code and add a block from the control tab to "wait until < >". in it, add an "equals" block, and in each half, add the “length of” block from the variables tab. change them so one is `player_tones` and the other is `CPU_tones`. Order does not matter here. This waits until the player has pressed all the buttons they need to before advanceing in the game


if you start the script now, you should see you should be able to push the buttons, and the `player_tones` list will change as you press them. However, the game doesn't care what buttons you press, so we need to check if the buttons the player pressed (`player_tones`) is the same as the tones the computer created(`CPU_tones`). For this, we need a special kind of *if* called an *if else*. these are also under control. add one, and add another equals block into its hexagon socket. In an if else, the condition given is checked, and then runs the first half of the "E". however, if it is false, it will run the second half of the "E".

In each half of the hexagon socket, add `player_tones` and `CPU_tones`. Order doesn’t matter here. this checks if the list of buttons the player pressed is the same as, or equal to, the list of colors the computer presented them. *If* it is, the player won that round, and our code will lead into the first part of the “E”. *else*, the player lost, it will go to the second half of the “E”, and the game should end. 

If the player won, they should get another point, so add a block from variables to change score by one. We also want the game to go faster, so our time delay `time` should be changed. We can change this to 9/10 of what it was in the last round by adding a few blocks to **set time to (time * 0.9).** The multiplication block is under operators. Feel free to change 0.9 to another number, but if you make it too low (like 0.1), the game will get too fast too quickly. 

Under else, we need to end the game. from the Looks tab, add a block to say “you made a mistake” for 2 seconds. also add a "stop all" block from control. Finally, add a block to wait `1` second from the control tab, to make sure the game doesn't start playing the next pattern until the player is ready. 

Adding Outputs for LEDs
-----------------------

If you play the game now, it may be difficult, because the lights aren't turning on!

we need to add some blocks to turn the lights on! If you look back over our script, we have blocks broadcasting lots of numbers. This is like they are yelling into the air “ONE!” as loud as possible, and another block can listen until they hear that symbol. 

Under control, add a block for "When i receive []". Under this, we will add some more broadcasts to turn the lights on. Another thing our broadcasts can do is control electricity! to do this, we will make more broadcasts, saying things like `allon` or `pin15on` or `pin12off`. these talk to the raspberry pi telling it to change its outputs. Under this, add 2 broadcast blocks, a wait block, and another broadcast block. Duplicate this 3 times and change the broadcasts in the top blocks to numbers 1-4. in the first broadcast, have it say “alloff”, the second say “pin#on” and have the third be “pin#off”. this number should match the broadcast number (which color it is) from this table. You should be done now, enjoy the game!

|number|on message|off message|
|:----:|:--------:|:---------:|
|1     |pin11on   |pin11off   |
|2     |pin15on   |pin15off   |
|3     |pin13on   |pin13off   |
|4     |pin12on   |pin12off   |
