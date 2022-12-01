label downtown:
    scene normingtonDowntown
    "The hustle and bustle of the busy roads and the crowded sidewalks frightens Ellis. Not bueno."
    jump choicesDowntown

label choicesDowntown:
    if day<3:
        return
    elif day==3:
        menu:
            "Desmond's Delivery Run":
                call desmondDeliveryRun
                return
            "Delivery":
                call deliveryRun
                return
    elif day==4:
        menu:
            "Desmond's Delivery Run":
                call desmondDeliveryRun
                return
            "Delivery":
                call deliveryRun
                return
            "Volunteer":
                call volunteerShelter
                return
    else:
        menu:
            "Desmond's Delivery Run":
                call desmondDeliveryRun
                return
            "Delivery":
                call deliveryRun
                return
            "Volunteer":
                call volunteerShelter
                return
            "Pursenapper":
                call Pursenapper
                return
            "Graffi-No":
                call graffiNo
                return
            "Thiefstopper":
                call thiefStopper
                return