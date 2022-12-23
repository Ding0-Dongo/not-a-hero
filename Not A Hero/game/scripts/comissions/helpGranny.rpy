label helpGranny:
    if energy < 1:
        "Ellis is too tired to do that right now."
        return
    else:
        if commission5Done:
            scene apartments with fade
            show ellisNeutral at ellis_std:
                xalign 0.8
            show deltaNeutral at delta_std:
                xalign 0.2

            e "Again?"
            oldLady "Again."
            D "Agreed."
            cat "*Meows with the exaggerated swagger of a small war criminal*"
            e "Haa..."
            $ money += 5
            $ energy -= 1
            return
        else:
            "Normington Hills, 08:00 AM"

            scene apartments with fade

            show deltaNeutral at delta_std:
                xalign 1.5
            show ellisSurprised at ellis_std:
                xalign 1.5
            
            show deltaNeutral at delta_std:
                linear 0.5 xalign 0.2
            show ellisSurprised at ellis_std:
                linear 0.5 xalign 0.8
            
            e "D-Delta... why did we have to wake up this early? The association doesn't even open till 9!"

            hide ellisSurprised
            show ellisAnnoyed at ellis_std:
                xalign 0.8
            
            hide deltaNeutral
            show deltaClosed at delta_std:
                xalign 0.2

            D "Where there are civilians in need of help, we must answer. There are no excuses to not responding to the needs of the people immediately."
            e "I wanna go back to bed..."
            oldLady "Ohohoho... it's good to rise early, young'uns, for the sunrise grants us energy."

            hide deltaClosed
            show deltaNeutral at delta_std:
                xalign 0.2

            hide ellisAnnoyed
            show ellisSurprised at ellis_std with hpunch:
                xalign 0.8
            
            e "A-AAAH! WHERE DID YOU COME FROM?!"
            oldLady "Ah ah ah, not so loud! It's early in the morning, young man!"

            hide deltaNeutral
            show deltaInquire at delta_std:
                xalign 0.2
            
            D "Good morning ma'am. We are here on behalf of the Normington Association of Heroes."

            hide deltaInquire
            show deltaNeutral at delta_std:
                xalign 0.2
            
            oldLady "Ah yes, I remember asking for help from you lot."
            oldLady "You see, my cat got stuck on this tree outside."

            hide ellisSurprised
            show ellisAnnoyed at ellis_std:
                xalign 0.8
            
            e "You mean the ONE TREE on this entire block???"
            cat "*Meows with the passion of the holy sunrise*"
            oldLady "Oooooh my poor baby... *sniffle *sniffle"

            hide deltaNeutral
            show deltaHappy at delta_std:
                xalign 0.2

            D "Well then, Ellis. As the saying goes, \"The floor's all yours\""

            hide ellisAnnoyed
            show ellisThinking at ellis_std:
                xalign 0.8
            
            "What should I do?"
            menu:
                "Shake Tree":
                    hide ellisThinking
                    show ellisNeutral at ellis_std:
                        xalign 0.8

                    if strength < 5:
                        "Ellis gently shakes the tree, knocking the cat back and forth before it eventually jumps from the branches onto the arms of the old lady."
                        jump comm5GoodEnd
                    else:
                        "Ellis shakes the tree so hard, the cat clings to the tree, petrified to make a move."
                        jump comm5BadEnd
                "Climb Tree":
                    hide ellisThinking
                    show ellisNeutral at ellis_std:
                        xalign 0.8

                    "Ellis begins climbing the tree when suddenly..."

                    hide ellisNeutral
                    show ellisSurprised at ellis_std with hpunch:
                        xalign 0.8
                    
                    "QUICK! A QTE!"
                    "QUICKLY, ELLIS, PRESS Q!"
                    "...did you press Q?"
                    
                    hide ellisSurprised
                    show ellisAnnoyed at ellis_std:
                        xalign 0.8
                    
                    "We don't know how to make QTEs in Ren'Py so it doesn't matter."
                    jump comm5GoodEnd
                "Lure Cat Down With Food":
                    e "...what do I even have that can lure a cat?"
                    "Delta pulls out a piece of dried squid from his pocket and hands it to Ellis."

                    hide deltaHappy
                    show deltaInquire at delta_std:
                        xalign 0.2

                    D "This may come in handy."

                    hide ellisThinking
                    show ellisAnnoyed2 at ellis_std:
                        xalign 0.8
                    
                    e "Do you always have stuff like this on hand-"

                    hide ellisAnnoyed2
                    show ellisSurprised at ellis_std with hpunch:
                        xalign 0.8
                    
                    "*THUD*"
                    "(The cat jumped into Ellis's arms.)"
                    "Lo and behold, it worked like a charm."
                    jump comm5GoodEnd

label comm5GoodEnd:
    oldLady "Ohohoho... Thank you, young hero for taking time out of your busy day to help a decrepit old lady like me..."

    hide ellisNeutral
    hide ellisAnnoyed
    hide ellisSurprised
    show ellisShy at ellis_std:
        xalign 0.8
    
    e "Decrepit? I wouldn't exactly say-"

    hide deltaHappy
    show deltaInquire at delta_std:
        xalign 0.2
    
    D "Forgive my intrusion ma'am, but my partner, Ellis, is formally known as a HERO, not hero."
    
    hide ellisShy
    show ellisAnnoyed at ellis_std:
        xalign 0.8
    
    e "...how did you notice the difference??"
    $ money += 5
    $ energy -= 1
    $ commission5Done = True
    return

label comm5BadEnd:
    hide deltaHappy
    show deltaNeutral at delta_std:
        xalign 0.2
    
    hide ellisNeutral
    show ellisShy at ellis_std:
        xalign 0.8
    
    oldLady "My poor fluffy baby..."
    "Ellis looks down, wishing he could have done more to help."

    hide deltaNeutral
    show deltaClosed at delta_std:
        xalign 0.2
    
    D "It's ok, maybe you'll get it next time."

    hide ellisNeutral
    show ellisSurprised at ellis_std with hpunch:
        xalign 0.8
    
    e "Next time?!"

    $ energy -= 1
    return