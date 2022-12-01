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
    #(black screen)
    "*beep-beep-beep* *beep-beep-beep*"
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
    #scene: clinic (interior)
    "(DELTA walks into the clinic. ALPHA is standing in the lobby.)"
    D "The one day I'm not here... ALPHA?"
    A "*turns to see him* Oh, DELTA. You sure got here quick. They're in the room down the hall."
    D "*looking around* Is PHI here?"
    A "She's on her way. She had to declare the accident at headquarters first."
    "(DELTA walks to the door that ALPHA was talking about, but hesitates. He looks back at ALPHA.)"

    A "What's wrong?"
    D "I... I don't know."
    D "I just... I don't want to go in there, and I don't know why."
    A "..."
    A "Would you go in there if I told you there isn't a corpse in there?"
    D "(... is that why I don't want to go in there? Am I afraid to lose another HERO?)"
    P "ALPHA, stop it, you're making him cry."
    "(PHI walks in briskly through the sliding doors of the clinic.)"
    D "I'm- I'm not crying..."
    P "*gently* {i}DELTA.{/i} Ellis is fine. He just needs to see you, that's all."
    P "Don't pay any attention to ALPHA."

    A "I didn't mean it like that."
    P "Whatever you say, ALPHA."
    P "*nods at DELTA* We'll wait out here. Do what you do best, DELTA."
    D "... thank you..."
    #(fade to black)
    #scene: hospital room
    #(fade in)
    "(It's not nearly as bad as the tension made it out to be - Josephine is sitting on a chair in the room. Ellis and Desmond are both in hospital beds.)"
    "(Desmond appears to be asleep, a heart monitor hooked up nearby beeping at interval.)"
    "(Ellis is awake, however, and looks up as DELTA walks in.)"

    e "DELTA?"
    D "(... what do I even say?... am I shaking?)"
    D "No... no bad injuries, I hope?"
    "(Ellis doesn't respond for a moment.)"
    j "I'll be outside."
    "(Josephine leaves the room.)"
    D "*takes a deep breath* Sorry I wasn't there."
    e "No, it's OK. No one could have known."
    e "And I'm OK, thankfully. *looks over at the other bed* But Desmond..."
    e "I think I heard the nurses saying he'll be in a wheelchair for a while."

    D "..."
    D "(I can't believe this is happening.)"
    e "DELTA, do you want to... sit down, maybe? *gestures at the chair by the bed*"
    e "*smiles a bit* You're the one in a hospital bed, and you're worried about me?"
    "(DELTA sits down.)"
    e "*shrugs awkwardly* I guess it's just my nature."
    "(They're both quiet for a moment.)"
    D "I haven't forgotten the terms of our agreement, by the way."
    e "*nods* I was trying to think of a good way to bring that up..."
    D "*clears throat*"

    if standing < 3:
        D "To be honest, you haven't done all that much as a HERO so far."
        D "But there's always room for improvement, so don't be too hard on yourself."
        e "*nods*"
    else:
        D "For your first week, you've been pretty active."
        D "Just about everyone in Normington City knows your name, I'd wager."
        e "*laughs* Come on, you're exaggerating..."

    if social > 2:
        e "I guess it's not that bad, after all."
        e "I really thought being introverted would... I don't know, keep me from helping a community, but..."
        e "*smiles* I guess there's other things I can do."
        D "You're already thinking about doing more?"
        e "Oh?... I guess I am. I don't mind doing more HEROwork, really..."
        e "*brightly* Josephine and I already agreed to do the TEAM commission at the cultural fair with Desmond!"
        D "*frowns* Doesn't that end tomorrow?"
        e "Yeah, but we're getting discharged later today."

        e "Why, do we look that bad? *looks over at Desmond*"
        D "*coughs* Decline to answer."
        e "*laughs* Will you and the other mentors come with us?"
        D "Huh? You want us to?"
        e "Well, it's kind of a big event, so we could have some fun, right?"
        e "And... after we do the commission, Desmond will pretty much be a full-fledged hero."
        e "So it'll be a big event for us, too!"
        D "... yeah, I guess you're right. (He looks so excited. Is this the same Ellis I met a week ago?)"

        D "I'll see if we have time, then."
        #(fade to black)
    else: 
        e "I'm still not sure that being a HERO is for me, though."
        e "It's nice, and all, and it's been a good week, but... I think it's too much."
        D "Right. I won't make you keep being a HERO."
        e "*nods* Thank you, DELTA."
        D "For what?"
        e "Um... well... for being there, I guess? And you never pushed me into doing something I didn't want to do."
        e "I've had a few friends that made me come along with them to events that really burned me out."
        e "... I guess that's a reason I've been trying to keep to myself."

        e "But you helped me get around again. *smiles* So... thank you."
        D "... it was no problem, really."
        #(fade to black)