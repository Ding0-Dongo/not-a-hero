label gym:
    hide screen NormingtonCityMap
    hide screen continueNextDay
    menu:
        "Train Strength":
            call TrainStrength

        "Train Stamina":
            call TrainStamina

        "Train Speed":
            call TrainSpeed

        "End Training (Leave)":
            jump mapScreen