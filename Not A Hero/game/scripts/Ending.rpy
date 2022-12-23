label theEnding:

    #test code
    # "standing?"
    # menu:
    #     "up":
    #         $ standing = 3
    #     "stay":
    #         "standing did not change"

    # "social?"
    # menu:
    #     "up":
    #         $ social = 3
    #     "stay":
    #         "social did not change"
    #end test code
    
    #to play after 'The Ending' story quest is completed.
    scene blackScreen

    stop music

    "LATER"
    "*beep-beep-beep* *beep-beep-beep*"
    play music endingAudio
    D "PHI?"
    P "DELTA, are you still in maintenance?"
    D "Got out just a half hour ago. Why?"
    P "You didn't hear? The elementary school caught fire."
    D "What?"
    P "It's all under control now; you missed it. Luckily no civilians were hurt too badly."
    P "But our TEAM was on the scene, and some of them, well..."

    P "*quietly* ... I think you should go to the clinic."
    D "..."
    P "Ellis might need you."
    "*click*"
    
    scene hospitalInterior with fade
    show alphaNeutral at alpha_std with dissolve:
        xalign 0.8
    show deltaSad at delta_std:
        xalign -1.8
    pause(0.1)
    show deltaSad at delta_std:
        linear 0.5 xalign 0.2

    "(DELTA walks into the clinic. ALPHA is standing in the lobby.)"
    D "The one day I'm not here..."
    
    hide deltaSad
    show deltaSerious at delta_std:
        xalign 0.2
    D "ALPHA?"
    A "*turns to see him* Oh, DELTA. You sure got here quick. They're in the room down the hall."
    D "*looking around* Is PHI here?"
    A "She's on her way. She had to declare the accident at headquarters first."

    show alphaNeutral at alpha_std:
        linear 0.5 xalign 0.5
    show deltaSerious at delta_std:
        linear 0.5 xalign 1.1
    pause 1.0
    hide deltaSerious
    show deltaSad2 at delta_std:
        xalign 1.1
    pause 0.5
    show deltaSad2 at delta_std:
        linear 0.3 xalign 1.0
    
    "(DELTA walks to the door that ALPHA was talking about, but hesitates. He looks back at ALPHA.)"
    A "What's wrong?"
    D "I... I don't know."
    D "I just... I don't want to go in there, and I don't know why."
    A "..."
    A "Would you go in there if I told you there isn't a corpse in there?"
    
    hide deltaSad2
    show deltaNeutral2 at delta_std:
        xalign 1.0
    show phiNeutral at phi_std:
        xalign -0.8
    
    D "(... is that why I don't want to go in there? Am I afraid to lose another HERO?)"
    P "ALPHA, stop it, you're making him cry."
    
    show phiNeutral at phi_std:
        linear 0.3 xalign 0.0
    
    "(PHI walks in briskly through the sliding doors of the clinic.)"
    D "I'm- I'm not crying..."

    show alphaNeutral at alpha_std:
        linear 0.3 xalign 0.0
    show phiNeutral at phi_std:
        linear 0.3 xalign 0.5
    
    P "*gently* {i}DELTA.{/i} Ellis is fine. He just needs to see you, that's all."
    P "Don't pay any attention to ALPHA."
    A "I didn't mean it like that."
    P "Whatever you say, ALPHA."
    P "*nods at DELTA* We'll wait out here. Do what you do best, DELTA."

    hide deltaNeutral2
    show deltaSad at delta_std:
        xalign 1.0
    
    pause(0.3)

    D "... thank you..."

    show blackScreen with fade
    pause(0.1)
    scene hospitalRoom with fade
    
    show deltaNeutral at delta_std:
        xalign -0.8
    show ellisNeutral at ellis_std with dissolve:
        xalign 1.0
    show joNeutral at jo_std with dissolve:
        xalign 0.5

    pause(0.3)
    show deltaNeutral at delta_std:
        linear 0.3 xalign 0.0

    "(It's not nearly as bad as the tension made it out to be - Josephine is sitting on a chair in the room. Ellis and Desmond are both in hospital beds.)"
    "(Desmond appears to be asleep, a heart monitor hooked up nearby beeping at interval.)"
    "(Ellis is awake, however, and looks up as DELTA walks in.)"

    hide ellisNeutral
    show ellisSad at ellis_std:
        xalign 1.0

    e "..."
    e "DELTA?"

    hide deltaNeutral
    show deltaSad2 at delta_std:
        xalign 0.0

    D "(... what do I even say?... am I shaking?)"
    D "No... no bad injuries, I hope?"
    "(Ellis doesn't respond for a moment.)"
    j "I'll... I'll be outside."

    show joNeutral at jo_std:
        linear 0.3 xalign -0.8
    show deltaSad2 at delta_std:
        linear 0.3 xalign 0.2
    show ellisSad at ellis_std:
        linear 0.3 xalign 0.8
    
    "(Josephine leaves the room.)"
    
    hide joNeutral

    D "*takes a deep breath* Sorry I wasn't there."
    e "No, it's OK. No one could have known."

    hide ellisSad
    show ellisNeutral at ellis_std:
        xalign 0.8
    
    e "And I'm OK, thankfully."
    
    hide ellisNeutral
    show ellisSad at ellis_std:
        xalign 0.8
    
    e "*looks over at the other bed* But Desmond..."
    e "I think I heard the nurses saying he'll be in a wheelchair for a while."

    D "..."
    D "(I can't believe this is happening.)"
    
    hide ellisSad
    show ellisNeutral at ellis_std:
        xalign 0.8
    
    e "DELTA, do you want to... sit down, maybe? *gestures at the chair by the bed*"
    
    hide deltaSad2
    show deltaHappy at delta_std:
        xalign 0.2
    
    D "*smiles a bit* You're the one in a hospital bed, and you're worried about me?"
    e "*nods*"
    "(DELTA sits down.)"

    hide ellisNeutral
    show ellisHappy at ellis_std:
        xalign 0.8
    
    e "*shrugs awkwardly* I guess it's just my nature."
    
    hide ellisHappy
    show ellisNeutral at ellis_std:
        xalign 0.8

    hide deltaHappy
    show deltaNeutral at delta_std:
        xalign 0.2
    
    "(They're both quiet for a moment.)"
    
    hide deltaNeutral
    show deltaInquire at delta_std:
        xalign 0.2
    
    D "I haven't forgotten the terms of our agreement, by the way."
    e "*nods* I was trying to think of a good way to bring that up..."
    D "*clears throat*"

    hide deltaInquire
    show deltaWisdom at delta_std:
        xalign 0.2
    
    if standing < 3:
        D "To be honest, you haven't done all that much as a HERO so far."
        D "But there's always room for improvement, so don't be too hard on yourself."
        e "*nods*"
    else:
        D "For your first week, you've been pretty active."
        
        hide deltaWisdom
        show deltaTeasing at delta_std:
            xalign 0.2
        D "Just about everyone in Normington City knows your name, I'd wager."
        
        hide ellisNeutral
        show ellisHappy at ellis_std:
            xalign 0.8
        e "*laughs* Come on, you're exaggerating..."

    hide ellisNeutral
    hide ellisHappy
    hide deltaTeasing
    hide deltaWisdom
    show ellisNeutral at ellis_std:
        xalign 0.8
    show deltaNeutral at delta_std:
        xalign 0.2

    if social > 2:
        e "I guess it's not that bad, after all."
        e "I really thought being introverted would... I don't know, keep me from helping a community, but..."
        
        hide ellisNeutral
        show ellisHappy at ellis_std:
            xalign 0.8
        
        e "*smiles* I guess there's other things I can do."
        
        hide deltaNeutral
        show deltaTeasing at delta_std:
            xalign 0.2
        
        D "You're already thinking about doing more?"
        
        hide ellisHappy
        show ellisAsk at ellis_std:
            xalign 0.8

        e "Oh?... I guess I am."
        
        hide ellisAsk
        show ellisHappy at ellis_std:
            xalign 0.8

        e "I don't mind doing more HEROwork, really..."
        e "*brightly* Josephine and I already agreed to do the TEAM commission at the cultural fair with Desmond!"
        
        hide deltaTeasing
        show deltaNeutral at delta_std:
            xalign 0.2
        
        D "*frowns* Doesn't that end tomorrow?"

        hide ellisHappy
        show ellisNeutral at ellis_std:
            xalign 0.8

        e "Yeah, but we're getting discharged later today."
        e "Why, do we look that bad? *looks over at Desmond*"

        hide deltaNeutral
        show deltaInquire at delta_std:
            xalign 0.2

        D "... decline to answer."

        hide ellisNeutral
        show ellisHappy at ellis_std:
            xalign 0.8

        e "*laughs* Will you and the other mentors come with us?"
        
        hide deltaInquire
        show deltaThinking at delta_std:
            xalign 0.2
        
        D "Huh? You want us to?"
        
        hide ellisHappy
        show ellisNeutral at ellis_std:
            xalign 0.8

        e "Well, it's kind of a big event, so we could have some fun, right?"
        e "And... after we do the commission, Desmond will pretty much be a full-fledged hero."
        
        hide ellisNeutral
        show ellisHappy at ellis_std:
            xalign 0.8
        
        e "So it'll be a big event for us, too!"
        
        hide deltaThinking
        show deltaHappy at delta_std:
            xalign 0.2
        
        D "... yeah, I guess you're right." 
        D "(He looks so excited. Is this the same Ellis I met a week ago?)"

        D "I'll see if we have time, then."
        show blackScreen with fade
    else: 
        e "I'm still not sure that being a HERO is for me, though."
        
        hide ellisNeutral
        show ellisNervous at ellis_std:
            xalign 0.8
        
        e "It's nice, and all, and it's been a good week, but... I think it's too much."
        
        hide deltaNeutral
        show deltaClosed at delta_std:
            xalign 0.2

        D "Right. I won't make you keep being a HERO."
        e "*nods* ..."

        hide ellisNervous
        show ellisHappy at ellis_std:
            xalign 0.8

        e "Thank you, DELTA."

        hide deltaClosed
        show deltaInquire at delta_std:
            xalign 0.2

        D "For what?"

        hide ellisHappy
        show ellisNervous at ellis_std:
            xalign 0.8
        
        e "Um... well... for being my mentor, I guess? And you never pushed me into doing something I didn't want to do."
        
        hide ellisNervous
        show ellisSad at ellis_std:
            xalign 0.8
        
        e "I've had a few friends that made me come along with them to events that really burned me out."
        e "... I guess that's a reason I've been trying to keep to myself."

        hide ellisSad
        show ellisHappy at ellis_std:
            xalign 0.8

        e "But you helped me get around again. *smiles* So... thank you."
        D "..."
        
        hide deltaInquire
        show deltaTeasing at delta_std:
            xalign 0.2

        D "It was no problem, really."
        show blackScreen with fade