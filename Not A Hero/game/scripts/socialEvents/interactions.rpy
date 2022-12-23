#interactions for all the days

label socializeFirst:
    scene hq with fade

    "(DELTA and Ellis are in the headquarters. Ellis is waiting for DELTA to finish up some work before they go out to do some commissions.)"

    show deltaNeutral at delta_std with moveinleft:
        xalign 0.8

    show ellisHesitant at ellis_std with moveinleft:
        xalign 0.3

    e "Hey, DELTA?"
    D "*shuffling through files* Mm?"

    hide ellisHesitant
    show ellisNervous at ellis_std:
        xalign 0.3

    e "*looking at the crowd* I didn't know there were so many... people working for the association."

    hide deltaNeutral
    show deltaInquire at delta_std:
        xalign 0.8

    D "Yeah, we weren't always so popular. Association's been growing as of late, though."
    D "They're thinking on making another branch in the northern part of the city soon. *staples some papers together*"

    hide ellisNervous
    show ellisNeutral at ellis_std:
        xalign 0.3

    
    e "Oh, that's... good?"

    hide deltaInquire
    show deltaHappy at delta_std:
        xalign 0.8

    D "*smiles slightly* You know, if you're bored, you can go talk to one of your fellow HEROs."

    hide ellisNeutral
    show ellisSurprised at ellis_std:
        xalign 0.3

    e "Ah- no, no! I... I'm okay just waiting, really!"
    D "Consider it a challenge while you wait, then. C'mon, don't be a silent protagonist."
    
    hide ellisSurprised 
    show ellisShy at ellis_std:
        xalign 0.3

    e "Silent protag-? *sighs* DELTA, it's just, I... I don't know these people..."

    menu:
        "(Be serious)":
            hide deltaHappy
            show deltaSerious at delta_std:
                xalign 0.8
            
            D "You didn't know me a day before either."

            hide ellisShy
            show ellisNervous at ellis_std:
                xalign 0.3
            
            e "*uncertain* I'm still not sure... DELTA... what if they don't like me?"
            e "I know I'm pretty awkward sometimes... well, all the time, really..."
            hide deltaSerious
            hide ellisNervous

            jump socializeFirstCont
        "(Make a joke)":
            hide deltaHappy
            show deltaTeasing at delta_std:
                xalign 0.8

            D "You can always run back here if they're out to get you."

            hide ellisShy
            show ellisNervous at ellis_std:
                xalign 0.3

            e "Will they be out to get me?"
            jump jokeReply

label jokeReply:
    menu:
        "Yes.":
            D "Yes."
            "(ALPHA happens to pass by and overhear them. He knocks a few knuckles on DELTA's head, without a word.)"
            
            hide deltaTeasing
            show deltaNeutral at delta_std:
                xalign 0.8
            D "Ow. Ok, but honestly..."

            hide deltaNeutral
            hide ellisNervous
            jump socializeFirstCont
        "No.":
            hide deltaTeasing
            show deltaNeutral at delta_std:
                xalign 0.8

            D "No. I was joking."
            D "Sorry. It was a bad joke."

            hide deltaNeutral
            hide ellisNervous
            jump socializeFirstCont

label socializeFirstCont:
    show ellisShy at ellis_std:
        xalign 0.3

    show deltaSerious at delta_std:
        xalign 0.8

    D "Ellis, you're all HEROs here. No one's going to hurt you, and, well, if someone does... literally everyone else here has your back."

    hide deltaSerious
    show deltaNeutral at delta_std:
        xalign 0.8

    D "Think of it like your physical training, alright?"
    D "You'll get better at being around people with time."
    
    hide ellisShy
    show ellisHesitant at ellis_std:
        xalign 0.3
    e "...."

    hide deltaNeutral
    show deltaInquire at delta_std:
        xalign 0.8
    D ".... either way, you don't have anything better to do while you wait."

    hide deltaInquire
    hide ellisHesitant

    "(Ellis protests, but eventually gets up and wanders off into the crowd.)"
    "(Around the time DELTA finishes with his work, Ellis returns, looking a little stressed out.)"

    show deltaNeutral at delta_std with moveinleft:
        xalign 0.8

    show ellisHesitant at ellis_std with moveinleft:
        xalign 0.3

    D "Back so soon?"
    e "Can we... can we go somewhere quiet for a bit?"
    D "Sure. Just let me... *puts a folder back on a shelf* Now we can go."
    show blackScreen with fade

    pause(0.5)

    "Ellis was stressed out by the encounter. (+1 stress)"
    $ stress += 1

label interactionsDayOne:
    "Who do you want to talk to today?"
    menu:
        "Narrator":
            "Why do you want to talk to the narrator?"
            "The narrator didn't say anything."
            "I SAID NOTHING!!!"

        "DELTA":
            D "(He's not what I expected)"
            D "If you have any questions about the HERO program or NAH."
            D "I'll be your mentor. I've got you."

        "PHI":
            P "Welcome to the team, Elly!"
            P "We're the TEAM."
            P "We'll be helping you out with anything you might need."
            P "Yes, there's a different between team and TEAM."
            P "You'll get it!"

        "Josephine":
            j "It's great to have you here, Ellis!"
            j "I know it's a new place and all, so..."
            j "Don't be afraid to reach out!"

        "ALPHA":
            A "It's a pleasure to have you on our team."
            A "I promise you're not a replacement or anything."
            A "By the way, this place has a knack for acronyms."
            A "We have TEAM, HERO... NAH..."
            A "...Did we ever go over NAH?"

        "Desmond":
            d "Hey, Ellis."
            d "I remember when I was in your shoes."
            d "I got you if you want pointers."

        "Raccoon...?":
            sc "hey, kid."
            sc "ive got this shop."
            sc "And ive got the goods."
            sc "hmu"

    return


label interactionsDayTwo:
    "Who do you want to talk to today?"
    menu:
        "DELTA":
            D "How was your first day?"
            D "I know it can be overwhelming."
            D "Just don't forget to take breaks during your training."

        "PHI":
            P "Elly!"
            P "How's it going?"
            P "Y'know, I think DELTA's really glad to have you on the TEAM."
            P "Don't tell him I said that."

        "Josephine":
            j "Have you taken a look at the missions ALPHA put up yet?"
            j "There's quite a bit, but we can do it!"

        "ALPHA":
            A "Have you gotten used to the work around here?"
            A "Don't worry if you haven't, it's all new."
            A "We're all here to help you become a hero!"
            A "hero, not HERO."

        "Desmond":
            d "Josephine wants to go to the park soon."
            d "I'd say I was gonna go, but..."
            d "*He glances at a piece of paper in his hand*"
            d "I guess this can wait."

        "Raccoon":
            sc "hehe, kid, youre going through the whole shindig."
            sc "cant say i envy ya though."

    return

label interactionsDayThree:
    "Who do you want to talk to today?"
    menu:

        "DELTA":
            D "The training here can be pretty relentless sometimes."
            D "Makes it all the more rewarding, I think."
            D "Helping others to become better versions of themselves. Things like that."

        "PHI":
            P "Whoa! Has someone been training?"
            P "It's like three days ago that you've come and joined us!"
            P "And it was three days ago!"

        "Josephine":
            j "It's nice to finally get a breath of fresh air!"
            j "I know this is HERO, and it's literally spelled like hero, but"
            j "it's always nice to get a little me time."
            j "What good can we do if we can't take care of ourselves?"

        "ALPHA":
            A "For upcoming heroes, HAH has assessments."
            A "It's nothing too pressuring. It's to see how far you've gone in training."
            A "I think you should be proud for as far you've gotten."
            A "I'm sure DELTA's proud of you."

        "Desmond":
            d "I've got a couple of commissions lined up for today."
            d "They're not bad. You get used to them."
            d "Though these delivery ones kind of make me feel like I'm in a video game."

        "Raccoon":
            sc "what im doin here?"
            sc "well, ya gotta know how to cater to the crowd."
            sc "need those big bucks"

    return

label interactionsDayFour:
    "Who do you want to talk to today?"
    menu:
        "Narrator":
            "Whoooooshhhh"
            "Just the wind here."
            "Nothing important."

        "DELTA":
            D "I still find it surprising you had a roommate named Ellis."
            D "It makes the data a bit more confusing."
            D "I wonder how they were like."
            D "Not that they'll replace you. You're shaping up to become a good hero, Ellis."

        "PHI":
            P "Goooooood afternoon, Elly!"
            P "You know what we should have here?"
            P "TEAM socials!"
            P "I'd so love to get to know you better!"
            P "Great TEAM-building activity too!"

        "Josephine":
            j "I've been thinking that it'd be a good opportunity for everyone to know first aid."
            j "It can really be a lifesaver in rough situations."
            j "It shouldn't be too bad to teach!"

        "ALPHA":
            A "Now that I'm thinking about it, who names this stuff?"
            A "To name almost everything with canny acronyms..."
            A "That's gotta be a skill!"
            A "Don't worry, we won't be training you in that."
            A "Probably..."

        "Desmond":
            d "How'd your assessment go?"
            d "It's fine if it didn't go as planned."
            d "There's gonna be a next time."

        "Shifty":
            sc "eyyy, i see you got access to that shop."
            sc "my shop."
            sc "ill give you the look around next time."

    return

label interactionsDayFive:
    "Who do you want to talk to today?"
    menu:
        "DELTA":
            D "I see that you've been hanging out with Josephine and Desmond lately."
            D "They've been in this business for a while, and they're always open to help."
            D "Even though you may not work the same as them, you're valuable to the TEAM."
            D "...Thanks, Ellis."

        "PHI":
            P "I've been looking through board games for our social, and I don't know which would be good."
            P "This card game, I think the last time ALPHA played it, he was not having it."
            P "It was really funny! We should play it again."

        "Josephine":
            j "There's still really good coffee place that I wanna take you!"
            j "One of my favorites to just think and relax."
            j "My friend, a coffee addict, introduced it to me."
            j "I am not the coffee addict."

        "ALPHA":
            A "Have you been training regularly?"
            A "It's good to get into the habit of something."
            A "Especially in this line of work."

        "Desmond":
            d "When I first come to HAH, I didn't think I'd be here for so long."
            d "But I like the place and helping other people."
            d "Doesn't feel like it's been two years though."

        "Shifty":
            sc "i got energy drinks."
            sc "i pop those suckers like 100 times a day."
            sc "keeps me up for the job, ya know."

    return

label interactionsDaySix:
    "Who do you want to talk to today?"
    menu:
        "DELTA":
            D "Have you heard the TEAM social PHI wants to do?"
            D "It'll be just us, so don't worry about it being big."
            D "I just think with the games she's choosing, we may be TEAM-breaking rather than TEAM-building."
            D "Don't be afraid to say no when she says something farfetched."
            D "I'm speaking from experience, trust me."

        "PHI":
            P "Elly! I think a thief got one of my card games!"
            P "I don't know how! I had them right in front of me."
            P "I doubt there's a thief that looks like raccoon, right?"
            P "...right?"

        "Josephine":
            j "Hey, Elli, I just wanted to say..."
            j "*She turns away* ..."

        "ALPHA":
            A "As HEROs, you must be able to take care of yourself first."
            A "Your feelings are your own, and you must respect that, as with everyone else."
            A "Do that for your sake."
            A "And also for DELTA's."

        "Desmond":
            d "Hey..."
            d "Take care of yourself, okay?"

        "Shifty":
            sc "just saying"
            sc "i got the energy drinks you need"
            sc "and now board games too."

    return

label interactionsDaySeven:
    "Who do you want to talk to today?"
    menu:
        "DELTA":
            D "Wow, it's already been a whole week!"
            D "I think you are the one meant for this program, Ellis."
            D "You've gone so far already, and you'll go even farther."
            D "I'm proud to call myself your mentor."

        "PHI":
            P "It's been a whole week since you've been here!"
            P "I think that calls for a celebration!"
            P "Is there anything you want?"
            P "Restaurant? Game?"

        "Josephine":
            j "I'm glad you're still here!"
            j "This program isn't made for everyone, but those who go though it are real heroes!"
            j "Heroes and HEROs! There's a difference, but it's not that big in meaning."
            j "I look forward to working with you more!"

        "ALPHA":
            A "How was your first week here?"
            A "Maybe a week just flashed right before your eyes. Maybe not."
            A "You can't discredit the amount of progress you've made though."
            A "You'll get into the swing of things in no time. You've gotten this far."

        "Desmond":
            d "You've gotten through the first week."
            d "It might be the hardest one for all the new members."
            d "So congratulations, it's really nice working with you, TEAMmate."

        "Shifty":
            sc "a whole week?"
            sc "thats more than some people keep going"
            sc "i dunno what you do, but im rooting for you i guess"
            sc "after all, you help the shop."

    return