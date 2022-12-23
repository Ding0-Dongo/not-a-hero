label deliveryRun:
    if energy < 1:
        "(Ellis doesn't have enough energy to do this story quest right now.)"
    else:
        show plaza
        "Downtown Normington"
        
        show ellisNeutral at ellis_std with fade:
            xalign 0.5

        "(Ellis is walking around the downtown area of Normington City when he happens upon a familiar person.)"
        
        show ellisNeutral at ellis_std:
            linear 0.8 xalign 0.1
        pause(0.8)
        hide ellisNeutral
        show ellisAsk at ellis_std:
            xalign 0.1
        show desNeutral at ellis_std with moveinright:
            xalign 0.8

        e "... Desmond?"

        d "... huh?"

        hide desNeutral
        show desChuckle at ellis_std:
            xalign 0.8

        d "Oh, Ellis, is that you? Didn't recognize you for a second there, sorry. I'm on a commission right now, so I'm busy."
        
        hide ellisAsk
        show ellisNervous at ellis_std:
            xalign 0.1

        e "Oh, um, sorry then. I'll just get out of your way."
        
        hide desChuckle
        show desNeutral at ellis_std:
            xalign 0.8

        d "No, no, it's fine. You know, now might actually be a pretty good time."
        
        hide ellisNervous
        show ellisAsk at ellis_std:
            xalign 0.1

        e "Huh? A good time? For what?"
        d "You haven't done a TEAM commission yet, have you?"
        
        hide ellisAsk
        show ellisSad at ellis_std:
            xalign 0.1
        
        e "*shakes his head*"

        hide desNeutral
        show desChuckle at ellis_std:
            xalign 0.8
        hide ellisSad
        show ellisNeutral at ellis_std:
            xalign 0.1

        d "Right. Never a better time than the present, then."
        
        hide desChuckle
        show desNeutral at ellis_std:
            xalign 0.8
        
        d "TEAM commissions are just commissions you run with your TEAMmates. Maybe not the whole TEAM, but at least one other person."
        d "Got it?"
        
        hide ellisNeutral
        show ellisAsk at ellis_std:
            xalign 0.1

        e "Uh... I think so."
        d "Any questions, then?"

        hide ellisAsk
        show ellisObjection at ellis_std:
            xalign 0.1

        e "Are there any... specific rules for TEAM commissions? Are only some commissions TEAM?"
        
        hide ellisObjection
        show ellisNeutral at ellis_std:
            xalign 0.1

        d "Yeah. I mean, you can't just tag along with someone who's doing a simple thing."
        e "Guess that makes sense..."
        d "If you're not busy, do you feel like helping me out with a few deliveries? It's one of the easier TEAM commissions."

        if stamina < 3:
            hide ellisNeutral
            show ellisNervous at ellis_std:
                xalign 0.1
            e "... um, sorry, I don't think I'm ready for that yet."
            d "Oh? That's a shame. Another day, maybe?"
            
            hide ellisNervous
            show ellisNeutral at ellis_std:
                xalign 0.1

            e "Sure... I'll see you later, Desmond?"

            hide desNeutral
            show desChuckle at ellis_std:
                xalign 0.8

            d "Yup. Seeya."

            show blackScreen with fade

            "(This story quest requires 3 stamina! Train up and try again!)"
        else:
            hide ellisNeutral
            show ellisHappy at ellis_std:
                xalign 0.1

            e "... sure!"
            d "Oh? It's a pretty active commission. Hope you're up for some exercise."
            
            hide ellisHappy
            show ellisNervous at ellis_std:
                xalign 0.1
            
            e "I- I can handle it. (I think...)"
            
            hide desNeutral
            show desChuckle at ellis_std:
                xalign 0.8
            
            d "That's good to hear. Just let me know if you need a break, though."
            
            hide desChuckle
            show desNeutral at ellis_std:
                xalign 0.8
            
            d "Here, take one of the packages."
            e "(He reaches for one of the largest-looking packages.)"
            d "Wait, not that one-!"
            
            hide ellisNervous
            show ellisSurprised at ellis_std:
                xalign 0.1

            e "(!!!)"

            show ellisSurprised at ellis_std with hpunch:
                xalign 0.1
            show blackScreen with fade

            "(Ellis and Desmond spend a good while delivering packages. It's tiring, but rewarding work.)"
            "(For his efforts, Ellis gains $10 from the association, as well as a $5 first-time bonus.)"
            "'Delivery' commission unlocked."

            $ money += 15
            $ energy -= 1