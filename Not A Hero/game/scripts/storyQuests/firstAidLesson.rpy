label firstAidLesson:
    if energy < 2:
        "Ellis is too tired to do that right now."
        return
    else:
        scene plaza with fade

        show joClosed at jo_std:
            xalign 1.5
        show ellisNeutral at ellis_std:
            xalign -0.5
        
        show joClosed at jo_std:
            linear 0.3 xalign 1.0
        show ellisNeutral at ellis_std:
            linear 0.3 xalign 0.0

        "(Ellis finds himself on the edges of Normington Plaza.)"
        "(It looks like some kind of rather large event is going on near the center.)"
        e "... *uncomfortable*"

        hide joClosed
        show joExclaim at jo_std:
            xalign 1.0
        
        j "*turns and sees him* Oh, Ellis? Ellis, hey! Over here! *waves at him*"
        
        hide ellisNeutral
        show ellisShy at ellis_std:
            xalign 0.0
        
        e "(Is... is that... Josephine?) *gulp* (I can't pretend like I didn't see her... oh no...)"
        e "*sigh* (Guess I better go over to her... maybe I should've just stayed home today...)"
        "(It takes much effort for Ellis to walk over to Josephine, who is smack-dab in the middle of the event.)"

        show ellisShy at ellis_std:
            linear 0.3 xalign 0.2
        show joExclaim at jo_std:
            linear 0.3 xalign 0.8
        
        j "*eyes twinkle* Ellis! I'm so glad you could make it!"

        hide ellisShy
        show ellisCringe at ellis_std:
            xalign 0.2
        
        e "*tries to laugh* Um... yeah..."
        e "(Is she... hosting this event?)"

        hide ellisCringe
        show ellisNeutral at ellis_std:
            xalign 0.2
        hide joExclaim
        show joNeutral at jo_std:
            xalign 0.8
        
        j "I'm holding a workshop to teach citizens the basics of first aid! Do you want to help?"
        j "It's a TEAM commission. Did Desmond or DELTA tell you about those already?"

        if deliveryRunDone == True:
            e "Um... yeah. Desmond told me about them."

            hide joNeutral
            show joFrown2 at jo_std:
                xalign 0.8
            
            j "Aw, man! I was hoping to be the one to introduce you to them."

            hide joFrown2
            show joNeutral at jo_std:
                xalign 0.8
            
            j "What did you two do together?"

            hide ellisNeutral
            show ellisThinking at ellis_std:
                xalign 0.2
            
            e "Just... um... just delivered some packages, that's all."
            j "Oh, don't undersell yourself, Ellis. Package delivering is important, you know. And so often untimely..."

        else:
            hide ellisNeutral
            show ellisShy at ellis_std:
                xalign 0.2
            
            e "Um... no, should I have known about these already?"

            hide joNeutral
            show joExclaim at jo_std:
                xalign 0.8
            
            j "Oh no, don't sweat it! I'll introduce you to them! They're really easy to get the hang of!"
            e "(That's a relief....)"
            
            hide joExclaim
            show joNeutral at jo_std:
                xalign 0.8
            
            j "So basically, TEAM commissions are just normal commissions, but you do with them with a TEAMmate!"
            j "Generally they net more rewards for each participant, I think..."
            j "And you'll have to do at least a few in your HERO career, since you have to fulfill a certain number of TEAM commissions before you can graduate as a full-fledged hero."
            j "Make sense?"

        hide ellisThinking
        hide ellisShy
        show ellisNeutral at ellis_std:
            xalign 0.2
        
        e "*nods*"
        j "So, want to help me? We'll teach things like CPR, contents and usage of first aid kits, sanitation and hygiene, and more!"

        menu:
            "Sure":
                hide ellisNeutral
                show ellisNervous at ellis_std:
                    xalign 0.2

                e "As long as I don't have to demonstrate CPR..."
                e "Because I don't know how."

                hide ellisNervous
                show ellisNeutral at ellis_std:
                    xalign 0.2
                
                hide joNeutral
                show joExclaim at jo_std:
                    xalign 0.8
                
                j "*laughs* Oh, don't worry about it! Leave that up to me. Maybe you could even learn it too, while you're here!"
                e "(Might not be a bad idea, actually...)"
                
                hide joExclaim
                show joNeutral at jo_std:
                    xalign 0.8
                
                j "I'll get you started over at this station here with me, I'm teaching kids how to properly clean and bandage scrapes."
                "(Josephine leads Ellis over to a stand of colorful bandages and alcohol wipes.)"
                j "See? Pretty nice setup we've got here, huh?"
                e "*nods weakly*"
                j "*smiles warmly* Don't worry, Ellis. I know this may be out of your comfort zone, but..."
                e "You know, I'm pretty proud that you're trying. It's not easy, is it?"

                menu:
                    "It's not that bad":
                        hide ellisNeutral
                        show ellisCringe at ellis_std:
                            xalign 0.2
                        
                        e "It's... uh, it's not {i}that{/i} bad..."

                        hide joNeutral
                        show joClosed at jo_std:
                            xalign 0.8
                        
                        j "*she smiles* You're really brave, Ellis..."
                        j "I know for sure I wasn't this brave when I first started out!"
                    "It's the hardest thing in the world":
                        hide ellisNeutral
                        show ellisCringe at ellis_std:
                            xalign 0.2
                        
                        e "It feels like the hardest thing in the world..."

                        hide joNeutral
                        show joFrown at jo_std:
                            xalign 0.8
                        
                        j "Oh no!... You know what? You look like you might need a little something for the rest of the day..."

                hide joFrown
                show joNeutral at jo_std:
                    xalign 0.8
                hide ellisCringe
                show ellisNeutral at ellis_std:
                    xalign 0.2
                
                "(Josephine grabs an energy drink from under the table and hands it to Ellis.)"
                j "Here, something to keep you going. And don't be afraid to take a break!"

                show blackScreen with fade
                "(Josephine and Ellis spend a few hours teaching the importance and basics of first aid.)"
                "(It's mentally exhausting for Ellis, and he gets burned out partway. Fortunately for him, Josephine takes over for the rest of the workshop and lets him rest.)"
                "(For Ellis's efforts, the commission awards him $10. Josephine gives him a little extra, telling him to \"buy something nice\".)"
                "'PSA' commission unlocked."

                $ money += 15
                $ energy -= 2
                $ firstAidDone = True

            "No thanks":
                hide ellisNeutral
                show ellisSad at ellis_std:
                    xalign 0.2
                
                e "Hm, um... I'll... I'll have to think about it."

                hide joNeutral
                show joFrown at jo_std:
                    xalign 0.8
                
                j "Oh, really? Aw, well, that's OK."
                
                hide ellisSad
                show ellisNeutral at ellis_std:
                    xalign 0.2
                
                hide joFrown
                show joNeutral at jo_std:
                    xalign 0.8
                
                j "The workshop is all week, so if you change your mind, I'll be here!"
                j "*whispers conspiratorially* Or you can make Desmond come instead, he neeever does volunteering commissions."
                e "... oh?"
                j "He prefers the service ones more, but I know he needs the practice."

                hide ellisNeutral
                show ellisHappy at ellis_std:
                    xalign 0.2
                
                e "*laughs* OK... bye, Josephine."

                hide joNeutral
                show joExclaim at jo_std:
                    xalign 0.8
                
                j "Yeah! See ya 'round, Ellis! *waves*"

                show blackScreen with fade