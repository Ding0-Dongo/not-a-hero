label clinicDelivery:
    if energy < 3:
        "Ellis is too tired to do that right now."
        return
    else:
        if commission1Done == True:
            scene hospitalExterior with fade

            show ellisNeutral at ellis_std:
                xalign -0.5
            
            pause(0.1)

            show ellisNeutral at ellis_std:
                linear 0.5 xalign 0.5
            
            "(The commission gives Ellis the responsibility of delivering a package addressed to the local clinic.)"
            "(Ellis rides the bike to the clinic and delivers the package smoothly.)"

            $ energy -= 3
            $ money += 15
            $ social += 1

            return
        else:
            scene plaza with fade

            show ellisNeutral at ellis_std:
                xalign -0.5
            pause(0.1)
            show ellisNeutral at ellis_std:
                linear 0.5 xalign 0.5
            
            "(The commission gives Ellis the responsibility of delivering a package addressed to the local clinic.)"
            e "(Looks like it's one of those packages with insulation... maybe it's got medicine? ... either way, probably important.)"
            "(Ellis carefully places the package in a bike basket and begins riding down to the clinic.)"

            show blackScreen with fade

            scene hospitalExterior with fade
            show ellisNeutral at ellis_std:
                xalign -0.5
            pause(0.1)
            show ellisNeutral at ellis_std:
                linear 0.5 xalign 0.5
            
            "(He gets there without any problem, until he has to actually deliver the package.)"

            hide ellisNeutral
            show ellisShy at ellis_std:
                xalign 0.5
            
            e "(Ah... ha ha. Who do I... who do I give this package to? Do I have to get a signature? Was it prepaid? .... oh boy.)"
            e "*nervously wanders around the clinic*"

            if deliveryRunDone == True:
                hide ellisShy
                show ellisAnnoyed at ellis_std:
                    xalign 0.5
                
                e "OK, come on, Ellis, you've done this before."
            else:
                hide ellisShy
                show ellisSad2 at ellis_std:
                    xalign 0.5
                
                e "OK, come on, Ellis, you can figure this out yourself..."
            
            hide ellisSad2
            hide ellisAnnoyed
            show ellisNeutral at ellis_std:
                xalign 0.5

            "(After a few minutes of brisk walking, he discovers a delivery area behind the clinic.)"

            hide ellisNeutral
            show ellisAnnoyed at ellis_std:
                xalign 0.5
            
            e "(... I wish I'd known that was there before...)"

            hide ellisAnnoyed
            show ellisNeutral at ellis_std:
                xalign 0.5
            
            "(Ellis hands off the package to some workers. Apparently the signing and payment had been done beforehand.)"
            "(Relieved and ever slightly more confident, Ellis rides the bike back to the association, where he receives a $15 reward.)"

            $ energy -= 3
            $ money += 15
            $ social += 1

            return