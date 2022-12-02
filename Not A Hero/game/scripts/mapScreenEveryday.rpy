label mapScreen:
    show image "cityMap" with fade
    if day==1:
        if introMapDialogue == True:
            $ introMapDialogue = False
            "This is Normington City."
            "Every day, you will have the option to help out citizens around the city in order to become a true HERO!"
            show screen NormingtonCityMap
            show screen continueNextDay
            "Go now, spread those wings of yours, and become the Ellis the other Ellis could never even hope of becoming!"
            "*** DEVELOPERS' NOTE: don't continue the text on the map (ex: pressing enter), it'll advance the day. Click on the map instead to make the text disappear safely without skipping to the next day."
        else:
            show screen NormingtonCityMap
            show screen continueNextDay
            "--Click anywhere to continue--"
    else:
        show screen NormingtonCityMap
        show screen continueNextDay
        "--Click anywhere to continue--"

label continueToTheNextDay:
    if day<6:
        $ day+= 1;
        $ stress = 0;
        $ energy = 10;
        if day==4:
            hide screen NormingtonCityMap
            hide screen continueNextDay
            call ptStart
            jump mapScreen
        elif day==5:
            hide screen NormingtonCityMap
            hide screen continueNextDay
            call jshrStart
            jump mapScreen
        jump mapScreen
        return
    elif day==6:
        hide screen NormingtonCityMap
        hide screen continueNextDay
        jump theAccident
        return