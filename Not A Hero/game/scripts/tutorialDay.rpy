### going to try and figure out the tutorial here.

### this might take a bit while I figure out renpy.

label tutorial:

    scene bg room

    "Howdy there."

    "If you're seeing this then this is where the tutorial goes."

    show screen StatUI

    "Hopefully you should see some sort of stat UI."

    ". . ."

    $ energy -= 2

    "Get energy drained."

    "See that?"

    $ stress += 1

    hide screen StatUI

    show screen StatUI with hpunch

    "Now become stressed."

    "Okay: let's max out the stress bar"

    $ stress += 4

    hide screen StatUI

    show screen StatUI with hpunch

    if stress == 5:
        call StressMax

    "Alright, now to try some training."


label trainingScreen:

menu:
    "Train Strength":
        jump TrainStrength

    "Train Stamina":
        jump TrainStamina

    "Train Speed":
        jump TrainSpeed

    "End Training":
        pass

    
label endTutorial:

    "Alright!"

    "Resetting your stats and sending you to day one!"

    hide screen StatUI

    $ strength = 1
    $ stamina = 1
    $ speed = 1
    $ energyMax = 10

    jump testStart