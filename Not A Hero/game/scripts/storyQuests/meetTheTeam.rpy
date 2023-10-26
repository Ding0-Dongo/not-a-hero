# day one story quest
# mandatory to be completed first!

label meetTheTeam:
    scene plaza with fade
    show screen StatUI

    "{i}NORMINGTON ASSOCIATION OF HEROES (OUTSIDE)\n 09:00 AM{/i}"

    # show DELTA at left
    show deltaNeutral at delta_std with moveinleft:
        xalign 0.8

    D "We're here. Are you ready?"

    show ellisNeutral at ellis_std with moveinleft:
        xalign 0.3

    e "... do we have to? I don't really like introductions, or icebreakers, or that kind of thing..."

    hide deltaNeutral
    show deltaClosed at delta_std:
        xalign 0.8

    menu:
        "C'mon. You'll be fine.":
            D "C'mon. You'll be fine. Besides, you'll have to get used to these kinds of things, now that you're in a TEAM."
        "We can keep it short.":
            D "We can keep it short. They'll understand."
            D "But it would be good for you to know who you're working with."

    hide ellisNeutral
    show ellisSad at ellis_std:
        xalign 0.3
    hide deltaClosed
    show deltaNeutral at delta_std:
        xalign 0.8

    e "I know, but still..."
    D "(He seems pretty anxious.)"

    scene hq with fade

    "{i}NORMINGTON ASSOCIATION OF HEROES (INSIDE)\n 09:00 AM{/i}"

    show ellisNeutral at ellis_std with moveinleft:
        xalign 0.8

    # show DELTA at right
    show deltaNeutral at delta_std with moveinleft:
        xalign 0.3

    e "*looks up at the sign* So... um... the Normington Association of Heroes, huh?"
    D "That's our official name, yes."
    e "... NAH?"
    D "Pardon?"

    hide ellisNeutral
    show ellisAsk at ellis_std:
        xalign 0.8
    
    e "Is that the abbreviation?"

    hide deltaNeutral
    show deltaAnnoyed at delta_std:
        xalign 0.3

    D "..."

    hide deltaAnnoyed
    show deltaInquire at delta_std:
        xalign 0.3

    D "We don't call it that."

    hide ellisAsk
    show ellisHappy at ellis_std:
        xalign 0.8

    e "... *starts laughing*"

    hide deltaInquire
    show deltaHappy at delta_std:
        xalign 0.3

    D "..."

    hide deltaHappy
    show deltaNeutral at delta_std:
        xalign 0.3
    
    A "DELTA, you're finally here."

    hide ellisHappy
    show ellisShy at ellis_std:
        xalign 0.8
    
    "(Ellis immediately stops laughing.)"

    show ellisShy at ellis_std:
        linear 0.3 xalign 1.1

    show deltaNeutral at delta_std:
        linear 0.3 xalign 0.7

    show alphaNeutral at alpha_std:
        xalign -0.5

    show alphaNeutral at alpha_std:
        linear 0.3 xalign 0.0

    show phiNeutral at phi_std:
        xalign -0.5

    show phiNeutral at phi_std:
        linear 0.3 xalign 0.3

    D "(That's ALPHA and PHI, my... coworkers, of sorts. Together we mentor a TEAM of HEROs.)"
    
    hide phiNeutral
    show phiOverjoyed at phi_std:
        xalign 0.3
    
    P "*smiles warmly* DELTA, you didn't tell us your new HERO was adorable! I'm so jealous!"

    hide ellisShy
    show ellisNervous at ellis_std:
        xalign 1.1

    e "*flustered* U-um..."

    menu:
        "Subtly step in":
            hide phiOverjoyed
            show phiNeutral at phi_std:
                xalign 0.3
            hide deltaHappy
            show deltaInquire at delta_std:
                xalign 0.7
            D "Knock it off, PHI."
            jump meetTheTeamPartTwo
        "Let Ellis deal with it himself":
            hide phiOverjoyed
            show phiNeutral at phi_std:
                xalign 0.3
            jump meetTheTeamPartTwo

label meetTheTeamPartTwo:
    hide deltaHappy
    show deltaNeutral at delta_std:
        xalign 0.7

    D "Never mind. Where are your HEROs anyways?"

    hide phiNeutral
    show phiHappy at phi_std:
        xalign 0.3
    
    P "Upstairs, but they should be down here soon. I already gave them the call."
    P "Why don't we get started with the introductions while we wait?"
    
    hide phiHappy
    show phiNeutral at phi_std:
        xalign 0.3
    
    hide deltaNeutral
    show deltaInquire at delta_std:
        xalign 0.7
    
    D "Only if Ellis here is okay with it."
    A "So that's his name?"
    A "(ALPHA folds his arms. He's always been straightforward and no-nonsense.)"
    A "My name is ALPHA. I am one of the mentors for your TEAM, though your main mentor will be DELTA, of course."
    A "It's a pleasure to have you as our... replacement in the TEAM."

    hide ellisNervous
    show ellisShy at ellis_std:
        xalign 1.1
    
    "(Ellis's face drops.)"
    e "Re... replacement?"

    hide phiNeutral
    show phiSheepish at phi_std:
        xalign 0.3
    show alphaIndignant at alpha_std with hpunch
    hide phiSheepish
    show phiSheepish at phi_std:
        xalign 0.3

    "(PHI jabs ALPHA in the ribs.)"
    
    hide ellisShy
    show ellisAnnoyed2 at ellis_std:
        xalign 1.1
    
    P "ALPHA, don't say it like that! Don't pay him any mind, Elly."
    P "(She gives me an apologetic smile.)"
    D "It's fine."

    hide alphaIndignant
    show alphaNeutral at alpha_std

    hide ellisAnnoyed2
    show ellisNeutral at ellis_std:
        xalign 1.1

    e "(Ellis gives me a curious look.)"

    hide phiSheepish
    show phiExclaim at phi_std:
        xalign 0.3
    
    P "*friendly wave* Anyways, I'm PHI, head mentor of the TEAM! If DELTA or ALPHA can't help you, you can always come to me."
    P "Or if you just want to talk, I'm always available!"
    
    hide phiExclaim
    show phiHappy at phi_std:
        xalign 0.3
    
    P "Do you mind if I call you Elly, by the way? Or do you prefer Ellis?"

    hide ellisNeutral
    show ellisShy at ellis_std:
        xalign 1.1

    e "*shrugs awkwardly* I... dunno?"

    hide deltaInquire
    show deltaNeutral at delta_std:
        xalign 0.7
    
    D "(... He's rather non-confrontational. I'll have to talk to ALPHA and PHI about this later.)"
    "(A man and woman descend the steps into the lobby. They see the four of us and make their way over.)"

    show ellisShy at ellis_std:
        linear 0.3 xalign 1.5
    hide ellisShy

    show deltaNeutral at delta_std:
        linear 0.3 xalign 1.5
    hide deltaNeutral

    show alphaNeutral at alpha_std:
        linear 0.3 xalign 1.5
    hide alphaNeutral

    show phiHappy at phi_std:
        linear 0.3 xalign 1.0
    
    show desNeutral at ellis_std:
        xalign -0.5
    show desNeutral at ellis_std:
        linear 0.3 xalign 0.5
    
    show joNeutral at jo_std:
        xalign -0.5
    show joNeutral at jo_std:
        linear 0.3 xalign 0.0


    P "You two sure took your time! Join us, join us!"

    hide joNeutral
    show joClosed at jo_std:
        xalign 0.0

    j "Sorry, PHI. You know it's a new week, we have to get our assignments in the morning."
    D "(That's Josephine, PHI's HERO. She's been here for only three months, but she's taken to the work rather well.)"

    hide desNeutral
    show desChuckle at ellis_std:
        xalign 0.5

    d "Is he our new TEAMmate?"
    D "(And that's Desmond, ALPHA's HERO. He's been here for almost two years now, if memory serves. But he's climbed the ranks very quickly. Almost on track to become a full-fledged hero come the new year.)"
    P "Mhm! His name's Ellis! Ellis, say hi to your new TEAMmates!"

    show phiHappy at phi_std:
        linear 0.3 xalign 1.5
    pause(0.3)
    hide phiHappy

    show ellisNeutral at ellis_std:
        xalign 1.5
    show ellisNeutral at ellis_std:
        linear 0.3 xalign 1.0

    e "U-um... 'hi'.... *waves*"

    hide joClosed
    show joNeutral at jo_std:
        xalign 0.0
    
    j "Aw, hi! I think we'll get along just fine! *smiles* I'm excited to go on TEAM missions with you, Ellis!"
    
    show joNeutral at jo_std:
        linear 0.3 xalign -0.5
    show desChuckle at ellis_std:
        linear 0.3 xalign -0.5
    pause(0.3)
    hide desChuckle
    hide joNeutral


    show deltaNeutral at delta_std:
        xalign 1.5
    show deltaNeutral at delta_std:
        linear 0.3 xalign 0.2
    
    show ellisNeutral at ellis_std:
        linear 0.3 xalign 0.8

    D "Alright, alright. Now that we've gotten the introductions over with..."
    
    show deltaNeutral at delta_std:
        linear 0.3 xalign 0.5
    
    show ellisNeutral at ellis_std:
        linear 0.3 xalign 1.0
    
    show alphaNeutral at alpha_std:
        xalign -0.5
    show alphaNeutral at alpha_std:
        linear 0.3 xalign 0.0

    A "Not so fast. You two haven't gotten your commissions for the week yet."
    "(Desmond hands a file folder over to ALPHA. He and Josephine then leave the headquarters, giving a wave to Ellis.)"
    A "*thumbs through the files* Right. I specifically requested the association to give you some easier commissions."
    D "(He hands the folder over to me. I notice Ellis looking at the folder too.)"

    show ellisNeutral at ellis_std:
        linear 0.3 xalign 1.1
    show deltaNeutral at delta_std:
        linear 0.3 xalign 0.7
    
    show phiNeutral at phi_std:
        xalign 1.5
    show phiNeutral at phi_std:
        linear 0.3 xalign 0.3
    
    show alphaNeutral at alpha_std:
        linear 0.3 xalign 0.0

    P "So, any questions, either of you?"
    D "(I look over at Ellis.)"

    hide ellisNeutral
    show ellisAsk at ellis_std:
        xalign 1.1

    e "This- this might be a dumb question, but... what exactly does 'TEAM' stand for?"
    "(There's a moment of silence.)"

    hide ellisAsk
    show ellisSad2 at ellis_std:
        xalign 1.1

    e "*tries to explain* I-it's just! I was reading the manual last night, and I, well, I guess I could've missed it, but-"
    
    hide phiNeutral
    show phiSheepish at phi_std:
        xalign 0.3
    P "No no, you're okay! That's what we mentors are here for, answering questions! TEAM stands for 'Team of Entities for All Matters'."
    
    hide deltaNeutral
    show deltaAnnoyed at delta_std:
        xalign 0.7

    D "(It looked like it mentally pained her to say that.)"

    hide ellisSad2
    show ellisSurprised at ellis_std:
        xalign 1.1

    e "*in disbelief* That.... that's what it stands for?"

    hide alphaAnnoyed
    show alphaNeutral at alpha_std


    A "The association is well-known for making rather... inventive acronyms."
    P "You'll get used to it, don't worry. It has basically the same meaning as 'team', anyways."

    hide ellisSurprised
    show ellisNeutral at ellis_std:
        xalign 1.1

    e "I- I see... no more questions, thank you."

    hide deltaAnnoyed
    show deltaInquire at delta_std:
        xalign 0.7

    D "Ellis, I've got some things to discuss with ALPHA and PHI, could you wait outside?"
    
    hide phiSheepish
    show phiNeutral at phi_std:
        xalign 0.3
    hide deltaInquire
    show deltaNeutral at delta_std:
        xalign 0.7
    
    e "Outside? Um, sure."

    show ellisNeutral at ellis_std:
        linear 0.8 xpos 1.5
    hide ellis Neutral

    show deltaNeutral at delta_std:
        linear 0.3 xalign 1.0
    
    show phiNeutral at phi_std:
        linear 0.3 xalign 0.5

    "(Ellis leaves.)"
    A "*raises an eyebrow* Something wrong, DELTA?"

    hide deltaNeutral
    show deltaInquire at delta_std:
        xalign 1.0

    D "No, nothing of the sort. I just wanted to let you know something about Ellis."
    D "He's an... introvert, you see. So I don't want you two to push him too hard. Especially you, PHI. Don't tease him."
    
    hide phiNeutral
    show phiFrown at phi_std:
        xalign 0.5
    
    "(PHI pretends to be wounded.)"
    P "DELTA, you scoundrel! I would never do anything of the sort!"

    hide deltaInquire
    show deltaAnnoyed at delta_std:
        xalign 1.0

    D "{i}PHI.{/i}"

    hide phiFrown
    show phiHappy at phi_std:
        xalign 0.5
    
    P "*she grows serious* Yes, yes, DELTA, I understand. I'll hold back."

    hide deltaAnnoyed
    show deltaNeutral at delta_std:
        xalign 1.0

    A "How do you want us to approach him, then?"

    hide deltaNeutral
    show deltaInquire at delta_std:
        xalign 1.0

    menu:
        "Invite him to break out of his shell.":
            D "I'd like you two to invite him on more group events. TEAM missions, meetings, that kind of thing."
        "Respect his boundaries.":
            D "I'd like you two to invite him on some group events, but if he doesn't seem comfortable, just leave it be."

    hide deltaInquire
    show deltaNeutral at delta_std:
        xalign 1.0

    hide alphaNeutral
    show alphaShySmile at alpha_std

    P "Got it. Can do, DELTA!"
    D "(She gives me a mock salute. They're looking at me like a pair of proud parents.)"

    hide deltaNeutral
    show deltaInquire at delta_std:
        xalign 1.0

    D "... what?"

    hide deltaInquire
    show deltaNeutral at delta_std:
        xalign 1.0

    hide phiHappy
    show phiSheepish at phi_std:
        xalign 0.5

    P "It's just... it's good to see you back with us, DELTA."
    P "*almost apologetic* After your last HERO and all..."

    hide alphaShySmile
    show alphaAnnoyed at alpha_std

    A "PHI, we don't need to talk about that right now."
    P "*sighs* You're right, ALPHA. But DELTA, really, we're not just coworkers. We're friends, you know. You can talk to us if you need to."
    
    hide phiSheepish
    show phiNeutral at phi_std:
        xalign 0.5
    
    "(She gives ALPHA a hard stare, like she's expecting him to say something.)"

    hide alphaAnnoyed
    show alphaShySmile at alpha_std

    A "... yes, we'll be here for you."

    hide alphaShySmile
    show alphaNeutral at alpha_std

    A "But you should go get started with Ellis. There's a lot of things to get acquainted with."

    hide deltaNeutral
    show deltaAnnoyed at delta_std:
        xalign 1.0
    hide phiNeutral
    show phiHappy at phi_std:
        xalign 0.5

    D "(I take a quick look at the files.) Just how many commissions did you give us?"
    "(PHI begins walking me towards the door, hands on my shoulders.)"
    
    show deltaAnnoyed at delta_std:
        linear 1.0 xalign 1.5
    show phiHappy at phi_std:
        linear 1.0 xalign 1.5
    
    pause(1.0)
    
    hide deltaAnnoyed
    hide phiHappy

    P "You'll be fine! They're simple commissions, nothing you haven't seen before! Go get 'em, tiger!"

    show blackScreen with fade

    scene plaza

    show ellisNeutral at ellis_std:
        xalign 0.8

    show deltaAnnoyed at delta_std:
        xalign -0.5
    show deltaAnnoyed at delta_std:
        linear 0.3 xalign 0.2

    D "(I'm escorted out of the headquarters before I even have time to protest. As the doors close, Ellis turns to see me.)"
    
    hide ellisNeutral
    show ellisAsk at ellis_std:
        xalign 0.8

    e "Oh, DELTA? I just realized something."

    hide deltaAnnoyed
    show deltaNeutral at delta_std:
        xalign 0.2

    D "Hm?"
    e "'Normington Association of Heroes Headquarters'? NAHH?"

    hide deltaNeutral
    show deltaHappy at delta_std:
        xalign 0.2
    
    D "*brief smile* We just call it HQ."

    hide ellisAsk
    show ellisHappy at ellis_std:
        xalign 0.8

    e "(He laughs, but then quickly stops.) Oh, I... I was going to ask you something, too."

    hide ellisHappy
    show ellisNeutral at ellis_std:
        xalign 0.8

    e "What did they mean by 'replacement', by the way? Did... did something happen to your last HERO?"
    
    hide deltaHappy
    show deltaSerious at delta_std:
        xalign 0.2

    D "(...)"

    hide ellisNeutral
    show ellisAnnoyed2 at ellis_std:
        xalign 0.8

    e "(He quickly backtracks.) If you don't want to talk about it, that's OK. But.... this isn't a dangerous job, is it?"
    D "No, it shouldn't be."
    D "..."

    hide deltaSerious
    show deltaNeutral at delta_std:
        xalign 0.2

    D "... and thank you."

    hide ellisAnnoyed2
    show ellisNeutral at ellis_std:
        xalign 0.8

    e "... for what?"
    D "(I begin heading down the stairs.) We should get started. You're not too worn out by the introductions, right?"
    e "(He quickly begins following me.) No, I... I think I'm OK. They seem like, um, good people."

    hide deltaNeutral
    show deltaInquire at delta_std:
        xalign 0.2

    D "Don't let PHI bug you. She's very outgoing."

    hide ellisNeutral
    show ellisHappy at ellis_std:
        xalign 0.8

    e "*laughs* I noticed... she reminds me of this third grade teacher I had..."

    show blackScreen with fade

    pause(0.5)

    "Reward: x1 Energy Drink (+[energyDrink] energy)"
    $ energy += energyDrink

    $ story1Done = True
    $ day+= 1

    jump mapScreen