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
        menu:
            "Josephine's Hangout Request":
                call josephineHangoutReq
                jump mapScreen
            "Help Kids":
                call helpKids
                jump mapScreen
    else:
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
        jump mapScreen