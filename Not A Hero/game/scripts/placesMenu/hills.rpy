label hill:
    hide screen NormingtonCityMap
    hide screen continueNextDay
    scene normingtonHills
    "The hills call out to Ellis in a warm, soothing breeze; the singular tree atop the hill fluttering and flowing like the undulating waves of a fresh, misty lake."
    jump choicesHill

label choicesHill:
    if day<2:
        menu:
            "Rest":
                call rest
                jump mapScreen
            "Nevermind":
                jump mapScreen
        jump mapScreen
    else:
        menu:
            "Help Old Lady":
                call helpGranny
            "Volunteer at the Senior Center":
                call volunteeringSC
            "Rest":
                call rest
            "Nevermind":
                jump mapScreen
        jump mapScreen
    jump mapScreen