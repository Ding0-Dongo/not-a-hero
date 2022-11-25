label helpKids:
    if commission4Done:
        kid1 "Big Brother Ellis is back!!!!"
        kid2 "Let's play let's playyyyy!!"
        kid3 "Friendship ended with Duck. Ellis is my new best friend."
        $ money += 5
        return
    else:
        "Normington Park, random time afternoon"
        j "aaaaAAH! I'm so glad you guys could make it on such short notice!"
        D "What seems to be the issue, HERO Josephine?"
        j "It's just that... we were tasked with watching over these kids but they are insistent on poking the ducks!"
        kid1 "Playing house is lame but mildly annoying the local wildlife is fun!"
        P "The kids proposed some ideas but..."
        j "Their ideas are more suited towards you, Ellis!"
        e "Huh? What did they want to do?"
        kid1 "Hi, I'm Johnnathaeign and I wanna fight!"
        kid2 "What's up, I'm Joughseph and I want you to be a tree! For science! Science rules!"
        kid3 "My name is Rose and I wish to race."
        e "Why did they introduce themselves like pokAmon NPCs...?"
        j "Welp! Choice is all yours, Ellis!"
        "How do I keep these kids from poking the ducks for an hour...?"
        menu:
            "Go with Johnnathaeign's suggestion and play-fight.":
                kid1 "Alrighty! Let's go!"
                "Johnnathaeign Fortnight dances."
                kid1 "Ok! Ellis, Josephine! You guys are the good guys!"
                kid2 "DELTA and PHI can be the bad guys!"
                kid3 "Let the fight commence."
                j "I'll deal with DELTA, and you deal with PHI! Up and at 'em!"
                "Josephine gets a good aeriel backwards air up-smash neutral footsie off on DELTA."
                P "Fuhahahaha! Think you can defeat me?!"
                P "Come at me with all you've got!"
                if strength < 2:
                    "Ellis feebly punches PHI's palm. PHI does not notice."
                    P "psst psst Ellis c'mon, gimme a good hard smack!"
                    e "I-"
                    P "What's wrong, Ellis?"
                    e "i-i-i'm trying..."
                    "No matter how many times Ellis hits PHI's palm, she simply does not notice."
                    P "Ellis, I can't really hear you..."
                    "Feeling the cold, judgemental eyes that laid on him, Ellis quickly did a 180 and blurts out:"
                    jump comm4BadEnd
                if strength >= 2:
                    "Ellis gives PHI's palm a good hard smack."
                    P "UWAAAAAAAUGH...!"
                    P "Y-You..."
                    P "Got me."
                    "*THUD*"
                    jump comm4GoodEnd
            "Go with Joughseph's suggestion and pretend to be a tree.":
                kid2 "Yayyyyyy!"
                "The moment Ellis climbs onto the monkey bars, the kids start circling under Ellis, chanting... something."
                kid2 "ASHES! ASHES! THEY ALL FALL DOWN!"
                "I dunno sounds kinda demonic to me."
                if stamina < 2:
                    "Ellis attempts to hang on for dear life but-"
                    "Whoops. Butterfingers."
                    j "WATCH OUT!"
                    "DELTA gracefully catches Ellis and sets him down while Josephine and PHI ensure none of the kids are hurt."
                    jump comm4BadEnd
                if stamina >= 2:
                    "Ellis hangs on for dear life as a tree as the kids start chanting yet another... ritual?"
                    kid3 "HUMPTY DUMPTY HAD A HUGE FALL"
                    kid1 "ALL THE KING'S HORSES AND ALL THE KING'S MEN"
                    kid2 "COULD NOT PUT HUMPTY TOGETHER AGAIN!"
                    "Ellis is... hello? Earth to- oh my, he's fainted from shock."
                    jump comm4GoodEnd
            "Go with Rose's suggestion and have a race":
                kid3 "Let us have an honorable battle."
                e "A-Alright! Be warned: I won't go easy on you!"
                P "aaaaand the race is afoot!"
                if speed >= 2:
                    P "Rose starts off strong with a huge lead off Ellis!"
                    j "Woah but what's this?! Ellis is quickly gaining ground!"
                    j "oooooOOOH THEY'RE NECK AND NECK NOW, IT'S ANYONE'S GAME...!"
                    "*TWEEEEEEET*"
                    P "Ellis wins!"
                    e "*pant* *pant* *wheeeze*"
                    kid3 "Again! Again!"
                    kid1 "OOOOOOOO ME NEXT!"
                    e "A-Alrighty! I've still got some fight in me...!"
                    jump comm4GoodEnd
                if speed < 2:
                    P "Rose starts off strong with a huge lead off Ellis!"
                    j "Ellis seems to be uhhh... lagging behind... quite a bit..."
                    P "Oh dear, Ellis is not doing too hot-"
                    "*an excruciating and painful 5 minutes later*"
                    e "*gasp* *wheeze* *gasp* *gasp* *wheeeeeeeeeeeze*"
                    kid3 "Man, you're not very good at using your legs to propel yourself forward using the bodily kinematic motions of your tendons, huh?"
                    e "I- *gasp* wh- HUH?"
                    jump comm4BadEnd

label comm4GoodEnd:
    "A fun filled hour passes by like the blink of an eye and it isn't long before the children's parents come."
    e "W-Whew... I... I survived."
    j "Good job, Ellis! This is one small step for you, one big step for the Association!!"
    e "I-I don't think my progress is representative of the Association as a whole..."
    j "Nonsense!"
    "As Ellis and Josephine keep talking, DELTA and PHI similarly converse about their partners."
    kid1 "H-Hey... Ellis?"
    e "Heya little Johnnathaeign. Why do you seem so sad?"
    kid1 "Will you be back next time?"
    kid2 "I wanna play with Ellis too next time!"
    kid3 "I concur."
    "Ellis looks around to see the patient faces of Josephine, DELTA, and PHI and the puppy-eyed kids and eventually say:"
    e "Yes!"
    $ money += 5
    $ commission4Done = True
    return

label comm4BadEnd:
    "S-Sorry! I-Uh-Um-What I mean to say is- uh- TOILET!"
    "And with that, Ellis runs out of the park."
    #(reload scene)
    "Returning to the park after spending 20 minutes looking for a restroom but ultimately failing to do so and instead awkwardly standing around glancing at his phone every 4 minutes, Ellis sees the kids happy at play, no longer bothering the local duck population."
    e "O-Oh I guess uh the whole thing's resolved..."
    D "That is correct. If there's nothing else, let us be on our way."
    "Glancing backwards one last time, Ellis sees Josephine waving at him."
    j "Next time, you got this!"
    return