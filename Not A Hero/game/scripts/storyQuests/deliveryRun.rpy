label deliveryRun:
    if energy < 2:
        "(Ellis doesn't have enough energy to do this story quest right now.)"
    else:
        show plaza
        "Downtown Normington"
        "(Ellis is walking around the downtown area of Normington City when he happens upon a familiar person.)"
        e "... Desmond?"
        d "... huh?"
        d "Oh, Ellis, is that you? Didn't recognize you for a second there, sorry. I'm on a commission right now, so I'm busy."
        e "Oh, um, sorry then. I'll just get out of your way."
        d "No, no, it's fine. You know, now might actually be a pretty good time."
        e "Huh? A good time? For what?"
        d "You haven't done a TEAM commission yet, have you?"
        e "*shakes his head*"
        d "Right. Never a better time than the present, then."
        d "TEAM commissions are just commissions you run with your TEAMmates. Maybe not the whole TEAM, but at least one other person."
        d "Got it?"
        e "Uh... I think so."
        d "Any questions, then?"
        e "Are there any... specific rules for TEAM commissions? Are only some commissions TEAM?"
        d "Yeah. I mean, you can't just tag along with someone who's doing a simple thing."
        e "Guess that makes sense..."
        d "If you're not busy, do you feel like helping me out with a few deliveries? It's one of the easier TEAM commissions."

        if stamina < 3:
            e "... um, sorry, I don't think I'm ready for that yet."
            d "Oh? That's a shame. Another day, maybe?"
            e "Sure... I'll see you later, Desmond?"
            d "Yup. Seeya."

            show blackScreen with fade

            "(This story quest requires 3 stamina! Train up and try again!)"
        else:
            e "Sure."
            d "Oh? It's a pretty active commission. Hope you're up for some exercise."
            e "I- I can handle it."
            d "That's good to hear. Just let me know if you need a break, though."
            d "Here, take one of the packages."
            e "(He reaches for one of the largest-looking packages.)"
            d "Wait, not that one-!"
            e "(!!!)"

            show ellisWince with hpunch
            show blackScreen with fade

            "(Ellis and Desmond spend a good while delivering packages. It's tiring, but rewarding work.)"
            "(For his efforts, Ellis gains $10 from the association, as well as a $5 first-time bonus.)"
            "'Delivery' commission unlocked."

            $ money += 15
            $ energy -= 1