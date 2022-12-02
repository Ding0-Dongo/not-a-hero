label downtown:
    hide screen NormingtonCityMap
    hide screen continueNextDay
    scene normingtonDowntown
    "The hustle and bustle of the busy roads and the crowded sidewalks frightens Ellis. Not bueno."
    jump choicesDowntown

label choicesDowntown:
    if day<3:
        jump mapScreen
    elif day==3:
        if deliveryRunDone == False:
            menu:
                "Desmond's Delivery Run":
                    call desmondDeliveryRun
                    jump mapScreen
                "Delivery":
                    call deliveryRun
                    jump mapScreen
                "Nevermind":
                    jump mapScreen
        else:
            menu:
                "Delivery":
                    call deliveryRun
                    jump mapScreen
                "Nevermind":
                    jump mapScreen
    elif day==4:
        if deliveryRunDone == False:
            menu:
                "Desmond's Delivery Run":
                    call desmondDeliveryRun
                    jump mapScreen
                "Delivery":
                    call deliveryRun
                    jump mapScreen
                "Volunteer":
                    call volunteerShelter
                    jump mapScreen
                "Nevermind":
                    jump mapScreen
        else:
            menu:
                "Delivery":
                    call deliveryRun
                    jump mapScreen
                "Volunteer":
                    call volunteerShelter
                    jump mapScreen
                "Nevermind":
                    jump mapScreen
    else:
        if deliveryRunDone == False && pursenapperDone == False:
            menu:
                "Desmond's Delivery Run":
                    call desmondDeliveryRun
                    jump mapScreen
                "Delivery":
                    call deliveryRun
                    jump mapScreen
                "Volunteer":
                    call volunteerShelter
                    jump mapScreen
                "Pursenapper":
                    call Pursenapper
                    jump mapScreen
                "Graffi-No":
                    call graffiNo
                    jump mapScreen
                "Thiefstopper":
                    call thiefStopper
                    jump mapScreen
                "Nevermind":
                    jump mapScreen
        elif deliveryRunDone == True && pursenapperDone == False:
            menu:
                "Delivery":
                    call deliveryRun
                    jump mapScreen
                "Volunteer":
                    call volunteerShelter
                    jump mapScreen
                "Pursenapper":
                    call Pursenapper
                    jump mapScreen
                "Graffi-No":
                    call graffiNo
                    jump mapScreen
                "Thiefstopper":
                    call thiefStopper
                    jump mapScreen
                "Nevermind":
                    jump mapScreen
        elif deliveryRunDone == False && pursenapperDone == True:
            menu:
                "Desmond's Delivery Run":
                    call desmondDeliveryRun
                    jump mapScreen
                "Delivery":
                    call deliveryRun
                    jump mapScreen
                "Volunteer":
                    call volunteerShelter
                    jump mapScreen
                "Graffi-No":
                    call graffiNo
                    jump mapScreen
                "Thiefstopper":
                    call thiefStopper
                    jump mapScreen
                "Nevermind":
                    jump mapScreen
        else:
            menu:
                "Delivery":
                    call deliveryRun
                    jump mapScreen
                "Volunteer":
                    call volunteerShelter
                    jump mapScreen
                "Graffi-No":
                    call graffiNo
                    jump mapScreen
                "Thiefstopper":
                    call thiefStopper
                    jump mapScreen
                "Nevermind":
                    jump mapScreen