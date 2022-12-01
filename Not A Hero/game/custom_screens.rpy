## Screen with Stats Button
screen NormingtonCityMap:
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 0
        yoffset 0
        idle "cityMap"
        action Jump ("call_mapUI")
        # You may also use the code below depending on your needs.
        # action ShowMenu("mapUI")
        # This was the same code used in the vlog.

# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.
label call_mapUI:
    if day==0:
        call screen MapUI0
    elif day==1:
        call screen MapUI1
    elif day==2:
        call screen MapUI2
    elif day==3:
        call screen MapUI3
    elif day==4:
        call screen MapUI4
    elif day==5:
        call screen MapUI5
    elif day==6:
        call screen MapUI6

screen MapUI0:
    # add "images/normingtonMap.png"

    # imagebutton:
    #     xpos 618
    #     ypos 570
    #     idle "images/potato1.png"
    #     hover "images/potato1.png"
    #     action Jump("testingMap")

    # imagebutton:
    #     xpos 10
    #     ypos 10
    #     idle "images/potato2.png"
    #     hover "images/potato2.png"
    #     action Jump("testingMap2")
    imagebutton:
        xpos 618
        ypos 570
        idle "images/potato1.png"
        hover "images/potato1.png"
        action Jump("testingMap")
    imagebutton:
        #This will be for volunteering (library)
        xpos 10
        ypos 100
        idle "mapIcon"
        hover "mapIcon"
        action Call("lib")
        
        
screen MapUI1:
    imagebutton:
        #library
        xpos 1400
        ypos 200
        idle "mapIcon"
        hover "mapIcon2"
        action Call("lib")
    imagebutton:
        #hills
        xpos 1600
        ypos 800
        idle "mapIcon"
        hover "mapIcon2"
        action Call("hill")
    imagebutton:
        #NAHH
        xpos 1300
        ypos 750
        idle "mapIcon"
        hover "mapIcon2"
        action Call("association")
    imagebutton:
        #gym
        xpos 800
        ypos 500
        idle "mapIcon"
        hover "mapIcon2"
        action Call("gym")

screen MapUI2:
    imagebutton:
        #park
        xpos 1000
        ypos 470
        idle "mapIcon"
        hover "mapIcon2"
        action Call("park")
    imagebutton:
        #library
        xpos 1400
        ypos 200
        idle "mapIcon"
        hover "mapIcon2"
        action Call("lib")
    imagebutton:
        #hills
        xpos 1600
        ypos 800
        idle "mapIcon"
        hover "mapIcon2"
        action Call("hill")
    imagebutton:
        #NAHH
        xpos 1300
        ypos 750
        idle "mapIcon"
        hover "mapIcon2"
        action Call("association")
    imagebutton:
        #gym
        xpos 800
        ypos 500
        idle "mapIcon"
        hover "mapIcon2"
        action Call("gym")

screen MapUI3:
    imagebutton:
        #park
        xpos 1000
        ypos 470
        idle "mapIcon"
        hover "mapIcon2"
        action Call("park")
    imagebutton:
        #library
        xpos 1400
        ypos 200
        idle "mapIcon"
        hover "mapIcon2"
        action Call("lib")
    imagebutton:
        #hills
        xpos 1600
        ypos 800
        idle "mapIcon"
        hover "mapIcon2"
        action Call("hill")
    imagebutton:
        #NAHH
        xpos 1300
        ypos 750
        idle "mapIcon"
        hover "mapIcon2"
        action Call("association")
    imagebutton:
        #gym
        xpos 800
        ypos 500
        idle "mapIcon"
        hover "mapIcon2"
        action Call("gym")
    imagebutton:
        #downtown
        xpos 1500
        ypos 600
        idle "mapIcon"
        hover "mapIcon2"
        action Call("downtown")

screen MapUI4:
    imagebutton:
        #park
        xpos 1000
        ypos 470
        idle "mapIcon"
        hover "mapIcon2"
        action Call("park")
    imagebutton:
        #library
        xpos 1400
        ypos 200
        idle "mapIcon"
        hover "mapIcon2"
        action Call("lib")
    imagebutton:
        #hills
        xpos 1600
        ypos 800
        idle "mapIcon"
        hover "mapIcon2"
        action Call("hill")
    imagebutton:
        #NAHH
        xpos 1300
        ypos 750
        idle "mapIcon"
        hover "mapIcon2"
        action Call("association")
    imagebutton:
        #gym
        xpos 800
        ypos 500
        idle "mapIcon"
        hover "mapIcon2"
        action Call("gym")
    imagebutton:
        #downtown
        xpos 1500
        ypos 600
        idle "mapIcon"
        hover "mapIcon2"
        action Call("downtown")
    imagebutton:
        #plaza
        xpos 1600
        ypos 400
        idle "mapIcon"
        hover "mapIcon2"
        action Call("plaza")

screen MapUI5:
    imagebutton:
        #park
        xpos 1000
        ypos 470
        idle "mapIcon"
        hover "mapIcon2"
        action Call("park")
    imagebutton:
        #library
        xpos 1400
        ypos 200
        idle "mapIcon"
        hover "mapIcon2"
        action Call("lib")
    imagebutton:
        #hills
        xpos 1600
        ypos 800
        idle "mapIcon"
        hover "mapIcon2"
        action Call("hill")
    imagebutton:
        #NAHH
        xpos 1300
        ypos 750
        idle "mapIcon"
        hover "mapIcon2"
        action Call("association")
    imagebutton:
        #gym
        xpos 800
        ypos 500
        idle "mapIcon"
        hover "mapIcon2"
        action Call("gym")
    imagebutton:
        #downtown
        xpos 1500
        ypos 600
        idle "mapIcon"
        hover "mapIcon2"
        action Call("downtown")
    imagebutton:
        #plaza
        xpos 1600
        ypos 400
        idle "mapIcon"
        hover "mapIcon2"
        action Call("plaza")
    imagebutton:
        #elementary
        xpos 850
        ypos 100
        idle "mapIcon"
        hover "mapIcon2"
        action Call("elementary")
    imagebutton:
        #coffee
        xpos 400
        ypos 240
        idle "mapIcon"
        hover "mapIcon2"
        action Call("coffee")

screen MapUI6:
    imagebutton:
        #park
        xpos 1000
        ypos 470
        idle "mapIcon"
        hover "mapIcon2"
        action Call("park")
    imagebutton:
        #library
        xpos 1400
        ypos 200
        idle "mapIcon"
        hover "mapIcon2"
        action Call("lib")
    imagebutton:
        #hills
        xpos 1600
        ypos 800
        idle "mapIcon"
        hover "mapIcon2"
        action Call("hill")
    imagebutton:
        #NAHH
        xpos 1300
        ypos 750
        idle "mapIcon"
        hover "mapIcon2"
        action Call("association")
    imagebutton:
        #gym
        xpos 800
        ypos 500
        idle "mapIcon"
        hover "mapIcon2"
        action Call("gym")
    imagebutton:
        #downtown
        xpos 1500
        ypos 600
        idle "mapIcon"
        hover "mapIcon2"
        action Call("downtown")
    imagebutton:
        #plaza
        xpos 1600
        ypos 400
        idle "mapIcon"
        hover "mapIcon2"
        action Call("plaza")
    imagebutton:
        #elementary
        xpos 850
        ypos 100
        idle "mapIcon"
        hover "mapIcon2"
        action Call("elementary")
    imagebutton:
        #coffee
        xpos 400
        ypos 240
        idle "mapIcon"
        hover "mapIcon2"
        action Call("coffee")
    imagebutton:
        #clinic
        xpos 240
        ypos 800
        idle "mapIcon"
        hover "mapIcon2"
        action Call("clinic")


#Main Menu Powerpoint Slides
image main_menu_animated:
    pause 0.3
    linear 1 alpha 0.0
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
    text "Social Level [socialLevel]: [social]/[socialMax]" size 28 xalign 0.1 yalign 0.18
    text "$[money]" size 65 xalign 0.98 yalign 0.025 color "#23b84d"

# helo ethan you seem to be good at making these so Imma just plop down my "continue to next day" button here
screen continueNextDay:
    imagebutton:
        xpos 1500
        ypos 1000
        idle "nextDayButton"
        hover "nextDayButton"
        action Call("continueToTheNextDay")
    text "Continue to next day." size 28 xalign 0.95 yalign 0.96 color "#FFFFFF"


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
    return


# Label that gets called when the social bar is filled
label SocialLevelUp:
    $ tempSocialLevel = socialLevel
    $ socialLevel += 1
    "- - Social Level Up! ([tempSocialLevel] --> [socialLevel]) - -"
    $ social = 0
    $ socialMax += 2
    return

#Putting a transform here for a standardized ellis position
transform ellis_std:
    zoom 0.45
    yalign -1.5

label splashscreen:
    scene blackScreen
    with Pause(1)

    show text "Not A Studio Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(2)

    return