label volunteerSenior:
    if energy < 1:
        "Ellis is too tired to do that right now."
    else:
        if seniorVolunteerDone == False:
            show blackScreen with fade
            scene hq with fade

            show deltaWisdom at delta_std:
                xalign 0.2
            show ellisNeutral at ellis_std:
                xalign 0.8

            D "*flips a page on clipboard* Have you ever been to Normington's senior center, Ellis?"
            
            hide ellisNeutral
            show ellisAsk at ellis_std:
                xalign 0.8
            
            e "The senior center? Um... I used to go there to visit my grandma, why?"
            D "Excellent, so it's familiar to you. Because that's where we're going today."
            e "What? What for? Do... do we have to?"
            
            hide ellisAsk
            show ellisNeutral at ellis_std:
                xalign 0.8
            
            hide deltaWisdom
            show deltaNeutral at delta_std:
                xalign 0.2

            D "It won't be anything too difficult, just more volunteering."
            
            hide ellisNeutral
            show ellisNervous at ellis_std:
                xalign 0.8
            
            e "... isn't it kind of weird to go to a senior center if you don't know any seniors there?"
            D "No, why? Plenty of people volunteer at senior centers."
            
            hide deltaNeutral
            show deltaInquire at delta_std:
                xalign 0.2
            
            D "Don't ever be ashamed of doing a good thing, Ellis."
            e "*looks hesitant, but nods*"
            
            hide ellisNervous
            show ellisNeutral at ellis_std:
                xalign 0.8
            
            e "OK. Let's... let's go."

            scene apartments with fade

            show deltaNeutral at delta_std:
                xalign 0.2
            show ellisNeutral at ellis_std:
                xalign 0.8

            "(DELTA and Ellis catch a bus to the senior center.)"
            "(The elderly citizens are much kinder and understanding than Ellis was expecting.)"
            "(He hears some wholesome stories from the grandfathers, politely accepts some candies from the old ladies, and keeps the old folks company.)"
            "After about an hour or so, they say their goodbyes and leave.)"

            scene hq with fade

            show deltaTeasing at delta_std:
                xalign 0.2
            show ellisSad2 at ellis_std:
                xalign 0.8
            
            pause(0.3)

            D "Tired?"

            hide ellisSad2
            show ellisNeutral at ellis_std:
                xalign 0.8

            e "Yeah, but... it wasn't so bad."

            hide ellisNeutral
            show ellisHappy at ellis_std:
                xalign 0.8
            
            e "It was... kind of nice, actually."
            D "*smiles* That's good to hear."
        else:
            scene apartments with fade

            show deltaNeutral at delta_std:
                xalign 0.2
            show ellisHappy at ellis_std:
                xalign 0.8
            
            "(DELTA and Ellis spend an hour hanging out with the senior citizens.)"
            "(They hear some heartwarming stories and have some laughs.)"

        show blackScreen with fade
        "+1 stress +1 social"
        $ stress += 1
        $ social += 1
        $ energy -= 1