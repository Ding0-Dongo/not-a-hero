label fundraising:
    if energy < 1:
        "Ellis is too tired to do that right now."
        return
    else:
        if fundraisingDone == True:
            scene plaza with fade

            show deltaNeutral at delta_std:
                xalign 0.2
            show ellisHappy at ellis_std:
                xalign 0.8
            
            "(DELTA and Ellis spend some time at the fundraiser again.)"
            $ stress += 1
            $ tempSocialLevel += 2

            show blackScreen with fade
            return
        else:
            scene plaza with fade

            show deltaNeutral at delta_std:
                xalign 0.2
            show ellisNeutral at ellis_std:
                xalign 0.8
            
            e "*looking around* I didn't see this one in our schedule for today..."

            hide deltaNeutral
            show deltaInquire at delta_std:
                xalign 0.2
            
            D "PHI and Josephine invited us. It's a fundraising event."
            
            hide deltaInquire
            show deltaNeutral at delta_std:
                xalign 0.2
            hide ellisNeutral
            show ellisNervous at ellis_std:
                xalign 0.8
            
            e "What? But..."
            D "(He looks upset.)"

            menu:
                "You'll be fine.":
                    hide deltaNeutral
                    show deltaWisdom at delta_std:
                        xalign 0.2
                    
                    D "Come on, you'll be fine."
                    "(Ellis looks uncomfortable, but is too polite to disagree.)"
                "What's wrong?":
                    hide deltaNeutral
                    show deltaThinking at delta_std:
                        xalign 0.2
                    
                    D "What's wrong?"
                    "(DELTA waits until Ellis finds the words for what he wants to say.)"

                    hide ellisNervous
                    show ellisShy at ellis_std:
                        xalign 0.8
                    
                    e "It's just... *tries not to sound desperate* It... it sounds like a lot of... interaction...?"

                    hide deltaThinking
                    show deltaClosed at delta_std:
                        xalign 0.2
                    
                    D "Oh no, you don't have to talk to people if you don't want to."
                    e "But....?"
                    D "Just you being there is enough. And if you get tired, remember, we can always step out."

                    hide ellisShy
                    show ellisNeutral at ellis_std:
                        xalign 0.8
                    
                    e "They'll look at me weird, won't they? Won't it be weird if I disappeared halfway through the event?"                    
                    D "People come and go all the time at events. C'mon. I've got you."
                    
                    hide deltaClosed
                    show deltaTeasing at delta_std:
                        xalign 0.2
                    
                    D "I know I'm pushing you, but I think you can do it, Ellis. You've already been doing so well."
                    
                    hide ellisNeutral
                    show ellisAnnoyed at ellis_std:
                        xalign 0.8
                    
                    e "..."
                    "(Ellis takes a deep breath.)"

                    hide ellisAnnoyed
                    show ellisSad at ellis_std:
                        xalign 0.8
                    
                    e "O... OK. I- I'll try."
                    D "*smiles* You're already shaking."

                    hide ellisSad
                    show ellisAnnoyed at ellis_std:
                        xalign 0.8
                    
                    e "N-no I'm not."
                    D "It's OK. We'll take it slow. One conversation at a time."

                    hide ellisAnnoyed
                    show ellisNeutral at ellis_std:
                        xalign 0.8
                    
                    e "*nods*"
            
            hide deltaTeasing
            hide ellisNervous

            show deltaNeutral at delta_std:
                xalign 0.2
            show ellisNeutral at ellis_std:
                xalign 0.8
            
            "(DELTA and Ellis walk into the fundraising event.)"
            "(They check out some of the booths, talk to a few prospective donators, and do a lot of walking around.)"
            "(They also meet Josephine and PHI, but since they're on the job, they simply nod to each other and move along.)"
            "(After a while, Ellis finds his way over to some chairs and sits down.)"

            hide deltaNeutral
            show deltaInquire at delta_std:
                xalign 0.2
            hide ellisNeutral
            show ellisNervous at ellis_std:
                xalign 0.8
            
            D "Mm? Done for today?"

            hide deltaInquire
            show deltaNeutral at delta_std:
                xalign 0.2
            
            e "*nods, exhausted*"

            hide deltaNeutral
            show deltaTeasing at delta_std:
                xalign 0.2
            
            D "*smiles* Good job. Here, I picked this up for you while we were at one of the booths."
            "(DELTA hands Ellis x1 Energy Drink Plus.)"
            e "Oh... thanks, DELTA. *opens up the can*"

            hide deltaTeasing
            show deltaClosed at delta_std:
                xalign 0.2
            
            D "Drink it slowly now, it's a little stronger than-"

            hide ellisNervous
            show ellisSurprised at ellis_std with hpunch:
                xalign 0.8
            
            e "*pauses after the first sip, eyes widen*"
            
            hide deltaClosed
            show deltaSerious at delta_std:
                xalign 0.2
            
            D "Usual.... (looks around) Oops."
            "(DELTA sees PHI nearby and quickly helps Ellis to his feet.)"
            D "Alright, time to go."

            hide ellisSurprised
            show ellisHappy at ellis_std:
                xalign 0.8
            
            e "Can I have another one?"

            hide deltaSerious
            show deltaThinking at delta_std:
                xalign 0.2
            
            D "What? *in disbelief* I- sure, but let's get out of here first."

            show blackScreen with fade

            $ energy += energyDrinkPlus
            $ energy -= 1
            $ stress += 1
            $ tempSocialLevel += 2

            return