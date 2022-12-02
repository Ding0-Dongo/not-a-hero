label association:
    hide screen NormingtonCityMap
    hide screen continueNextDay
    if day<6:
        menu:
            "Socialize":
                call socialize
                jump mapScreen
            "Nevermind":
                jump mapScreen
        jump mapScreen
    else:
        if talkThingsOutDone == False:
            menu:
                "Talk Things Out":
                    call talkThingsOut
                    jump mapScreen
                "Socialize":
                    call socialize
                    jump mapScreen
                "Nevermind":
                    jump mapScreen
        else:
            menu:
                "Socialize":
                    call socialize
                    jump mapScreen
                "Nevermind":
                    jump mapScreen
        jump mapScreen