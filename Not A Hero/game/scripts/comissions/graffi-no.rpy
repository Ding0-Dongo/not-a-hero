label graffiNo:
    if energy < 2:
        "Ellis is too tired to do that right now."
        return
    else:
        if commission3Done:
            scene alleyway

            show ellisHappy at ellis_std:
                xalign -1.8
            pause(0.1)
            show ellisHappy at ellis_std:
                linear 0.3 xalign 0.5

            e "Here I come!"
            gangster "NOT YOU AGAIN-"

            show ellisHappy at ellis_std with hpunch:
                xalign 0.5
            
            show blackScreen with fade

            "+$10"

            $ money += 10
            $ energy -= 2
            return
        else:
            "Downtown Normington, random time afternoon"

            scene alleyway with fade

            "*sketchy noises*"

            show deltaNeutral at delta_std with dissolve:
                xalign 0.2
            show ellisNeutral at ellis_std with dissolve:
                xalign 0.8  
            
            D "We've received reports of rampant gang activity around this part of Normington."
            
            hide deltaNeutral
            show deltaClosed at delta_std:
                xalign 0.2
            
            D "Including but not limited to: thievery, shoplifting, obscene graffiti-"
            e "Like the one right in front of us."
            D "Correct."

            hide ellisNeutral
            show ellisSurprised at ellis_std with hpunch:
                xalign 0.8

            gangster "WACHU SAY ABOUT MY WORK OF ART; MY MASTERPIECE?!"

            hide deltaClosed
            show deltaInquire at delta_std:
                xalign 0.2

            D "We kindly request you take down your \"work of art\" before we resort to filing your case under the Normington Association of-"
            
            hide deltaInquire
            show deltaAnnoyed at delta_std with hpunch:
                xalign 0.2
            
            gangster "YEAH YEAH, BLAB ALL YOU WANT, YOU AINT GETTING ANYTHING OUTTA ME, ANDROID-BOY!"
            
            hide deltaAnnoyed
            show deltaSerious at delta_std:
                xalign 0.2
            
            D "...Interrupt me once more and I'll-"
            
            hide deltaSerious
            show deltaAnnoyed at delta_std:
                xalign 0.2
            hide ellisSurprised
            show ellisNeutral at ellis_std:
                xalign 0.8
            
            ultraMobBoss "Well well well... what do we have here?"
            ultraMobBoss "Roaming into my territory and threatening my boys..."
            ultraMobBoss "Tsk... Tsk... Tsk..."
            ultraMobBoss "You heroes are all the same."
            
            hide ellisNeutral
            show ellisAsk at ellis_std:
                xalign 0.8

            e "But you're committing crimes which is bad!"
            
            hide ellisAsk
            show ellisSurprised at ellis_std:
                xalign 0.8

            ultraMobBoss "Yap any more, and I'll have to put you down, dog."
            gangster "YEAH YOU TELL 'EM BOSSMAN!"
            "Arid winds blows through the quiet alleyway, DELTA locking eyes with both the thug and the Godfather simultaneously."
            
            hide deltaAnnoyed
            show deltaClosed at delta_std:
                xalign 0.2
            
            hide ellisSurprised
            show ellisNeutral at ellis_std:
                xalign 0.8

            D "Ellis, I'll defend you. Do what you must to resolve this."
            "What should I do...?"
            menu:
                "Attempt to help DELTA by attacking the goon.":
                    hide ellisNeutral
                    show ellisNervous at ellis_std:
                        xalign 0.8
                    
                    "Without thinking, Ellis charges straight towards the goon."
                    "Roll for initiative!"
                    "..."

                    hide ellisNervous
                    show ellisSurprised at ellis_std with hpunch:
                        xalign 0.8
                    
                    e "... (!!!)"
                    "... let's just say Ellis is no longer allowed to roll die!"
                    
                    hide deltaClosed
                    show deltaSerious at delta_std with hpunch:
                        xalign 0.2
                    
                    "Thankfully, DELTA rolled a 20 and the thug is put down. Very forcibly."
                    gangster "OW"
                    ultraMobBoss "AAAAAAAA"
                    "The boss starts booking it down the road; far, far down the road."
                    gangster "BOSS WHERE ARE YOU GOING-"
                "Attempt to help DELTA by attacking the boss.":
                    hide ellisNeutral
                    show ellisNervous at ellis_std:
                        xalign 0.8
                    
                    "Without thinking, Ellis charges straight towards the godfather."
                    
                    show ellisNervous at ellis_std with hpunch:
                        xalign 0.8
                    
                    ultraMobBoss "AAAAAAAAAAAAAAAAAAAAAAAAAA DKFLSAJF;LSJADFLS;KA"
                    
                    hide deltaClosed
                    show deltaAnnoyed at delta_std:
                        xalign 0.2
                    
                    hide ellisNervous
                    show ellisAsk at ellis_std:
                        xalign 0.8
                    
                    e "(???)"
                    "Startled, and quite frankly terrified, the godfather starts to sprint away."
                    gangster "WHY ARE YOU RUNNING AREN'T YOU SUPPOSED TO BE LIKE THE TOP DOG, THE MOST POWERFUL DUDE MAN???"
                    ultraMobBoss "I DUNNO USUALLY THE HERO TAKES DOWN THE GOONS FIRST."
                    gangster "WHAT."
                    "The two take off into a very conspicuous dark alleyway, never to be seen for the rest of the day."

                    hide deltaAnnoyed
                    show deltaInquire at delta_std:
                        xalign 0.2
                    
                    D "Interesting."
                    e "... what just happened?"
                "Start erasing the graffiti.":
                    hide ellisNeutral
                    show ellisSurprised at ellis_std with hpunch:
                        xalign 0.8
                    
                    gangster "STOOOOOOOOOOOOOP!!!!11!"

                    hide ellisSurprised
                    show ellisNeutral at ellis_std:
                        xalign 0.8
                    hide deltaClosed
                    show deltaNeutral at delta_std:
                        xalign 0.2
                    
                    gangster "I-I was serious when I said this is my work of art..."
                    gangster "So it all started when I was 5 years old when I first saw Leonardo Da Vinci's Mona Lisa."
                    
                    hide deltaNeutral
                    show deltaAnnoyed at delta_std:
                        xalign 0.2
                    
                    "The thug starts relaying his entire life story up until this point."
                    
                    show blackScreen with fade
                    pause(0.1)                    
                    scene alleyway

                    show deltaAnnoyed at delta_std:
                        xalign 0.2
                    show ellisCringe at ellis_std:
                        xalign 0.8

                    "Every single hardship, trauma, disappointment, failure, embarrassment. By the end of his monologue, Ellis understands the thug more than anyone else he had up until this point."
                    "Enlightening, really."
                    gangster "...and then I got rejected from art school and that's how I got to where I am now."                
                    gangster "..."
                    gangster "...I need a moment-"
                    "The thug says before promptly dashing off, the mob boss having gone off ever since he started monologuing."
                    e "Poor guy..."

            show blackScreen with fade
            "After dealing with whatever else that remained, DELTA and Ellis spent the next half hour scrubbing off some quite amazingly sprayed graffiti."
            "For their efforts, they recieve $10 from the association."
            $ money += 10
            $ energy -= 2
            $ commission3Done = True
            return