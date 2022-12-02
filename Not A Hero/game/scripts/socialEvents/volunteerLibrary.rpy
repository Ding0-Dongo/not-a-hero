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
        
        hide deltaNeutral
        show deltaHappy at delta_std:
            xalign 0.2
        
        D "You mean HEROwork?"

        hide ellisSurprised
        show ellisAnnoyed2 at ellis_std:
            xalign 0.8
        
        e "... sure."
        
        hide ellisAnnoyed2
        show ellisHappy at ellis_std:
            xalign 0.8
        
        e "Anyways, can we do that today? Can we?"

        hide deltaHappy
        show deltaTeasing at delta_std:
            xalign 0.2
        
        D "(He sounds like a little kid asking about an amusement park.)"
        D "Yeah, I think we can fit it into our schedule today."
        
        hide deltaTeasing
        show deltaWisdom at delta_std:
            xalign 0.2
        
        D "You sound pretty excited about this, Ellis. Any reason? You like books or something?"

        hide deltaInquire
        show deltaHappy at delta_std:
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
        show ellisHappy at ellis_std:
            xalign 0.8
        
        e "I used to go to the library a lot when I was a kid. I actually still volunteer there from time to time."

        menu:
            "Really?":
                D "Really? That's a surprise."
            "That's great.":
                D "That's great. Always good to hear people doing HEROwork on their own."

        hide ellisHappy
        show ellisNervous at ellis_std:
            xalign 0.8
        
        e "*suddenly self-conscious* ... is it? I- I mean, it wasn't hard work or anything."
        e "Just stuff like reshelving books, mostly..."
        
        hide deltaHappy
        show deltaWisdom at delta_std:
            xalign 0.2
        
        D "Any good you can do for your community is HEROwork. Looks like it's in your bones, Ellis."
        
        hide ellisNervous
        show ellisAsk at ellis_std:
            xalign 0.8

        e "What? What's in my bones?"

        hide deltaWisdom
        show deltaHappy at delta_std:
            xalign 0.2
        
        D "Never mind. Let's get to this library of yours, then."
    
        show blackScreen with fade

        "(DELTA and Ellis walk briskly to the local library. There, they get name tags and help out with reshelving and organizing.)"
        "(Though they have to help out some patrons once or twice, it's mostly independent work.) (+1 stress, +1 social)"

        D "(I think I see why he liked volunteering at the library so much.)"


    else:
        scene plaza with fade

        show ellisHappy at ellis_std with dissolve:
            xalign 0.8
        
        show deltaNeutral at delta_std with dissolve:
            xalign 0.2

        "(DELTA and Ellis go to the library. They help reshelve and organize some books.)"
        "(+1 stress, +1 social)"
    
    show blackScreen with fade

    $ stress += 1
    $ social += 1