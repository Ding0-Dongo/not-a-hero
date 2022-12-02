label helpKids:
    if energy < 1:
        "Ellis is too tired to do that right now."
        return
    else:
        if commission4Done:
            scene park with fade
            show ellisHappy at ellis_std:
                xalign -0.8
            pause(0.3)
            show ellisHappy at ellis_std:
                linear 0.6 xalign 0.5
            
            kid1 "Big Brother Ellis is back!!!!"
            kid2 "Let's play let's playyyyy!!"
            kid3 "Friendship ended with Duck. Ellis is my new best friend."
            
            show blackScreen with fade
            "(Ellis earns $5 for helping out the kids.)"

            $ money += 5
            return
        else:
            scene park with fade
            
            show ellisAsk at ellis_std:
                xalign -0.8
            show deltaNeutral at delta_std:
                xalign -0.8
            
            "Normington Park, random time afternoon"
            show joExclaim at jo_std with dissolve:
                xalign 0.8
            show phiNeutral at phi_std with dissolve:
                xalign 1.1 
            
            show ellisAsk at ellis_std:
                linear 0.3 xalign 0.0
            show deltaNeutral at delta_std:
                linear 0.3 xalign 0.4

            j "aaaaAAH! I'm so glad you guys could make it on such short notice!"
            D "What seems to be the issue, HERO Josephine?"
            
            hide joExclaim
            show joNeutral at jo_std:
                xalign 0.8
            
            j "It's just that... we were tasked with watching over these kids but they are insistent on poking the ducks!"
            kid1 "Playing house is lame but mildly annoying the local wildlife is fun!"
            
            hide deltaNeutral
            show deltaAnnoyed at delta_std:
                xalign 0.4
            
            D "... (Not my area of expertise.)"
            P "The kids proposed some ideas but..."
            j "Their ideas are more suited towards you, Ellis!"
            e "Huh? What did they want to do?"
            kid1 "Hi, I'm Johnnathaeign and I wanna fight!"
            kid2 "What's up, I'm Joughseph and I want you to be a tree! For science! Science rules!"
            kid3 "My name is Rose and I wish to race."
            e "Why did they introduce themselves like Pok*mon NPCs...?"
            j "Welp! Choice is all yours, Ellis!"
            
            hide ellisAsk
            show ellisThinking2 at ellis_std:
                xalign 0.0

            "How do I keep these kids from poking the ducks for an hour...?"
            menu:
                "Go with Johnnathaeign's suggestion and play-fight.":
                    e "I... I guess we could play-fight?"
                    D "Eh?"
                    kid1 "Alrighty! Let's go!"
                    "Johnnathaeign Fortnight dances."
                    kid1 "Ok! Ellis, Josephine! You guys are the good guys!"
                    kid2 "DELTA and PHI can be the bad guys!"
                    P "Fitting~"
                    kid3 "Let the fight commence."
                    D "(What is up with these kids?)"
                    j "Well, looks like we gotta play along... I'll deal with DELTA, and you deal with PHI! C'mon, up and at 'em!"
                    "Josephine gets a good aerial backwards air up-smash neutral footsie off on DELTA."
                    
                    show joNeutral at jo_std:
                        linear 0.3 xalign 1.1
                    show deltaAnnoyed at delta_std:
                        linear 0.3 xalign 0.8
                    show phiNeutral at phi_std:
                        linear 0.3 xalign 0.3
                    hide ellisThinking2
                    show ellisSurprised at ellis_std:
                        xalign 0.0

                    pause 0.3

                    hide deltaAnnoyed
                    show deltaSerious at delta_std with hpunch:
                        xalign 0.8

                    D "Ah, we should've done something else for the day..."
                    "(PHI and Ellis square off together.)"
                    P "Fuhahahaha! Think you can defeat me?!"
                    
                    hide ellisSurprised
                    show ellisCry at ellis_std:
                        xalign 0.0
                    
                    e "U-uh, not really?!"
                    P "Come at me with all you've got!"
                    if strength < 2:
                        hide ellisCry
                        show ellisCringe at ellis_std:
                            xalign 0.0
                        
                        call hitPhi
                        
                        "Ellis feebly punches PHI's palm. PHI seems not to notice."
                        P "Psst, Ellis c'mon, gimme a good hard smack! It's got to be believable! Don't worry, it won't hurt me anyways!"
                        e "I-"
                        P "What's wrong, Ellis?"
                        e "I-I'm trying..."

                        call hitPhi
                        pause(1.0)
                        call hitPhi
                        pause(1.0)

                        "No matter how many times Ellis hits PHI's palm, she simply does not notice."
                        P "Ellis, is this really you hitting your hardest...?"
                        "Feeling the cold, judgemental eyes that laid on him, Ellis quickly does a 180 and blurts out:"
                        
                        show ellisCringe at ellis_std:
                            linear 0.3 xalign -0.8
                        jump comm4BadEnd
                    if strength >= 2:
                        hide ellisCry
                        show ellisCringe at ellis_std:
                            xalign 0.0
                        
                        call hitPhi
                        "Ellis gives PHI's palm a good hard smack."
                        P "UWAAAAAAAUGH...!"
                        P "Y-You..."
                        P "Got me."
                        "(PHI dramatically sinks to her knees.)"

                        hide phiNeutral with dissolve

                        e "... ah? (I didn't actually hurt her, did I?)"
                        jump comm4GoodEnd
                "Go with Joughseph's suggestion and pretend to be a tree.":
                    kid2 "Yayyyyyy!"
                    
                    show phiNeutral at phi_std:
                        linear 0.6 xalign 1.8
                    show joNeutral at jo_std:
                        linear 0.6 xalign 1.8
                    show deltaAnnoyed at delta_std:
                        linear 0.6 xalign 1.0

                    "The moment Ellis climbs onto the monkey bars, the kids start circling under Ellis, chanting... something."
                    kid2 "ASHES! ASHES! THEY ALL FALL DOWN!"
                    "(I dunno, sounds kinda demonic to me)."
                    if stamina < 2:
                        hide ellisThinking2
                        show ellisCry at ellis_std:
                            xalign 0.0

                        "Ellis attempts to hang on for dear life but-"

                        hide ellisCry
                        show ellisSurprised at ellis_std with hpunch:
                            xalign 0.0
                        hide deltaAnnoyed
                        show deltaInquire at delta_std:
                            xalign 1.0

                        "Whoops. Butterfingers."
                        j "WATCH OUT!"

                        show deltaInquire at delta_std with hpunch:
                            linear 0.2 xalign 0.3

                        "DELTA gracefully catches Ellis and sets him down while Josephine and PHI ensure none of the kids are hurt."
                        jump comm4BadEnd
                    if stamina >= 2:
                        show phiNeutral at phi_std:
                            linear 0.6 xalign 1.8
                        show joNeutral at jo_std:
                            linear 0.6 xalign 1.8
                        show deltaAnnoyed at delta_std:
                            linear 0.6 xalign 1.0
                        
                        hide ellisThinking2
                        show ellisCringe at ellis_std:
                            xalign 0.0

                        "Ellis hangs on for dear life pretending to be a tree as the kids start chanting yet another... ritual?"
                        kid3 "HUMPTY DUMPTY HAD A HUGE FALL"
                        kid1 "ALL THE KING'S HORSES AND ALL THE KING'S MEN"
                        kid2 "COULD NOT PUT HUMPTY TOGETHER AGAIN!"
                        "Ellis is... hello? Earth to- oh my, he's fainted from shock."
                        jump comm4GoodEnd
                "Go with Rose's suggestion and have a race":
                    kid3 "Let us have an honorable competition."

                    show phiNeutral at phi_std:
                        linear 0.6 xalign 1.0
                    show deltaAnnoyed at delta_std:
                        linear 0.6 xalign 1.8
                    show joNeutral at jo_std:
                        linear 0.6 xalign 1.8
                    show joNervous at jo_std:
                        xalign 1.8
                    show joExclaim at jo_std:
                        xalign 1.8

                    hide ellisThinking2
                    show ellisSad2 at ellis_std:
                        xalign 0.0
                    show ellisSurprised at ellis_std:
                        xalign -0.8
                    
                    e "A-Alright! Be warned: I won't go easy on you!"
                    P "aaaaand the race is afoot!"

                    show ellisSad2 at ellis_std:
                        linear 0.3 xalign -0.8

                    if speed >= 2:
                        P "Rose starts off strong with a huge lead off Ellis!"
                        
                        show joExclaim at jo_std:
                            linear 0.6 xalign 0.5

                        j "Woah but what's this?! Ellis is quickly gaining ground!"
                        j "oooooOOOH THEY'RE NECK AND NECK NOW, IT'S ANYONE'S GAME...!"
                        "*TWEEEEEEET*"
                        P "Ellis wins!"
                        
                        show ellisSurprised at ellis_std:
                            linear 1.0 xalign 0.0
                        
                        e "*pant* *pant* *wheeeze*"

                        hide ellisSurprised
                        show ellisWince at ellis_std:
                            xalign 0.0
                        
                        e "I haven't run this much in years..."
                        kid3 "Again! Again!"
                        kid1 "OOOOOOOO ME NEXT!"
                        e "A-Alrighty! I've still got some fight in me, just give me a moment...!"
                        jump comm4GoodEnd
                    if speed < 2:
                        P "Rose starts off strong with a huge lead off Ellis!"
                        
                        show joNervous at jo_std:
                            linear 0.6 xalign 0.5
                        j "Ellis seems to be uhhh... lagging behind... quite a bit..."
                        P "Oh dear, Ellis is not doing too hot-"
                        
                        show blackScreen with fade
                        "*an excruciating and painful 5 minutes later*"

                        hide blackScreen with dissolve

                        show ellisSurprised at ellis_std:
                            linear 1.0 xalign 0.0
                        e "*gasp* *wheeze* *gasp* *gasp* *wheeeeeeeeeeeze*"
                        kid3 "You're not very good at using your legs to propel yourself forward using the bodily kinematic motions of your tendons."
                        e "I- *gasp* wh- HUH?"
                        jump comm4BadEnd

label comm4GoodEnd:
    scene park with fade

    show ellisNeutral at ellis_std with dissolve:
        xalign 0.0
    show deltaAnnoyed at delta_std with dissolve:
        xalign 0.3
    show phiNeutral at phi_std with dissolve:
        xalign 0.8
    show joClosed at jo_std with dissolve:
        xalign 1.1
    
    "A fun filled hour passes by like the blink of an eye and it isn't long before the children's parents come."
    e "W-Whew... I... I survived."
    j "Good job, Ellis! This is one small step for you, one big step for the Association!!"
    
    hide ellisNeutral
    show ellisNervous at ellis_std:
        xalign 0.0
    
    e "I-I don't think my progress is representative of the Association as a whole..."
    j "Nonsense!"
    
    hide ellisNervous
    show ellisNeutral at ellis_std:
        xalign 0.0

    "As Ellis and Josephine keep talking, DELTA and PHI similarly converse about their partners."
    kid1 "H-Hey... Ellis?"
    e "Heya little Johnnathaeign. Why do you seem so sad?"
    kid1 "Will you be back next time?"
    kid2 "I wanna play with Ellis too next time!"
    kid3 "I concur."
    
    hide deltaAnnoyed
    show deltaHappy at delta_std:
        xalign 0.3
    
    "Ellis looks around to see the patient faces of Josephine, DELTA, and PHI and the puppy-eyed kids and eventually say:"
    
    hide ellisNeutral
    show ellisHappy at ellis_std:
        xalign 0.0

    e "Yes!"

    show blackScreen with fade
    "For their... efforts, Ellis and Josephine each receive $5."

    $ money += 5
    $ commission4Done = True
    return

label comm4BadEnd:
    e "S-Sorry! I-Uh-Um-What I mean to say is- uh- I gotta go!"
    "And with that, Ellis runs out of the park."
    
    scene park with fade
    
    show ellisNeutral at ellis_std:
        xalign -0.8
    show deltaAnnoyed at delta_std with dissolve:
        xalign 0.3
    show phiNeutral at phi_std with dissolve:
        xalign 0.8
    show joClosed at jo_std with dissolve:
        xalign 1.1

    pause(0.3)
    show ellisNeutral at ellis_std:
        linear 0.6 xalign 0.0
    pause(0.6)

    "(The situation appears to have resolved itself, as the ducks have flown off.)"
    e "O-Oh I guess uh the whole thing's over with..."
    
    hide deltaAnnoyed
    show deltaInquire at delta_std:
        xalign 0.3
    
    D "That is correct. If there's nothing else, let us be on our way."
    "Glancing backwards one last time, Ellis sees Josephine waving at him."
    j "Next time, you got this!"
    return

label hitPhi:
    show ellisCringe at ellis_std:
        linear 0.3 xalign -0.1
    pause(0.01)
    show ellisCringe at ellis_std:
        linear 0.1 xalign 0.2
    pause(0.01)
    show ellisCringe at ellis_std:
        linear 0.3 xalign 0.0