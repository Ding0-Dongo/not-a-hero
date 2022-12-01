label theAccident:

    #test code
    # "stamina?"
    # menu:
    #     "up":
    #         $ stamina = 7
    #     "stay":
    #         "stamina did not change"

    # "speed?"
    # menu:
    #     "up":
    #         $ speed = 7
    #     "stay":
    #         "speed did not change"

    # "strength?"
    # menu:
    #     "up":
    #         $ strength = 7
    #     "stay":
    #         "strength did not change"

    #Day 7
    #Scene: City

    "Normington Elementary (outside) 02:00 PM"
    "(As Ellis arrives on the scene, huge black plumes of smoke rise up in the air. The school is on fire.)"
    "(Numerous squad cars and ambulances are on the scene. Crying children and worried parents are being reunited in the parking lot.)"
    "(Ellis sees Josephine in the middle of all the chaos.)"
    e "*runs up* Josephine, what's- what's going on?"
    j "*turns to see Ellis with a worried look on her face* Ellis! You're here!"
    j "Desmond and I responded to the call. I've been patching up a few wounded kids. No one's majorly injured, thankfully."

    e "*sigh of relief* I'm glad to hear that..."
    e "*looks over at the burning building* But... where's Desmond?"
    j "*she bites her lip with worry* That's just the thing... he's been going in and out of the school to help people out."
    e "*alarmed* Is he still in there?"
    #(screenshake)
    "(The two of them wince and cover their ears as an explosion goes off somewhere in the school.)"
    j "*nods* But I'm almost done with my work here - Ellis, we have to go in and get him out of there."
    e "Go in? In to the building? *looks at the smoke apprehensively*
"
    j "You don't have to come if you don't want to, Ellis. I- I understand it sounds crazy."
    e "No, I... I want to come."
    "(The stubbornness in Ellis's voice surprises both Josephine and himself.)"
    j "... really? Ellis, I..."
    "(Josephine looks like she's about to say more, but stops herself.)"
    j "Right. Just... promise me you'll stay close in that building, okay? We'll watch each other's backs."
    e "*nods*"
    "(The two of them hop the barriers and begin running into the building, despite firemen shouting at them not to go in.)"

    "(Disclaimer: Don't do this.)"
    "(In the building, Josephine and Ellis instinctively cover their faces against the heat.)"
    "(It's blazing hot, thick smoke coagulating near the ceilings. Several walls are already streaked with soot.)"
    #(screenshake)
    "(A handful of burning ceiling tiles collapse right in front of them with a loud series of snapping and cracking.)"
    "(Ellis sneaks a glance at Josephine. There's fear in her eyes too, but she seems so calm and collected.)"
    e "J-Josephine, it's... the... the school's so large, how can we find him?"
    "(Josephine begins walking quickly, and Ellis follows after her.)"
    j "He wouldn't be in any of the outer classrooms - all the people there evacuated early."

    j "I want to say he's in one of the inner hallways, since I heard the firemen saying some of the rooms had been blocked off by debris."
    e "That... makes sense..."
    j "But I haven't been to this school before. I don't... I don't know where the inner rooms would be, Ellis."
    "(Josephine sounds hopeless, and she looks back at the door they'd just come in through.)"
    "(Ellis looks deeper into the depths of the burning school, and presses his lips together tightly.)"
    e "I... I would."
    j "*looks surprised* You would?"
    e "I... I used to go here. Before I started homeschool. I only attended for a few years, but..."
    "(A part of the wall plaster cracks open near them, and a shower of sparks rises up from it. They quickly step away from the sparks.)"

    e "We should get moving."
    j "*nods* Lead the way."
    "(They begin running down the hallway - a quick peek into the classrooms on either side reveals that they had been safely evacuated.)"
    "(It's difficult going - they have to keep pausing to get around assorted piles of debris in the hallway. The walkways are covered in water from the sprinklers.)"
    "(All the while, fire alarms blare and their lights spin rapidly, flashing beams of light in circles.)"
    "(Just being in the building is taking a toll on the two of them.)"

    "(STAMINA CHECK)"

    if stamina > 6:
        "(Stamina Check passed)"
        "(Ellis presses through, unwilling to quit.)"
        "(The two of them continue to work their way through the building, making considerable progress.)"
    else:
        "(Stamina Check failed)"
        "(Ellis nearly trips over an abandoned backpack and falls against the wall, gasping for breath.)"
        j "*helps support him* Ellis!"
        j "*looks worried* Ellis, you're not looking good. I think you should go back."
        e "*coughs* No, I... I have to-"
        j "Ellis, I'll find him. Just tell me where you think he could be."
        "(After giving Josephine a rough estimate and a few pointers, Ellis stumbles back out of the school.)"
        "(He is received by the healthcare workers outside and soon, passes out.)"
        #(fade to black)
        jump theEnding


    "(Soon, they've made it to the inner halls, and it's just as Josephine said - many have obstructed hallways or blocked classrooms.)"
    "(The two of them are slowing down, but they keep moving.)"

    "(SPEED CHECK)"

    if speed > 6:
        "(Speed Check passed)"
        "(They push their way through the halls, bolstered by each others' confidence.)"
    else:
        "(Speed Check failed)"
        "(Ellis finds himself unable to keep up with Josephine.)"
        j "*slows down* Ellis, are you alright?"
        "*panting* Yes, I just-"
        #(screenshake)
        "(A huge flaming beam of wood falls from the ceiling, separating the two of them. A wall of fire cuts off their view of each other.)"
        e "Josephine? Josephine!"
        j "Ellis, are you okay?"
        e "I'm fine, but... I- I don't think I can get to you..."
        j "Ellis, I'll find him. Just tell me where you think he could be."
        "(After giving Josephine a rough estimate and a few pointers, Ellis stumbles back out of the school.)"
        "(He is received by the healthcare workers outside and soon, passes out.)"
        #(fade to black)
        jump theEnding

    "(They almost pass another room, when Ellis sees a flash of color through the window of a classroom door.)"
    e "Wait, I think I saw him!"
    j "*slows down* Really?" 
    "(The two of them squint through the window.)"
    j "That's definitely him!"
    "(Josephine tries the door handle, but it only wiggles.)"
    j "Stuck... Ellis, I think we'll have to break the door down..."

    "(STRENGTH CHECK)"

    "Let me try..."
    "(Josephine steps aside as Ellis takes a few steps back, then rams into the door at full speed.)"

    if strength > 6:
        "(Strength Check passed)"
        "(The door flies open and the two of them immediately rush in.)"
        "(Desmond is unconscious, lying on the floor.)"
        "(Josephine begins checking for a pulse.)"
        e "... is he gonna be OK?"
        "(Josephine is quiet for a moment, then nods.)"
        j "He's still alive. We just need to get him out of here. Help me lift him up, Ellis."
        "(The two of them each take one arm and begin helping their friend out.)"
        #(fade to black)
        jump theEnding
    else:
        "(Strength Check failed)"
        "(The door doesn't budge, and Ellis knocks himself out.)"
        "(He barely hears Josephine calling his name with alarm as he goes down.)"
        #(fade to black)
        jump theEnding
