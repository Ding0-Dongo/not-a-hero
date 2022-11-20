## Screen with Stats Button
screen NormingtonCityMap:
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 0
        yoffset 0
        idle "images/normingtonMap.png"
        action Jump ("call_mapUI")
        # You may also use the code below depending on your needs.
        # action ShowMenu("mapUI")
        # This was the same code used in the vlog.

# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.
label call_mapUI:
    call screen MapUI

screen MapUI:
    # add "images/normingtonMap.png"

    imagebutton:
        xpos 618
        ypos 570
        idle "images/potato1.png"
        hover "images/potato1.png"
        action Jump("testingMap")

    imagebutton:
        xpos 10
        ypos 10
        idle "images/potato2.png"
        hover "images/potato2.png"
        action Jump("testingMap2")



#Main Menu Powerpoint Slides
image main_menu_animated:
    "images/Untitled_Artwork 7.png"
    linear 1 alpha 1.0
    pause 3.2
    linear 1 alpha 0.0
    "images/Untitled_Artwork 6.png"
    linear 1 alpha 1.0
    pause 3.2
    linear 1 alpha 0.0
    "images/Untitled_Artwork 5.png"
    linear 1 alpha 1.0
    pause 3.2
    linear 1 alpha 0.0
    "images/Untitled_Artwork 4.png"
    linear 1 alpha 1.0
    pause 3.2
    linear 1 alpha 0.0
    "images/Untitled_Artwork 3.png"
    linear 1 alpha 1.0
    pause 3.2
    linear 1 alpha 0.0
    "images/Untitled_Artwork 2.png"
    linear 1 alpha 1.0
    pause 3.2
    linear 1 alpha 0.0
    "images/Untitled_Artwork 1.png"
    linear 1 alpha 1.0
    pause 3.2
    linear 1 alpha 0.0
    "images/Untitled_Artwork.png"
    linear 1 alpha 1.0
    pause 3.2
    linear 1 alpha 0.0
    repeat


# This is for displaying all the stats and bars.
screen StatUI:
    bar:
        value energy
        range energyMax
        xysize(400, 50)
        xalign 0.01
        yalign 0.01

    bar:
        value stress
        range 5
        xysize(400, 50)
        xalign 0.01
        yalign 0.07
        left_bar "#d32d2daa"
        right_bar "#b2b27299"

    text "ENERGY: [energy]/[energyMax]" size 28 xalign 0.03 yalign 0.02
    text "STRESS: [stress]/5" size 28 xalign 0.03 yalign 0.08
    text "STR: [strength]" size 28 xalign 0.025 yalign 0.13
    text "STMN: [stamina]" size 28 xalign 0.1 yalign 0.13
    text "SPD: [speed]" size 28 xalign 0.025 yalign 0.18
    text "Social: [social]/10" size 28 xalign 0.1 yalign 0.18

### The training labels will need to be tweaked when we add a proper training area outside of the tutorial!
# This label is called whenever someone chooses to increase their strength
label TrainStrength:
    if energy - 2 < 0:
        "WARNING: ENERGY SUPPLIES LOW. ACTION CANNOT BE PERFORMED."
    elif strength == 10:
        show blackScreen with fade
        "Wow! Your strength cannot be trained further!"
        hide blackScreen with fade
    else:
        show blackScreen with fade
        "It's weightlifting time!"
        "*Clang, clang*"
        "*Huff, huff*"
        "STRENGTH UP"
        $ strength += 1 + (speed - 1)
        $ energy -= 2
        hide blackScreen with fade
    jump trainingScreen

# This label is called whenever someone chooses to increase their stamina
label TrainStamina:
    if energy - 2 < 0:
        "WARNING: ENERGY SUPPLIES LOW. ACTION CANNOT BE PERFORMED."
    elif stamina == 10:
        show blackScreen with fade
        "Wow! Your stamina cannot be trained further!"
        hide blackScreen with fade
    else:
        show blackScreen with fade
        "It's jumprope time!"
        "*Tap tap tap*"
        "Phew!"
        "STAMINA UP"
        $ stamina += 1 + (speed - 1)
        $ energy -= 2
        $ energyMax += stamina
        hide blackScreen with fade
    jump trainingScreen

# This label is called whenever someone chooses to increase their speed
label TrainSpeed:
    if energy - 4 < 0:
        "WARNING: ENERGY SUPPLIES LOW. ACTION CANNOT BE PERFORMED."
    elif speed == 10:
        show blackScreen with fade
        "Wow! Your stamina cannot be trained further!"
        hide blackScreen with fade
    else:
        show blackScreen with fade
        "It's treadmill time!"
        "*Stomp stomp stomp*"
        "*Pant, pant*"
        "SPEED UP"
        $ speed += 1
        $ energy -= 4
        hide blackScreen with fade
    jump trainingScreen

### Adding a label that should be called when the player reaches the max value of the stress bar
### This should have it displayed that the player is too stressed and return them to the 'default' area, wherever it gets decided that is.
### When days are implemented, this should have the player skip the day they failed on.
label StressMax:
    show blackScreen with fade
    pause(1)
    hide blackScreen with fade
    "ERROR: STRESS LEVELS TOO HIGH"
    show blackScreen with fade
    pause(1)
    "ERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR--"
    ". . ."
    pause(0.75)
    "--Instert Return to Menu--"
    hide blackScreen with fade
