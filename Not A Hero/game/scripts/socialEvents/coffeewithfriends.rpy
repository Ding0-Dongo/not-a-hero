#image deltaNeutral = Transform("images/Delta/delta neutral.png", zoom=.4)
#image ellisNeutral = Transform("images/Ellis/Tilt.Neutral.png", zoom=.4)
#image ellisHappy = Transform("images/Ellis/Up.Confident.png", zoom=.4)
#image phiNeutral = Transform("images/Phi/phi neutral.png", zoom=.4)

label coffeeWithFriends:
    if (coffeewithfriends_firstime == True):
        stop sound
        # image deltaNeutral = Transform("images/Delta/delta neutral.png", zoom=.4)
        # image ellisNeutral = Transform("images/Ellis/Tilt.Neutral.png", zoom=.4)
        # image ellisHappy = Transform("images/Ellis/Up.Confident.png", zoom=.4)
        # image phiNeutral = Transform("images/Phi/phi neutral.png", zoom=.4)
        #hide screen
        stop music
        play music MainMusic
        scene hq
        show deltaNeutral
        D "Morning, Ellis... hm? What are you doing?"
        hide deltaNeutral
        show deltaNeutral at right
        show ellisNeutral at left
        e "Oh Delta! Um... I was just... trying to see if Desmond and Josephine were free."
        D "Running a TEAM commission?"
        e "No, no, I... I just wanted to see if I could... invite them... for... for coffee... *voice trails off*"
        D "(Initiative, that's promising.) Oh? Interesting."
        D "But how does that relate to why you're looking at the association status board?"
        e "Well, I... I wanted to see if they were free... I didn't want to bother them if they were busy on a commission, you know?"
        D "You didn't want to, say, just ask them?"
        e "No, that's- I- *shakes his head*"
        D "*shrugs* Worst thing they could say is no..."
        e "'No' is pretty bad though... *winces*"
        D "We could always grab coffee if they don't want to."
        e "Can... can androids drink coffee?"
        D "Eh, it doesn't do anything for us. We don't really need to eat, drink, or sleep, really."
        D "Oh, but it never hurts to turn ourselves off and on again every now and then."
        hide ellisNeutral
        show ellisHappy at left
        e "*holds a straight face for a moment, then starts laughing*"
        D "So, HERO, gonna ask your friends out for coffee now?"
        hide ellisHappy
        show ellisNeutral at left
        e "Can you come with me?... Please?"
        D "Sure, but I don't know if you want me to be there with you and your friends"
        e "Oh! Um- well, you don't have to be there if... if you don't want to..."
        D "Eh, work life and personal life should be separate anyways. You go have fun with your friends. I'll find something to do."
        hide ellisNeutral
        show ellisHappy at left
        e "*nods enthusiastically* Th-thanks, DELTA!"
        D "(I get the idea he wouldn't be able to say he didn't want me to come with them...)"
        hide deltaNeutral
        hide ellisHappy
        #show deltaNeutral 
        #show phiNeutral right
        #show phiNeutral midright
        #show desNeutral right
        "(Delta and Ellis find Josephine and Desmond. The two of them seem to be free, and quickly agree to get coffee.)"
        #hide scene
        scene coffeeshop_inside
        stop music
        play music CoffeeShopMusic
        play sound CafeChatterAudio
        "(The three HEROs head to the break room.)"
        show deltaNeutral
        D "*watches the TEAM joking around and having fun, smiles a bit* (Seems like they're hitting it off pretty well.)"
        hide deltaNeutral
        show deltaNeutral at left
        show phiNeutral at right
        P "DELTA, are you a miracle-worker or what?"
        D "*smiles drops, turns to see PHI* Oh. PHI."
        P "*laughs* Aw, well, don't look so happy to see me, DELTA..."
        D "I'm not unhappy to see you. I was just thinking about something."
        P "Mm, yeah, I can tell. You're doing pretty good work with Ellis thought, huh?"
        D "Meh, it's about average."
        P "Humble as always, DELTA... say, do you want to grab coffee with me and ALPHA?"
        D "Not particularly."
        P "Buzzkill."
        D "Isn't ALPHA busy, anyways?"
        P "Aww, alright, you caught me."
        D "*sighs* What are you getting at, PHI?"
        P "Oh, y'know... It's not just Ellis doing some growth amd making some changes, y'know. *jabs DELTA with a knowing look*"
        D "Come on, you know we don't have time for that. We have jobs, duties to fulfill."
        P "*shrugs* File it under 'performance bottlecap'"
        D "It really isn't."
        P "If you say so. Either way, we should leave them to their fun."
        "(The two androids watch their TEAM for a moment longer.)"
        D "Yeah... back to work."


        #image deltaNeutral = Transform("images/Delta/delta neutral.png", zoom=1)
        #image ellisNeutral = Transform("images/Ellis/Tilt.Neutral.png", zoom=1)
        #image ellisHappy = Transform("images/Ellis/Up.Confident.png", zoom=1)
        #image phiNeutral = Transform("images/Phi/phi neutral.png", zoom=1)

        hide deltaNeutral
        hide phiNeutral

        $ coffeewithfriends_firstime = False

        jump NormingtonCoffee

    else:
        stop sound
        "(Ellis and his friends have a nice chat over coffee.)"
        "(Though he's still a bit anxious, he manages to enjoy himself.)"
        $ stress += 1
        $ social += 1
        "Stress increased. Social Increased."


        jump NormingtonCoffee

