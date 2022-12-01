# day one story quest
# mandatory to be completed first!

label meetTheTeam:
    # need to replace these scenes with the official bgs when we have them

    scene Normington City with fade

    show screen StatUI

    "{i}NORMINGTON ASSOCIATION OF HEROES (OUTSIDE)\n 09:00 AM{/i}"

    # show DELTA at left
    show test1 with moveinleft:
        xalign 0.8
        yalign 1.0

    D "We're here. Are you ready?"

    show ellis Neutral with moveinleft:
        xalign 0.3
        yalign 1.3

    e "... do we have to? I don't really like introductions, or icebreakers, or that kind of thing..."

    menu:
        "C'mon. You'll be fine.":
            D "C'mon. You'll be fine. Besides, you'll have to get used to these kinds of things, now that you're in a TEAM."
        "We can keep it short.":
            D "We can keep it short. They'll understand. But it would be good to know who you're working with."

    e "I know, but still..."

    D "(He seems pretty anxious.)"

    scene Normington Association of Heroes Headquarters with fade

    "{i}NORMINGTON ASSOCIATION OF HEROES (INSIDE)\n 09:00 AM{/i}"

    show ellis Neutral at right with moveinleft:
        yalign 1.3

    # show DELTA at right
    show test1 at left with moveinleft

    e "*looks up at the sign* So... um... the Normington Association of Heroes, huh?"

    D "That's our official name."

    e "... NAH?"

    D "Pardon?"

    e "Is that the abbreviation?"

    hide test1

    show test2 at left

    D "..."

    D "We don't call it that."

    hide test2

    show test1 at left

    e "... *starts laughing*"

    A "DELTA, you're finally here."

    "(Ellis immediately stops laughing.)"

    show ellis Neutral:
        linear 0.3 xpos 0.4
        yalign 1.3

    # show ALPHA at right

    show test3 with moveinright:
        xalign 0.6
        yalign 1.0

    show test4 with moveinright:
        xalign 0.8
        yalign 1.0

    D "(That's ALPHA and PHI, my coworkers, of sorts. Together we mentor a TEAM of HEROs.)"

    P "*smiles warmly* DELTA, you didn't tell us your new HERO was adorable! I'm so jealous!"

    e "*flustered* U-um..."

    menu:
        "Subtly step in":
            D "Knock it off, PHI."
            jump meetTheTeamPartTwo
        "Let Ellis deal with it himself":
            jump meetTheTeamPartTwo

label meetTheTeamPartTwo:

    D "Never mind. Where are your HEROs anyways?"

    P "Upstairs, but they should be down here soon. I already gave them the call."

    P "Why don't we get started with the introductions while we wait?"

    D "Only if Ellis here is okay with it."

    A "So that's his name?"

    A "(ALPHA folds his arms. He's always been straightforward and no-nonsense.)"

    A "My name is ALPHA. I am one of the mentors for your TEAM, though your main mentor will be DELTA, of course."

    A "It's a pleasure to have you as our... replacement in the TEAM."

    "(Ellis's face drops.)"

    e "Re... replacement?"

    hide test3

    show test3 with hpunch:
        xalign 0.6
        yalign 1.0

    "(PHI jabs ALPHA in the ribs.)"

    P "ALPHA, don't say it like that! Don't pay him any mind, Elly."

    P "(She gives me an apologetic smile.)"

    D "It's fine."

    e "(Ellis gives me a curious look.)"

    P "*friendly wave* Anyways, I'm PHI, head mentor of the TEAM! If DELTA or ALPHA can't help you, you can always come to me."

    P "Or if you just want to talk, I'm always available!"

    P "Do you mind if I call you Elly, by the way? Or do you prefer Ellis?"

    e "*shrugs awkwardly*"

    D "(He's rather non-confrontational. I'll have to talk to ALPHA and PHI about this later.)"

    "(A man and woman descend the steps into the lobby. They see the four of us and make their way over.)"

    ### this is going to get messy with just test sprites lol

    show potato with moveinright:
        xalign 0.98
        yalign 1.0
    
    show test2 with moveinright:
        xalign 0.46
        yalign 1.0

    P "You two sure took your time! Join us, join us!"

    j "Sorry, PHI. You know it's a new week, we have to get our assignments in the morning."

    D "(That's Josephine, PHI's HERO. She's been here for only three months, but she's taken to the work rather well.)"

    d "Is he our new TEAMmate?"

    D "(And that's Desmond, ALPHA's HERO. He's been here for almost two years now, if memory serves. But he's climbed the ranks very quickly. Almost on track to become a full-fledged hero come the new year.)"

    P "Mhm! His name's Ellis! Ellis, say hi to your new TEAMmates!"

    e "U-um... 'hi'.... *waves*"

    j "Aw, hi! I think we'll get along just fine! *smiles* I'm excited to go on TEAM missions with you, Ellis!"

    D "Alright, alright. Now that we've gotten the introductions over with..."

    A "Not so fast. You two haven't gotten your commissions for the week yet."

    "(Desmond hands a file folder over to ALPHA. He and Josephine then leave the headquarters, giving a wave to Ellis.)"

    pause(0.5)

    show potato:
        linear 3.6 xpos 1.3
    
    pause(0.23)
    
    show test2:
        linear 3.5 xpos 1.3

    pause(3.1)

    hide potato

    hide test2

    A "*thumbs through the files* Right. I specifically requested the association to give you some easier commissions."

    D "(He hands the folder over to me. I notice Ellis looking at the folder too.)"

    P "So, any questions, either of you?"

    D "(I look over at Ellis.)"

    e "This- this might be a dumb question, but... what exactly does 'TEAM' stand for?"

    "(There's a moment of silence.)"

    e "*tries to explain* I-it's just! I was reading the manual last night, and I, well, I guess I could've missed it, but-"

    P "No no, you're okay! That's what we mentors are here for, answering questions! TEAM stands for 'Team of Entities for All Matters'."

    D "(It looked like it mentally pained her to say that.)"

    e "*in disbelief* That.... that's what it stands for?"

    A "The association is well-known for making rather... inventive acronyms."

    P "You'll get used to it, don't worry. It has basically the same meaning as 'team', anyways."

    e "I- I see... no more questions, thank you."

    D "Ellis, I've got some things to discuss with ALPHA and PHI, could you wait outside?"

    e "Outside? Um, sure."

    show ellis Neutral:
        linear 0.8 xpos -0.3

    "(Ellis leaves.)"

    hide ellis Neutral

    A "*raises an eyebrow* Something wrong, DELTA?"

    D "No, nothing of the sort. I just wanted to let you know something about Ellis."

    D "He's an... introvert, you see. So I don't want you two to push him too hard. Especially you, PHI. Don't tease him."

    "(PHI pretends to be wounded.)"

    P "DELTA, you scoundrel! I would never do anything of the sort!"

    D "{i}PHI.{/i}"

    P "*she grows serious* Yes, yes, DELTA, I understand. I'll hold back."

    A "How do you want us to approach him, then?"

    menu:
        "Invite him to break out of his shell.":
            D "I'd like you two to invite him on more group events. TEAM missions, meetings, that kind of thing."
        "Respect his boundaries.":
            D "I'd like you two to invite him on some group events, but if he doesn't seem comfortable, just leave it be."

    P "Got it. Can do, DELTA!"

    D "(She gives me a mock salute. They're looking at me like a pair of proud parents.)"

    D "... what?"

    P "It's just... it's good to see you back with us, DELTA."

    P "*almost apologetic* After your last HERO and all..."

    A "PHI, we don't need to talk about that right now."

    P "*sighs* You're right, ALPHA. But DELTA, really, we're not just coworkers. We're friends, you know. You can talk to us if you need to."

    "(She gives ALPHA a hard stare, like she's expecting him to say something.)"

    A "... yes, we'll be here for you."

    A "But you should go get started with Ellis. There's a lot of things to get acquainted with."

    D "(I take a quick look at the files.) Just how many commissions did you give us?"

    "(PHI begins walking me towards the door, hands on my shoulders.)"

    show test4:
        linear 2.0 xpos 0.4

    P "You'll be fine! They're simple commissions, nothing you haven't seen before! Go get 'em, tiger!"

    show test1:
        linear 2.2 xpos -0.2

    show test4:
        linear 2.2 xpos 0.2

    pause(0.8)

    show blackScreen with fade

    scene Normington City

    show ellis Neutral with moveinleft:
        xalign 0.3
        yalign 1.3
    
    show test1 with moveinright:
        xalign 0.8
        yalign 1.0

    D "(I'm escorted out of the headquarters before I even have time to protest. As the doors close, Ellis turns to see me.)"

    e "Oh, DELTA? I just realized something."

    D "Hm?"

    e "'Normington Association of Heroes Headquarters'? NAHH?"

    D "*brief smile* We just call it HQ."

    e "(He laughs, but then quickly stops.) Oh, I... I was going to ask you something, too."

    e "What did they mean by 'replacement', by the way? Did... did something happen to your last HERO?"

    hide test1

    show test3:
        xpos 0.7
        yalign 1.0

    D "(...)"

    e "(He quickly backtracks.) If you don't want to talk about it, that's OK. But.... this isn't a dangerous job, is it?"

    D "No, it shouldn't be."

    hide test3

    show test1:
        xpos 0.7
        yalign 1.0

    D "... and thank you."

    e "... for what?"

    D "(I begin heading down the stairs.) We should get started. You're not too worn out by the introductions, right?"

    e "(He quickly begins following me.) No, I... I think I'm OK. They seem like, um, good people."

    D "Don't let PHI bug you. She's very outgoing."

    e "*laughs* I noticed... she reminds me of this third grade teacher I had..."

    show blackScreen with fade

    pause(0.5)

    "Reward: x1 Energy Drink (+[energyDrink] energy)"
    $ energy += energyDrink

    $ story1Done = True
    $ day+= 1

    jump mapScreen