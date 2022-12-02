label helpGranny:
    if energy < 1:
        "Ellis is too tired to do that right now."
        return
    else:
        if commission5Done:
            e "Again?"
            oldLady "Again."
            D "Agreed."
            cat "*Meows with the exaggerated swagger of a small war criminal*"
            "Haa..."
            $ money += 5
            $ energy -= 1
            return
        else:
            "Normington Hills, 08:00 AM"
            e "D-Delta... why did we have to wake up this early? The association doesn't even open till 9!"
            D "Where there are civilians in need of help, we must answer. There are no excuses to not responding to the needs of the people immediately."
            oldLady "Ohohoho... it's good to rise early, young'uns, for the sunrise grants us energy."
            e "WHERE DID YOU COME FROM?!"
            D "Good morning ma'am. We are here on behalf of the Normington Association of Heroes."
            oldLady "Ah yes, I remember asking for help from you lot."
            oldLady "You see, my cat got stuck on this tree."
            e "You mean the ONE TREE on this entire hill???"
            cat "*Meows with the passion of the holy sunrise*"
            oldLady "Oooooh my poor baby... *sniffle *sniffle"
            D "Well then, Ellis. As the saying goes, \"The floor's all yours\""
            "What should I do?"
            menu:
                "Shake Tree":
                    if strength < 5:
                        "Ellis gently shakes the tree, knocking the cat back and forth before it eventually jumps from the branches onto the arms of the old lady."
                        jump comm5GoodEnd
                    else:
                        "Ellis shakes the tree so hard, the cat stands there, petrified to make any move."
                        jump comm5BadEnd
                "Climb Tree":
                    "Ellis begins climbing the tree when suddenly..."
                    "QUICK! A QTE!"
                    "QUICKLY, ELLIS, PRESS Q!"
                    "...did you press Q?"
                    "Either way, our game is a visual novel so it doesn't matter."
                    jump comm5GoodEnd
                "Lure Cat Down With Food":
                    e "...what do I even have that can lure a cat?"
                    "Delta pulls out a piece of dried squid from his pocket and hands it to Ellis."
                    D "This may come in handy."
                    e "Do you always have stuff like this on-hand-"
                    "*THUD*"
                    "Lo and behold, it worked like a charm."
                    jump comm5GoodEnd

label comm5GoodEnd:
    oldLady "Ohohoho... Thank you, young hero for taking time out of your busy day to help a decrepit old lady like me..."
    e "Decrepit? I wouldn't exactly say-"
    D "Forgive my intrusion ma'am, but my partner, Ellis, is formally known as a HERO, not hero."
    e "...how did you notice the difference??"
    $ money += 5
    $ energy -= 1
    $ commission5Done = True
    return

label comm5BadEnd:
    oldLady "My poor fluffy baby..."
    "Ellis looks down, wishing he could have done more to help."
    D "It's ok. You can try harder next time."
    return