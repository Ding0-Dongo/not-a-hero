# requires josephine's apology to be completed first!

label talkThingsOut:
    # black screen (i don't know how to do this AAA)
    show blackScreen
    "(After a lot of deliberation, Ellis makes up his mind to go talk to Desmond.)"
    "(It takes him a while, but after a bit of nervously asking around, he finds where Desmond is.)"
    "(Seems like Desmond has been pretty busy all of yesterday and today... but he agreed to meet in the park for a while.)"
    # scene park
    scene park with fade # totally a park

    show ellisNeutral at ellis_std:
        xalign -1.5
    show ellisNeutral at ellis_std:
        linear 0.3 xalign 0.5

    "(Ellis gets there first. He nervously waits in the park by the fountain.)"
    "(A couple other people are walking around in the park too, passing him by.)"
    
    hide ellisNeutral
    show ellisNervous at ellis_std:
        xalign 0.5
    
    e "(... I kinda wish I wasn't just standing around here by myself. It feels so awkward...)"
    
    show ellisNervous at ellis_std:
        linear 0.3 xalign 0.8
    
    show desNeutral at ellis_std:
        xalign -0.5
    show desNeutral at ellis_std:
        linear 0.3 xalign 0.2

    d "Ellis, there you are. You wanted to talk about something?"

    hide ellisNervous
    show ellisSurprised at ellis_std:
        xalign 0.8

    e "*quickly turns around* Oh-! Desmond, yeah, I... I did."

    hide ellisSurprised
    show ellisNeutral at ellis_std:
        xalign 0.8

    "(He notices Desmond looks more tired than usual.)"
    e "Um... you alright?"
    d "Huh?"

    hide ellisNeutral
    show ellisAsk at ellis_std:
        xalign 0.8
    
    e "It's just... you look like you didn't sleep well?"
    
    hide desNeutral
    show desDrowsy at ellis_std:
        xalign 0.2
    
    d "*waves a hand dismissively* Ellis, I'm busy. If you want to talk to me, make it quick."
    
    hide ellisAsk
    show ellisNervous at ellis_std:
        xalign 0.8

    e "Right... sorry. I just... wanted to talk about yesterday. At... at the café."
    d "*brow furrows* ...what about it?"
    "(Before Ellis can speak, Desmond continues.)"
    d "It's fine if you don't want to do the commission. Josephine already talked to me about it. We won't make you join us."
    
    hide ellisNervous
    show ellisSad2 at ellis_std:
        xalign 0.8

    hide desDrowsy
    show desNeutral at ellis_std:
        xalign 0.2
    
    e "No, I- please, let me explain. I just... I panicked yesterday. I should have... should have talked to you guys instead of just running away."
    d "Well, you're talking to us now. Water under the bridge."
    
    hide ellisSad2
    show ellisScarfNeutral at ellis_std:
        xalign 0.8
    
    e "I want to join you guys, really, but... I'm just not ready yet. Maybe- maybe another week."
    
    hide desNeutral
    show desDrowsy at ellis_std:
        xalign 0.2
    
    d "*folds his arms* It's only one week, but I guess we could always do a different one next month."
    
    hide ellisScarfNeutral
    show ellisSad2 at ellis_std:
        xalign 0.8

    e "Oh, I... I'm sorry... (I'm going to delay his initiation as a full-fledged hero...)"
    
    hide ellisSad2
    show ellisCringe at ellis_std:
        xalign 0.8

    e "(... I feel terrible. I might be sick.)"
    d "(nonchalant) It's whatever. *shrugs*"

    hide desDrowsy
    show desNeutral at ellis_std:
        xalign 0.2
    
    d "Was that all we had to talk about? If we're done here, I have to get back to my commissions."
    
    show desNeutral at ellis_std:
        linear 0.3 xalign -0.1

    "(Ellis can only manage a nod in response. Desmond turns to leave.)"
    
    hide ellisCringe
    show ellisNeutral at ellis_std:
        xalign 0.8
    
    e "Desmond, you... you really throw yourself into your work when you're stressed, huh...?"
    d "..."
    d "I'll see you later, Ellis."
    
    show desNeutral at ellis_std:
        linear 0.3 xalign -0.8

    show ellisNeutral at ellis_std:
        linear 0.3 xalign 0.5

    "(Desmond leaves.)"

    hide desNeutral
    
    hide ellisNeutral
    show ellisSad at ellis_std:
        xalign 0.5
    
    e "(I thought talking things out would make me feel better... so why do I feel so awful?)"

    show blackScreen with fade
    "(Ellis was stressed out by the encounter. +2 stress)"
    $ stress += 2
