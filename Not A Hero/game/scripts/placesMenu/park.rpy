label park:
    hide screen NormingtonCityMap
    hide screen continueNextDay
    scene normingtonPark
    stop music
    play music ParkMusic
    "The cool spring breeze blows over Ellis as the leaves rustle and grass whistles."
    jump choicesPark

label choicesPark:
    if day<2:
        stop music
        play music MainMusic
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
                    stop music
                    play music MainMusic
                    jump mapScreen
        else:
            menu:
                "Help Kids":
                    call helpKids
                    jump mapScreen
                "Nevermind":
                    stop music
                    play music MainMusic
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
                    if walkedToday == False:
                        $ walkedToday = True
                        call takeWalk
                        stop music
                        play music MainMusic
                        jump mapScreen
                    else:
                        "Ellis already took a walk today."
                        jump mapScreen
                "Nevermind":
                    stop music
                    play music MainMusic
                    jump mapScreen
        else:
            menu:
                "Help Kids":
                    call helpKids
                    jump mapScreen
                "Take a Walk":
                    if walkedToday == False:
                        $ walkedToday = True
                        call takeWalk
                        stop music
                        play music MainMusic
                        jump mapScreen
                    else:
                        "Ellis already took a walk today."
                        jump mapScreen
                "Nevermind":
                    stop music
                    play music MainMusic
                    jump mapScreen
        jump mapScreen