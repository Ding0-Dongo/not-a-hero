label elementary:
    hide screen NormingtonCityMap
    hide screen continueNextDay
    scene normingtonElementary
    "Ellis hears the shrills and fun-filled shrieks of the kids, running and laughing about."
    jump choicesElementary

label choicesElementary:
    if day<5:
        jump mapScreen
    else:
        call mediation
        jump mapScreen