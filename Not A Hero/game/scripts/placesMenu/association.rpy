label association:
    hide screen NormingtonCityMap
    hide screen continueNextDay
    if day<6:
        call socialize
        jump mapScreen
    else:
        menu:
            "Talk Things Out":
                call talkThingsOut
            "Socialize":
                call socialize
        jump mapScreen