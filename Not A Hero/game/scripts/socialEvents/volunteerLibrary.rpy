label volunteerLibrary:
    if libraryVolunteerDone == False:
        scene hq with fade

        show deltaNeutral at delta_std:
            xalign 0.2
        
        show ellisSurprised at ellis_std:
            xalign 1.5
        show ellisSurprised at ellis_std:
            linear 0.3 xalign 0.8

        e "DELTA! I didn't know library volunteering was herowork!"
        D "You mean HEROwork?"

        hide ellisSurprised
        show ellisAnnoyed2 at ellis_std:
            xalign 0.8
        
        e "... sure."
        
        hide ellisAnnoyed2
        show ellisHappy at ellis_std:
            xalign 0.8
        
        e "Anyways, can we do that today? Can we?"
        D "(He sounds like a little kid asking about an amusement park.)"

        hide deltaNeutral
        show deltaInquire at delta_std:
            xalign 0.2

        D "Yeah, I think we can fit it into our schedule today."
        D "You sound pretty excited for this, Ellis. Any reason? You like books or something?"

        hide deltaInquire
        show deltaNeutral at delta_std:
            xalign 0.2

        hide ellisHappy
        show ellisSurprised at ellis_std with hpunch:
            xalign 0.8

        e "(!!!)"

        hide ellisSurprised
        show ellisNervous at ellis_std:
            xalign 0.8
        
        e "Oh! Haha... um... well..."
        
        hide ellisNervous
        show ellisObjection at ellis_std:
            xalign 0.8
        
        e "I guess that's kind of obvious, huh?"

        hide ellisObjection
        show ellisNeutral at ellis_std:
            xalign 0.8
        
        e "I used to go to the library a lot when I was a kid. I actually still volunteer there from time to time."

        hide deltaNeutral
        show deltaInquire at delta_std:
            xalign 0.2

        menu:
            "Really?":
                D "Really? That's a surprise."
            "That's great.":
                D "That's great. Always good to hear people doing HEROwork on their own."

    else:
        show ellisHappy at ellis_std:
            xalign 0.8
        
        show deltaNeutral at delta_std:
            xalign 0.2

        "(DELTA and Ellis go to the library. They help reshelve and organize some books.)"
        "(+1 stress, +1 social)"
    
    show blackScreen with fade

    $ stress += 1
    $ social += 1