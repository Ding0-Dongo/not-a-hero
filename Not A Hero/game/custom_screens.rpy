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
<<<<<<< Updated upstream
        xpos 618
        ypos 570
        idle "images/potato1.png"
        hover "images/potato1.png"
        action Jump("testingMap")
=======
        #This will be for volunteering (library)
        xpos 10
        ypos 100
        idle "images/places/NormingtonCityLibrary.png"
        hover "images/places/NormingtonCityLibrary.png"
        action Call("lib")
    imagebutton:
        #delete this before demo just testing day 6 purse snatch quest #######
        xpos 1000
        ypos 100
        idle "images/apurse.jpeg"
        hover "images/apurse.jpeg"
        action Jump ("action_purse")
>>>>>>> Stashed changes

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
        range 10
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

    text "ENERGY: [energy]/10" size 28 xalign 0.03 yalign 0.02
    text "STRESS: [stress]/5" size 28 xalign 0.03 yalign 0.08
    text "STR: [strength]" size 28 xalign 0.025 yalign 0.13
    text "STMN: [stamina]" size 28 xalign 0.1 yalign 0.13
    text "SPD: [speed]" size 28 xalign 0.025 yalign 0.18
    text "Social: [social]/10" size 28 xalign 0.1 yalign 0.18

        