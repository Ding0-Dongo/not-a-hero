# this social event unlocks only if 
# josephine's apology was completed.

label volunteerClinic:
    if energy < 3:
        "Ellis is too tired to do that right now."
        return
    else:
        if clinicVolunteerDone == True:
            scene hospitalInterior with fade
            show deltaNeutral at delta_std:
                xalign 0.2
            show ellisHappy at ellis_std:
                xalign 0.8
            
            "(DELTA and Ellis volunteer at the clinic. They help out visitors and pass out flyers.)"
            $ energy -= 3
            $ stress += 2
            $ social += 3

            show blackScreen with fade
        else:
            scene hq with fade
            show deltaInquire at delta_std:
                xalign 0.2
            show ellisNeutral at ellis_std:
                xalign 0.8
            
            D "Ellis, did you know they have an event going on at the clinic this week?"

            hide deltaInquire
            show deltaNeutral at delta_std:
                xalign 0.2
            hide ellisNeutral
            show ellisAsk at ellis_std:
                xalign 0.8
            
            e "Oh, um... yeah, I... I already know."

            hide ellisAsk
            show ellisHappy at ellis_std:
                xalign 0.8
            
            e "I don't mind volunteering there, I guess."

            hide deltaNeutral
            show deltaInquire at delta_std:
                xalign 0.2
            
            D "Oh? Did you already volunteer there?"

            hide deltaInquire
            show deltaNeutral at delta_std:
                xalign 0.2
            hide ellisHappy
            show ellisSad2 at ellis_std:
                xalign 0.8
            
            e "Er... something like that?"
            D "(He doesn't look so comfortable talking about it.)"

            menu:
                "Ask about it politely":
                    hide deltaNeutral
                    show deltaInquire at delta_std:
                        xalign 0.2
                    
                    D "Do you want to talk about it?"

                    hide deltaInquire
                    show deltaNeutral at delta_std:
                        xalign 0.2
                    
                    e "It's- it's nothing, really, nothing {i}too{/i} serious, just..."

                    call volunteerClinicAsk
                "Ask about it firmly":
                    hide deltaNeutral
                    show deltaClosed at delta_std:
                        xalign 0.2
                    
                    D "Well, what happened?"

                    hide deltaClosed
                    show deltaNeutral at delta_std:
                        xalign 0.2
                    
                    e "Nothing, just..."

                    call volunteerClinicAsk
                "Let it go":
                    D "(He'll talk about it when he's ready.)"

            show blackScreen with fade
            scene hospitalInterior with fade
            
            show deltaNeutral at delta_std:
                xalign 0.2
            show ellisNeutral at ellis_std:
                xalign 0.8
                
            "(DELTA and Ellis volunteer at the clinic. They help out visitors and pass out flyers.)"

            show blackScreen with fade

            $ energy -= 3
            $ stress += 2
            $ social += 3

            return

label volunteerClinicAsk:
    hide ellisSad2
    show ellisSad at ellis_std:
        xalign 0.8
    
    e "*sigh* ... I think we had a fight..."

    hide deltaNeutral
    show deltaThinking at delta_std:
        xalign 0.2
    
    D "A fight? You and whom?"

    hide ellisSad
    show ellisSurprised at ellis_std:
        xalign 0.8
    
    e "Well- not a physical one of course-"

    hide deltaThinking
    show deltaTeasing at delta_std:
        xalign 0.2
    
    D "*lightheartedly* That's a given."

    hide ellisSurprised
    show ellisHappy at ellis_std:
        xalign 0.8
    
    e "*stifles a laugh* DELTA!"
    D "Sorry, sorry, go on."

    hide deltaTeasing
    show deltaThinking at delta_std:
        xalign 0.2
    hide ellisHappy
    show ellisNeutral at ellis_std:
        xalign 0.8
    
    e "We had an argument... me and Desmond and Josephine. Not really an argument, but..."

    hide ellisNeutral
    show ellisSad at ellis_std:
        xalign 0.8
    
    e "I guess we didn't really... communicate too well."
    e "Josephine asked me to meet her at the clinic so she could apologize."

    hide deltaThinking
    show deltaInquire at delta_std:
        xalign 0.2
    
    D "Oh? Good for you, Ellis... good for you. You two talked things out, then?"

    hide deltaInquire
    show deltaNeutral at delta_std:
        xalign 0.2
    hide ellisSad
    show ellisNeutral at ellis_std:
        xalign 0.8
    
    e "*nods* I think it went pretty OK. I mean, we're not confused or upset anymore, so..."

    hide ellisNeutral
    show ellisThinking2 at ellis_std:
        xalign 0.8
    
    e "But... my point is-! I think I'm ready to volunteer at the clinic."

    hide deltaNeutral
    show deltaHappy at delta_std:
        xalign 0.2
    
    D "*smiles* Good to hear."
    D "You know, Ellis, you might be ready to do commissions on your own soon."

    hide ellisThinking2
    show ellisSurprised at ellis_std:
        xalign 0.8
    
    e "What? No, I- I still need you, DELTA. It's only been a week, I'm not... I don't think I'm ready to go out on my own yet."

    hide deltaHappy
    show deltaTeasing at delta_std:
        xalign 0.2
    
    D "Oh, no, you've been getting a lot more independent lately, Ellis. Haven't you noticed?"

    hide ellisSurprised
    show ellisNervous at ellis_std:
        xalign 0.8
    
    e "But- I'm not-"

    hide deltaTeasing
    show deltaHappy at delta_std:
        xalign 0.2
    
    D "Don't worry, it's not like I'm abandoning you. You'll just have a lot more freedom."

    hide deltaHappy
    show deltaClosed at delta_std:
        xalign 0.2
    
    D "If you ever need guidance, I'll be right there. And of course, you can always get help from your TEAM, or the other mentors."

    hide deltaClosed
    show deltaHappy at delta_std:
        xalign 0.2
    
    D "But we can figure that out later. For now, we'll volunteer at the clinic, alright?"

    pause(1)

    hide ellisNervous
    show ellisHappy at ellis_std:
        xalign 0.8
    
    e ".... alright! *nods*"
    