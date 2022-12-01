label mapScreen:
    show image "images/normingtonMap.png"
    if day==1:
        "This is Normington City."
        "Every day, you will have the option to help out citizens around the city in order to become a true HERO!"
        show screen NormingtonCityMap
        show screen continueNextDay
        "Go now, spread those wings of yours, and become the Ellis the other Ellis could never even hope of becoming!"
    else:
        ""
        show screen NormingtonCityMap
        show screen continueNextDay

label continueToTheNextDay:
    if day<7:
        $ day+= 1;
        jump mapScreen
        return
    elif day==7:
        hide screen NormingtonCityMap
        hide screen continueNextDay
        jump theAccident
        return