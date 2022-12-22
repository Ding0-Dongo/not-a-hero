label volunteerShelter:
    if energy < 2:
        "Ellis is too tired to do this right now."
        return
    else:
        if shelterVolunteerDone == True:
            scene apartments with fade
            show deltaNeutral at delta_std:
                xalign 0.2
            show ellisHappy at ellis_std:
                xalign 0.8
            
            "(DELTA and Ellis take the bus to the homeless shelter. There, they hand out meals and care packages.)"
            "(It's a good experience for Ellis.)"

            show blackScreen with fade

            $ energy -= 2
            $ stress += 1
            $ social += 2
        else:
            scene hq with fade
            show deltaNeutral at delta_std:
                xalign 0.2
            show ellisNeutral at ellis_std:
                xalign 0.8
            
            D "Up for some volunteering today, Ellis?"

            hide ellisNeutral
            show ellisHappy at ellis_std:
                xalign 0.8
            
            e "Oh, sure! The library or the senior center?"

            hide deltaNeutral
            show deltaInquire at delta_std:
                xalign 0.2
            
            D "The homeless shelter."

            hide ellisHappy
            show ellisNervous at ellis_std:
                xalign 0.8
            
            e "Ah. That's... that's new."

            hide deltaInquire
            show deltaClosed at delta_std:
                xalign 0.2
            
            D "It's still mostly the same. Soup kitchen, care packages, and the like."

            hide deltaClosed
            show deltaNeutral at delta_std:
                xalign 0.2
            
            D "Do you think you can do it?"
            e "*nods slowly* If... if it's anything like the last few times..."

            menu:
                "Go dad mode":
                    hide deltaNeutral
                    show deltaHappy at delta_std:
                        xalign 0.2

                    D "... proud of you."

                    hide ellisNervous
                    show ellisAsk at ellis_std:
                        xalign 0.8
                    
                    e "Huh?"
                    D "Never mind."

                "Nah, stay professional.":
                    pass
            
            D "Alright, let's get going."

            show blackScreen with fade
            scene apartments with fade

            show deltaNeutral at delta_std:
                xalign 0.2
            show ellisNeutral at ellis_std:
                xalign 0.8
            
            "(DELTA and Ellis take the bus to the homeless shelter. There, they hand out meals and care packages.)"
            "(It's a good experience for Ellis.)"

            $ energy -= 2
            $ stress += 1
            $ social += 2

    return