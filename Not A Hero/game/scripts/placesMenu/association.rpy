label association:
    hide screen NormingtonCityMap
    hide screen continueNextDay
    if day<6:
        menu:
            "Socialize":
                call socialize
            "Nevermind":
                jump mapScreen
        jump mapScreen
    else:
        menu:
            "Talk Things Out":
                call talkThingsOut
            "Socialize":
                call socialize
            "Nevermind":
                jump mapScreen
        jump mapScreen