label clinic:
    hide screen NormingtonCityMap
    hide screen continueNextDay
    scene normingtonClinic
    "The silent hallways echo the beeps and boops of the machines with but the faintest of coughs."
    jump choicesClinic

label choicesClinic:
    if day<6:
        jump mapScreen
    else:
        menu:
            "Josephine's Apology":
                call josephineApology
            "Delivery":
                call deliveryClinic
            "Nevermind":
                jump mapScreen
        jump mapScreen
    jump mapScreen