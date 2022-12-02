label park:
    hide screen NormingtonCityMap
    hide screen continueNextDay
    scene normingtonPark
    "The cool spring breeze blows over Ellis as the leaves rustle and grass whistles."
    jump choicesPark

label choicesPark:
    if day<2:
        jump mapScreen
    elif day<5:
        if josephineHangoutDone == False:
            menu:
                "Josephine's Hangout Request":
                    call josephineHangoutReq
                    jump mapScreen
                "Help Kids":
                    call helpKids
                    jump mapScreen
                "Nevermind":
                    jump mapScreen
        else:
            menu:
                "Help Kids":
                    call helpKids
                    jump mapScreen
                "Nevermind":
                    jump mapScreen
    else:
        if josephineHangoutDone == False:
            menu:
                "Josephine's Hangout Request":
                    call josephineHangoutReq
                    jump mapScreen
                "Help Kids":
                    call helpKids
                    jump mapScreen
                "Take a Walk":
                    call takeWalk
                    jump mapScreen
                "Nevermind":
                    jump mapScreen
        else:
            menu:
                "Help Kids":
                    call helpKids
                    jump mapScreen
                "Take a Walk":
                    call takeWalk
                    jump mapScreen
                "Nevermind":
                    jump mapScreen
        jump mapScreen