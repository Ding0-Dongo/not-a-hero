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

    "Alright, now to try some training."


    label trainingScreen:

    menu:
        "Train Strength":
            call TrainStrength

        "Train Stamina":
            call TrainStamina

        "Train Speed":
            call TrainSpeed

        "End Training":
            pass
    

    "Alright!"

    "Resetting your stats and sending you to day one!"

    hide screen StatUI

    $ strength = 1
    $ stamina = 1
    $ speed = 1
    $ energyMax = 10

    jump testStart