label park:
    scene normingtonPark
    "The cool spring breeze blows over Ellis as the leaves rustle and grass whistles."
    jump choicesPark

label choicesPark:
    if day<2:
        return
    elif day<5:
        menu:
            "Josephine's Hangout Request":
                call josephineHangoutReq
                return
            "Help Kids":
                call helpKids
                return
    else:
        menu:
            "Josephine's Hangout Request":
                call josephineHangoutReq
                return
            "Help Kids":
                call helpKids
                return
            "Take a Walk":
                call takeWalk
                return
        return