label dayZero:

    #Day 0 (Prologue)

    "Normington City 09:00 AM"
    scene plaza with fade
    show deltaNeutral at delta_std with dissolve:
        xalign 0.5
    
    pause(0.5)

    hide deltaNeutral
    show deltaInquire at delta_std:
        xalign 0.5
    
    D "Well, looks like this should be the place."
    
    hide deltaInquire
    show deltaNeutral at delta_std:
        xalign 0.5
    
    D "(My name is DELTA. I am an android working for the Normington Association of Heroes. My job is to mentor and train new heroes.)"
    D "(Today's the first day of my new assignment. I'm supposed to meet him today. PHI told me his name is Ellis. Supposedly, he lives in an apartment in the city.)"
    D "(Well, no time to waste.)"

    scene apartments with fade
    "Normington Hills 09:30 AM"

    show deltaNeutral at delta_std:
        xalign 0.5

    D "(Looks like I'm right on time. Good.)"
    D "*knocks on the door*"
    
    pause (1.0)

    "(shuffling is heard) "
    D "(...)"
    D "(He sure is taking a while in there.)"
    "(Door opens)"

    show deltaNeutral at delta_std:
        linear 0.3 xalign 0.2
    show ellisNeutral at ellis_std with dissolve:
        xalign 0.8

    e "... um, hello? Can- can I help you?"
    D "(Huh. He's... different than what I expected.)"
    
    hide deltaNeutral
    show deltaInquire at delta_std:
        xalign 0.2

    D "My name is DELTA, I'm from the local hero association. I'm looking for Ellis. Are you him?"

    hide ellisNeutral
    show ellisHesitant at ellis_std:
        xalign 0.8

    e "Ellis? Yeah, that's me, but..."

    hide deltaInquire
    show deltaNeutral at delta_std:
        xalign 0.2

    D "Great, are you ready to go? I have to show you the headquarters before we can get started."

    hide ellisHesitant
    show ellisNervous at ellis_std:
        xalign 0.8

    e "Started? Get started with what? I... I think there's been some confu-"
    D "Started with your HERO mentoring. If you don't have any other questions..."

    hide ellisNervous
    show ellisSad2 at ellis_std:
        xalign 0.8

    e "No, no, you don't- you don't understand. I used to have a roommate, and um... his name was also Ellis."
    D "..."

    hide ellisSad2
    show ellisSad at ellis_std:
        xalign 0.8

    e "So I... I think he might've been the Ellis you were looking for."
    e "Sorry..."

    hide deltaNeutral
    show deltaClosed at delta_std:
        xalign 0.2

    D "(I'm beginning to wish PHI gave me a last name.)"
    D "What makes you think that?"
    e "Um- well, you're with the heroes' association, aren't you? It's just..."

    hide ellisSad
    show ellisNervous at ellis_std:
        xalign 0.8
    
    e "Hero work? I... I don't think I'm really cut out to be a hero... that would've all been Ellis- I mean, the other Ellis."
    D "Unless you've committed some sort of crime, I'm afraid I don't see the issue."
    e "It's... it's just..."

    hide deltaClosed
    show deltaNeutral at delta_std:
        xalign 0.2
    hide ellisNervous
    show ellisSurprised at ellis_std with hpunch: 
        xalign 0.8

    e "I'm an introvert! I'm not a hero!"
    #hide text box and flash title screen
    window hide
    #ok so how this' gonna go down is that we flash the title screen, then present the option to the player of whether
    #or not they want to see the tutorial
    #if they don't, we immediately yeet them into day 1
    show titleScreen with fade
    with Pause(3)
    show blackScreen with fade
    #hide screen titleScreenFlash

    menu:
        "Begrudgingly play the Normington Association of Hero's Training Tape":
            #it'd be cool if we added like a vhs sound effect here
            jump tutorial
        "Chuck that in the trash":
            jump meetTheTeam