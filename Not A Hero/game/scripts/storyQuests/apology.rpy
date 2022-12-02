label apology:
    scene hospitalInterior with fade
    show joNeutral at jo_std with dissolve:
        xalign 0.8
    show ellisNeutral at ellis_std:
        xalign -0.8
    pause(0.2)
    show ellisNeutral at ellis_std:
        linear 0.6 xalign 0.2
    
    "(Ellis walks into the lobby of Normington Clinic, where Josephine asked to meet with him.)"
    "(He sees Josephine at one of the volunteer tables, and hesitates. He still gets nervous and upset when he thinks about yesterday.)"
    "(She hasn't noticed him yet. It's not too late to turn back...)"

    menu:
        "Turn back":
            hide ellisNeutral
            show ellisNervous at ellis_std:
                xalign 0.2
            pause(0.1)
            show ellisNervous at ellis_std:
                linear 0.6 xalign -0.8
            "(Ellis shakes his head and quickly turns around, leaving the clinic. He's not ready for this yet.)"

            show blackScreen with fade
            return
        "Go talk to her":
            "(Ellis takes a few deep breaths, shaking off his nerves. He has to do this - no matter how uncomfortable it might be.)"
            "(It's like going to the dentist, he realizes. Better to just get it over with and feel better, than let things get worse.)"
    
    "(He still hesitates a bit, trying to think about what to say before he goes up to Josephine.)"
    "(Josephine notices him before he has much time, though. Her eyes brighten and she waves him over.)"
    j "Ellis! Hey!... *she smiles apologetically*"
    e "*tries to smile back* Hi, Josephine..."
    j "*she pushes back her hair* I'm... I'm really glad you came, Ellis. I'm sorry about yesterday."
    j "Desmond and I just got excited, that's all. We... we won't make you do the TEAM commission with us if you don't want to, of course."
    
    hide ellisNeutral
    show ellisSad at ellis_std:
        xalign 0.2

    e "No, it's... it's fine..."
    j "Ellis, you don't have to pretend. You literally ran out the door yesterday..."

    hide ellisSad
    show ellisSad2 at ellis_std:
        xalign 0.2
    
    e "Ah, right... I... I did do that..."
    j "It's okay to have boundaries, you know. Just... just let us know, okay? I know Desmond and I can be pretty obnoxious sometimes. *she grins*"

    hide ellisSad2
    show ellisSurprised at ellis_std:
        xalign 0.2
    
    e "*protests* No, no! You're not, really."
    j "You're too nice, Ellis... I'm not saying 'grow a spine', but really. Feel free to tell us when you don't feel comfortable with something."
    j "After all, it wouldn't be very TEAM-y of us to make you do something you didn't want to do."
    "(Josephine looks over at one of the hospital staff, who is waving their arm at her.)"
    j "Ah, I'd love to talk more, Ellis, but I {i}am{/i} volunteering here."
    "(She goes back to bagging a small plastic bag with assorted goods.)"
    j "Unless you'd like to join me? We can keep talking, in that case."

    hide ellisSurprised
    show ellisNeutral at ellis_std:
        xalign 0.2

    e "Oh... sure, I guess. I have an hour or two free."
    j "*nods at a desk in the front* Cool! Just check in at the front there and get a sticker."
    
    show ellisNeutral at ellis_std:
        linear 0.3 xalign -0.8
    pause (1.0)
    show ellisNeutral at ellis_std:
        linear 0.3 xalign 0.2
    
    "(Ellis checks in as a volunteer and returns to Josephine's table.)"
    "(Josephine explains what they're doing, and they get to work. It turns out they're bagging up gift bags for an event later in the day.)"
    j "By the way, have you talked to Desmond yet?"
    
    hide ellisNeutral
    show ellisAsk at ellis_std:
        xalign 0.2
    
    e "Huh? No, why?"
    j "Mm... I think you should talk to him too, Ellis."
    
    hide ellisAsk
    show ellisNervous at ellis_std:
        xalign 0.2
    
    e "I... I kind of just talked to you because you asked me to."
    j "I know, but... it might be good practice, right?"
    j "And for your own good..."

    hide ellisNervous
    show ellisSad2 at ellis_std:
        xalign 0.2
    
    e "I don't know..."
    "(Josephine sighs and her hands pause on another bag.)"
    j "If I know Desmond well enough, I know he definitely isn't going to talk about this unless someone talks to him first."
    
    hide ellisSad2
    show ellisStunned at ellis_std:
        xalign 0.2

    "(Ellis holds his breath.)"
    j "So... as a favor, Ellis... will you go talk to him?"

    hide ellisStunned
    show ellisAnnoyed at ellis_std:
        xalign 0.2
    
    e "I was afraid you were going to ask me that..."
    j "I won't make you. But... I really do think it would be good for the two of you."

    hide ellisAnnoyed
    show ellisSad at ellis_std:
        xalign 0.2
    
    e "*sighs* I know, but... I just- I really haven't done this type of... thing... in a while."
    j "(half-joking) Done what? Talk to people?"

    hide ellisSad
    show ellisAnnoyed2 at ellis_std:
        xalign 0.2

    e "*turns red* Josephine!"
    j "*laughs* Sorry, sorry! I know what you mean, Ellis. But I promise it gets easier with practice."
    j "And hey, if you do this for me, I'll owe you one, OK?"
    e "(still uncertain) I don't know..."
    j "Well, forget about it. You don't have to if you don't want to. But... just think about it, alright?"

    hide ellisAnnoyed2
    show ellisNeutral at ellis_std:
        xalign 0.2
    
    e "*nods*"
    j "*smiles* You're brave, Ellis..."

    hide ellisNeutral
    show ellisSad at ellis_std:
        xalign 0.2
    
    e "(.... am I? I don't think so...)"

    show blackScreen with fade

    "Story quest 'Talk Things Out' unlocked."

    $ apologyDone = True