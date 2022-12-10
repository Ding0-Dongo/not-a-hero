label hill:
    hide screen NormingtonCityMap
    hide screen continueNextDay
    scene apartments
    "Ellis returns home to his apartment."
    jump choicesHill

label choicesHill:
    if day<2:
        menu:
            "Rest":
                if restedToday == False:
                    $ restedToday = True
                    call rest
                    jump mapScreen
                else:
                    "Ellis has already rested today."
                    jump mapScreen
            "Nevermind":
                jump mapScreen
        jump mapScreen
    else:
        menu:
            "Help Old Lady":
                call helpGranny
            "Volunteer at the Senior Center":
                call volunteerSenior
            "Rest":
                if restedToday == False:
                    $ restedToday = True
                    call rest
                    jump mapScreen
                else:
                    "Ellis has already rested today."
                    jump mapScreen
            "Nevermind":
                jump mapScreen
        jump mapScreen
    jump mapScreen