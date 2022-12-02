label clinic:
    hide screen NormingtonCityMap
    hide screen continueNextDay
    scene hospitalExterior
    "The silent hallways echo the beeps and boops of the machines with but the faintest of coughs."
    jump choicesClinic

label choicesClinic:
    if day<6:
        jump mapScreen
    else:
        if josephineApologyDone == False:
            menu:
                "Josephine's Apology":
                    call apology
                "Delivery":
                    call deliveryClinic
                "Nevermind":
                    jump mapScreen
            jump mapScreen
        else:
            menu:
                "Delivery":
                    call deliveryClinic
                "Nevermind":
                    jump mapScreen
            jump mapScreen
    jump mapScreen