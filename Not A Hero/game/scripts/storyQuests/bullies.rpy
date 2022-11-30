label bullies:
    # scene: school
    show schoolExterior
    "Normington Elementary"
#    show ellisNeutral
    "(Near the elementary school, Ellis sees something strange going on...)"
    "(It looks like a group of children gathered around another child. They seem to be shouting some unkind things.)"
#    show ellisSad
    e "(Great... bullies... they used to be my worst nightmare...)"
    "(Ellis gulps as he watches the children continue shouting at the other child.)"
    e "..."
#    show ellisAnnoyed2
    e "(I'm not even the one getting bullied right now... why am I getting so nervous?!)"

    menu:
        "Get involved":
            "(Ellis gently shakes the school fence to get the kids' attention.)"
            e "Hey, what's going on here?"
            "(The kids look up.)"
            kids "Who are you?"
            miscChild "We're not supposed to talk to strangers."
            e "Um... well, I'm- I'm pretty sure you're not supposed to bully other kids, either."
            kids "*visibly nervous* We're not bullying anyone!"
            e "Then what's going on here?"
            bully "He stole my pencil!"
            e "*looks at the other child* Did you take his pencil?"
            bulliedChild "*almost in tears* No, I swear I didn't! I gave it back to him after class!"
            bully "Liar!"
            e "Hey, you- you don't know if he's lying yet."
            "(Ellis sees a recess monitor looking up and frowning at him. He realizes talking to children at a school gate probably isn't the best move.)"
            e "Sorry, I- I'll be right back."
            "(Ellis goes to the office of the school to check in as a visitor.)"
            "(He finds his way over to the playground and returns to the children.)"
            e "So, um, hi. My name's Ellis, by the way. *gestures to visitor's badge*"
            kids "*monotone* Hi, Mr. Ellis..."
            "(The children don't look ready to trust him yet.)"
            e "Where... where did you last see the pencil?"
            bulliedChild "I gave it back to him in class... I don't know what happened to it after that, I swear!"
            e "And where's your class?"
            bulliedChild "206..."
            e "OK. How's this sound? We'll... we'll go to classroom 206, and we'll see if we can find the pencil."
            "(The kids murmur a consensus.)"
            e "Alright, lead the way, then."
            "(After a short walk, the small group arrives in the classroom.)"
            
            #show classroom

            "(The teacher is at her desk. She looks up and adjusts her glasses, then smiles.)"
            teacher "Oh, hello! Are you here to pick up one of the children?"
            e "*flushes* Wh-what? No, I'm... I'm not anyone's parent, I'm just... visiting! Visiting... (Do I look that old?!)"
            teacher "*gets up and walks over* Well, then, how can I help you? You don't look like a member of the school board..."
            miscChild "Mr. Ellis is helping us find a pencil!"
            teacher "*amused* Oh? Well, don't let me stop you, then. *returns to her desk*"
            "(After a lengthy search, the pencil is finally found on the floor, behind the leg of a desk.)"
            "(It's not an ordinary yellow pencil, instead, a pencil with cars printed on bright plastic. Perhaps of sentimental value.)"
            "(The owner is happily reunited with it, and the issue seems to be resolved.)"
            teacher "Now, children, what do we say when we've wronged someone?"
            bully "... sorry for calling you a liar and saying you stole my pencil."
            bulliedChild "Sorry I didn't give you your pencil back in person."
            bulliedChild "I feel like we could have avoided this..."
            bully "... yeah..."
            "(The children quickly make up to each other and run back out to the playground to catch the last few minutes of recess. They wave cheerful goodbyes.)"
            teacher "You know, 'Mr. Ellis', was it?"
            e "Huh? Oh, yeah, that's... that's me. You can just call me Ellis, though. *laughs nervously*"
            teacher "Are you part of our anti-bullying campaign?"
            e "Uh... haven't heard of it before, I think. (That's a thing now?)"
            teacher "*surprised* Really? I'd suggest you give it a try. You handled the situation so well."
            teacher "*sees his hesitation* Oh, it's nothing official! Just volunteers that sometimes come in and act as mediators for the kids."
            teacher "Mediation usually takes place in the library, and any children with disagreements or problems come in."
            teacher "It's been going pretty successfully so far. Administration was thinking on introducing it to the middle and high schools soon."
            e "I- I think I'd rather keep working with the younger kids. I'm... not sure I'd do so well with the older ones."
            e "*embarrassed* I'm just a little nervous around people my age."
            teacher "*nods* Oh, no problem! I completely understand."
            teacher "But is that a yes? Are you joining the campaign?"
            e "Ah... I... I guess...? (I don't really think I can say no...)"
            teacher "*smiles* I'm so glad to hear that. Thank you so much, Ellis."
            e "Oh, it's nothing. (What have I gotten myself into...)"
            "(Ellis leaves the school, in a state of awe.)"
            e "(Maybe it won't be so bad, though?)"

            show blackScreen with fade

            "Ellis was stressed out by the encounter."
            $ stress += 2
            $ social += 2
            "'Mediation' social event unlocked."

            $ bulliesDone = True

        "Keep your head down":
            e "(I'd rather not get involved in this...)"
            "(Ellis quickly looks down at the sidewalk and walks away from the school.)"
            
            show blackScreen with fade