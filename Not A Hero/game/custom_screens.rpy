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
        