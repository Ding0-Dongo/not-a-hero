### going to try and figure out the tutorial here.

### this might take a bit while I figure out renpy.

label tutorial:

    scene bg room

    show dummy Neutral

    "Howdy there."

    "If you're seeing this then this is where the tutorial goes."

    show screen StatUI

    "Hopefully you should see some sort of stat UI."

    "Get money!"

    $ money += 5

    show dummy Happy

    ". . ."

    $ energy -= 2

    "Get energy drained."

    show dummy Sad

    "See that?"

    "Gain some social points!"

    show dummy Happy

    $ social += 10
    if social == socialMax:
        call SocialLevelUp

    "Did the level go up?"

    $ stress += 1

    hide screen StatUI

    show screen StatUI with hpunch

    "Now become stressed."

    show dummy Sad

    "Okay: let's max out the stress bar"

    $ stress += 4

    hide screen StatUI

    show screen StatUI with hpunch

    show dummy Angry

    if stress == 5:
        call StressMax

    "Alright, now to try some training."

    show dummy Neutral


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

    show dummy Neutral

    #"Resetting your stats and sending you to day one!"
    "Aaaaaaaaaaand that should be all you need to know to do some good in the world!"

    "And always remember:"

    "{i}Even the darkest night will end and the sun will rise."
    #alternatively, any cool normington association quote will do just nicely here

    hide screen StatUI

    $ strength = 1
    $ stamina = 1
    $ speed = 1
    $ energyMax = 10
    $ social = 0
    $ socialLevel = 1
    $ tempSocialLevel = 0
    $ socialMax = 10

    jump testStart