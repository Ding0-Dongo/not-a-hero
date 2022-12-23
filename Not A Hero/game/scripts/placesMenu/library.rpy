label lib:
    hide screen NormingtonCityMap
    hide screen continueNextDay
    scene library with fade
    "As Ellis enters the library, the smells of cedar and academia immediately fills his lungs, taking him back to his middle school days."
    jump choicesLib

label choicesLib:
    if day<3:
        menu:
            "Volunteer at the Library":
                call volunteerLibrary
                jump mapScreen
            "Nevermind":
                jump mapScreen
        jump mapScreen
    else:
        menu:
            "Volunteer at the Library":
                call volunteerLibrary
                jump mapScreen
            "Read a book":
                if readToday == False:
                    $ readToday = True
                    call readBook
                    jump mapScreen
                else:
                    "Ellis has already read a book today."
                    jump mapScreen
            "Nevermind":
                jump mapScreen
        jump mapScreen
    jump mapScreen