label dayZero:

    #Day 0 (Prologue)
    #scene city

    "Normington City 09:00 AM"
    D "Well, looks like this should be the place."
    D "(My name is DELTA. I am an android working for the Normington Association of Heroes. My job is to mentor and train new heroes.)"
    D "(Today's the first day of my new assignment. I'm supposed to meet him today. PHI told me his name is Ellis. Supposedly, he lives in an apartment in the city.)"
    D "Well, no time to waste."

    # Scene: Apartment
    "Normington Hills 09:30 AM"
    D"(Looks like I'm right on time. Good.)"
    "*knocks on the door*"
    "..." #find out how to auto delay this
    "(shuffling is heard) "
    D "(...)"
    D "(He sure is taking a while in there.)"
    "*opens the door*"

    show ellis Neutral with fade
    e "... um, hello? Can- can I help you?"
    D "(Huh. He's... different than what I expected.)"
    D "My name is DELTA, I'm from the local hero association. I'm looking for Ellis. Are you him?"
    e "Ellis? Yeah, that's me, but..."
    D "Great, are you ready to go? I have to show you the headquarters before we can get started."
    e "Started? Get started with what? I... I think there's been some confu-"
    D "Started with your HERO mentoring. If you don't have any other questions..."

    e "No, no, you don't- you don't understand. I used to have a roommate, and um... his name was also Ellis."
    D "..."
    e "So I... I think he might've been the Ellis you were looking for."
    e "Sorry..."
    D "(I'm beginning to wish PHI gave me a last name.)"
    D "What makes you think that?"
    e "Um- well, you're with the heroes' association, aren't you? It's just..."
    e "Hero work? I... I don't think I'm really cut out to be a hero... that would've all been Ellis- I mean, the other Ellis."

    D "Unless you've committed some sort of crime, I'm afraid I don't see the issue."
    e "It's... it's just..."
    e "I'm an introvert! I'm not a hero!"
    #hide text box and flash title screen
    window hide
    #ok so how this' gonna go down is that we flash the title screen, then present the option to the player of whether
    #or not they want to see the tutorial
    #if they don't, we immediately yeet them into day 1
    show screen titleScreenFlash
    with Pause(3)
    show blackScreen with fade
    hide screen titleScreenFlash

    menu:
        "Begrudgingly play the Normington Association of Hero's Training Tape":
            #it'd be cool if we added like a vhs sound effect here
            jump tutorial
        "Chuck that in the trash":
            jump meetTheTeam