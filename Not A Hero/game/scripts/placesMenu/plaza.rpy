label plaza:
    hide screen NormingtonCityMap
    hide screen continueNextDay
    scene normingtonPlaza
    "Ellis sees some cool boards."
    jump choicesPlaza

label choicesPlaza:
    if day<3:
        jump mapScreen
    elif day<4:
        menu:
            "Fundraising":
                call fundraising
                jump mapScreen
    else:
        menu:
            "Fundraising":
                call fundraising
                jump mapScreen
            "Josephine's First Aid Lesson":
                call josephineFirstAid
                jump mapScreen
            "PSA":
                call psaTeam
                jump mapScreen
        jump mapScreen