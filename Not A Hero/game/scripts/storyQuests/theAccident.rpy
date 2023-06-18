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

    stop music fadeout 3.0

    scene schoolExterior with fade
    show ellisSurprised at ellis_std:
        xalign -1.8

    "Normington Elementary (outside) 02:00 PM"

    show ellisSurprised at ellis_std:
        linear 0.3 xalign 0.5

    "(As Ellis arrives on the scene, huge black plumes of smoke rise up in the air. The school is on fire.)"

    play music panicAudio

    "(Numerous squad cars and ambulances are on the scene. Crying children and worried parents are being reunited in the parking lot.)"
    
    hide ellisSurprised
    show joFrown2 at jo_std:
        xalign 1.8
    show ellisNeutral at ellis_std:
        xalign 0.5
    pause 0.1
    show ellisNeutral at ellis_std:
        linear 0.3 xalign 0.2
    show joFrown2 at jo_std:
        linear 0.3 xalign 0.8

    "(Ellis sees Josephine in the middle of all the chaos.)"

    hide ellisNeutral
    show ellisAsk at ellis_std:
        xalign 0.2

    e "*runs up* Josephine, what's- what's going on?"
    j "*turns to see Ellis with a worried look on her face* Ellis! You're here!"
    j "Desmond and I responded to the call. I've been patching up a few wounded kids. No one's majorly injured, thankfully."

    hide ellisAsk
    show ellisNervous at ellis_std:
        xalign 0.2

    e "*sigh of relief* I'm glad to hear that..."

    hide ellisNervous
    show ellisAsk at ellis_std:
        xalign 0.2
    
    e "*looks over at the burning building* But... where's Desmond?"

    hide joFrown2
    show joNervous at jo_std:
        xalign 0.8
    
    j "*she bites her lip with worry* That's just the thing... he's been going in and out of the school to help people out."
    
    hide ellisAsk
    show ellisSurprised at ellis_std:
        xalign 0.2

    e "*alarmed* Is he still in there?"

    hide ellisSurprised
    show ellisWince at ellis_std:
        xalign 0.2
    
    show schoolExterior with hpunch
    show schoolExterior with hpunch

    "(The two of them wince and cover their ears as an explosion goes off somewhere in the school.)"
    
    hide joNervous
    show joFrown at jo_std:
        xalign 0.8
    
    j "*nods* But I'm almost done with my work here - Ellis, we have to go in and get him out of there."
    
    hide ellisWince
    show ellisNervous at ellis_std:
        xalign 0.2
    
    e "Go in? In to the building? *looks at the smoke apprehensively*"
    
    hide joFrown
    show joClosed at jo_std:
        xalign 0.8
    
    j "You don't have to come if you don't want to, Ellis. I- I understand it sounds crazy."
    e "..."

    hide ellisNervous
    show ellisNeutral at ellis_std:
        xalign 0.2

    e "No, I... I want to come."
    "(The stubbornness in Ellis's voice surprises both Josephine and himself.)"
    
    hide joClosed
    show joFrown at jo_std:
        xalign 0.8
    
    j "... really? Ellis, I..."
    "(Josephine looks like she's about to say more, but stops herself.)"
    j "Right. Just... promise me you'll stay close in that building, okay? We'll watch each other's backs."
    
    hide ellisNeutral
    show ellisAnnoyed2 at ellis_std:
        xalign 0.2
    
    e "*nods*"
    "(The two of them hop the barriers and begin running into the building, despite firemen shouting at them not to go in.)"
    "(Disclaimer: Don't do this.)"
    
    scene schoolInterior with fade
    show joFrown2 at jo_std with dissolve:
        xalign 0.8
    show ellisNervous at ellis_std with dissolve:
        xalign 0.2

    "(In the building, Josephine and Ellis instinctively cover their faces against the heat.)"
    "(It's blazing hot, thick smoke coagulating near the ceilings. Several walls are already streaked with soot.)"
    
    hide ellisNervous
    show ellisSurprised at ellis_std:
        xalign 0.2
    hide joFrown2
    show joNervous at jo_std:
        xalign 0.8
    show schoolInterior with hpunch

    "(A handful of burning ceiling tiles collapse right in front of them with a loud series of snapping and cracking.)"
    
    hide joNervous
    show joFrown2 at jo_std:
        xalign 0.8
    
    "(Ellis sneaks a glance at Josephine. There's fear in her eyes too, but she seems so calm and collected.)"
    
    hide ellisSurprised
    show ellisSad at ellis_std:
        xalign 0.2
    
    e "J-Josephine, it's... the school's so large, how can we find him?"
    "(Josephine begins walking quickly, and Ellis follows after her.)"
    
    hide joFrown2
    show joFrown at jo_std:
        xalign 0.8
    
    j "He wouldn't be in any of the outer classrooms - all the people there evacuated early."
    j "I want to say he's in one of the inner hallways, since I heard the firemen saying some of the rooms had been blocked off by debris."
    
    hide ellisSad
    show ellisNeutral at ellis_std:
        xalign 0.2
    
    e "That... makes sense..."

    hide joFrown
    show joNervous at jo_std:
        xalign 0.8
    
    j "But I haven't been to this school before. I don't... I don't know where the inner rooms would be, Ellis."
    "(Josephine sounds hopeless, and she looks back at the door they'd just come in through.)"
    "(Ellis looks deeper into the depths of the burning school, and presses his lips together tightly.)"
    
    hide ellisNeutral
    show ellisAnnoyed2 at ellis_std:
        xalign 0.2
    
    e "I... I would."

    hide joNervous
    show joFrown at jo_std:
        xalign 0.8
    
    j "*looks surprised* You would?"

    hide ellisAnnoyed2
    show ellisSad at ellis_std:
        xalign 0.2
    
    e "I... I used to go here. Before I started homeschool. I only attended for a few years, but..."
    
    hide ellisSad
    show ellisWince at ellis_std:
        xalign 0.2
    hide joFrown
    show joNervous at jo_std:
        xalign 0.8
    show schoolInterior with hpunch

    "(A part of the wall plaster cracks open near them, and a shower of sparks rises up from it. They quickly step away from the sparks.)"

    hide ellisWince
    show ellisNeutral at ellis_std:
        xalign 0.2
    
    e "We should get moving."

    hide joNervous
    show joFrown2 at jo_std:
        xalign 0.8
    
    j "*nods* Lead the way."
    "(They begin running down the hallway - a quick peek into the classrooms on either side reveals that they had been safely evacuated.)"
    "(It's difficult going - they have to keep pausing to get around assorted piles of debris in the hallway. The walkways are covered in water from the sprinklers.)"
    "(All the while, fire alarms blare and their lights spin rapidly, flashing beams of light in circles.)"
    "(Just being in the building is taking a toll on the two of them.)"

    "(STAMINA CHECK: 6 STAMINA)"

    if stamina > 6:
        "(Stamina Check passed.)"

        hide ellisNeutral
        show ellisAnnoyed at ellis_std:
            xalign 0.2
        
        "(Ellis presses through, unwilling to quit.)"
        "(The two of them continue to work their way through the building, making considerable progress.)"

        show blackScreen with fade
    else:
        "(Stamina Check failed!)"

        hide ellisNeutral
        show ellisSurprised at ellis_std with hpunch:
            xalign 0.2
        hide joFrown2
        show joNervous at jo_std:
            xalign 0.8
        
        "(Ellis nearly trips over an abandoned backpack and falls against the wall, gasping for breath.)"
        
        hide ellisSurprised
        show ellisCringe2 at ellis_std:
            xalign 0.2
        show joNervous at jo_std:
            linear 0.3 xalign 0.5

        j "*helps support him* Ellis!"
        j "*looks worried* Ellis, you're not looking good. I think you should go back."
        e "*coughs* No, I... I have to-"

        hide joNervous
        show joFrown2 at jo_std:
            xalign 0.5
        
        j "Ellis, I'll find him. Just tell me where you think he could be."
        
        show blackScreen with fade
        "(After giving Josephine a rough estimate and a few pointers, Ellis stumbles back out of the school.)"
        "(He is received by the healthcare workers outside and soon, passes out.)"
        jump theEnding
        return

    hide blackScreen with dissolve
    "(Soon, they've made it to the inner halls, and it's just as Josephine said - many have obstructed hallways or blocked classrooms.)"
    
    hide ellisAnnoyed
    show ellisSad at ellis_std:
        xalign 0.2
    
    "(The two of them are slowing down, but they keep moving.)"

    "(SPEED CHECK: 6 SPEED)"

    if speed > 6:
        "(Speed Check passed.)"

        hide ellisSad
        show ellisAnnoyed at ellis_std:
            xalign 0.2

        "(They push their way through the halls, bolstered by each others' confidence.)"
    else:
        "(Speed Check failed!)"

        hide ellisSad
        show ellisWince at ellis_std:
            xalign 0.2
        
        "(Ellis finds himself unable to keep up with Josephine.)"
        j "*slows down* Ellis, are you alright?"
        e "*panting* Yes, I just-"
        
        hide ellisWince
        show ellisSurprised at ellis_std:
            xalign 0.2
        show joNeutral at jo_std:
            linear 0.3 xalign 1.8
        pause(0.01)
        show ellisSurprised at ellis_std with hpunch:
            linear 0.3 xalign 0.5
        
        show schoolInterior with hpunch
        show schoolInterior with hpunch
        "(A huge flaming beam of wood falls from the ceiling, separating the two of them. A wall of fire cuts off their view of each other.)"
        
        hide joNeutral

        e "Josephine? Josephine!"
        j "Ellis, are you okay?"

        hide ellisSurprised
        show ellisCringe2 at ellis_std:
            xalign 0.5

        e "I'm fine, but... I- I don't think I can get to you..."
        j "Ellis, I'll find him. Just tell me where you think he could be."
        
        show blackScreen with fade

        "(After giving Josephine a rough estimate and a few pointers, Ellis stumbles back out of the school.)"
        "(He is received by the healthcare workers outside and soon, passes out.)"
        jump theEnding
        return

    "(They almost pass another room, when Ellis sees a flash of color through the window of a classroom door.)"

    hide ellisAnnoyed
    show ellisSurprised at ellis_std:
        xalign 0.2
    
    e "Wait, I think I saw him!"

    hide joFrown2
    show joExclaim at jo_std:
        xalign 0.8
    
    j "*slows down* Really?" 
    "(The two of them squint through the window.)"

    hide ellisSurprised
    show ellisSad2 at ellis_std:
        xalign 0.2

    j "That's definitely him!"

    hide joExclaim
    show joFrown2 at jo_std:
        xalign 0.8
    
    "(Josephine tries the door handle, but it only wiggles.)"
    j "Stuck... Ellis, I think we'll have to break the door down..."

    hide ellisSad2
    show ellisThinking2 at ellis_std:
        xalign 0.2
    
    e "Let me try..."

    hide joFrown2
    show joNervous at jo_std:
        xalign 0.8
    
    j "Wait, Ellis-"
    "(Josephine steps aside as Ellis takes a few steps back, then rams into the door at full speed.)"
    "(STRENGTH CHECK: 6 STRENGTH)"

    if strength > 6:
        "(Strength Check passed.)"

        call ellisRAM
        pause(0.2)

        scene classroom with fade
        show ellisCringe at ellis_std:
            xalign -0.8
        show joNervous at jo_std:
            xalign -0.8
        
        pause(0.1)

        show ellisCringe at ellis_std:
            linear 0.3 xalign 0.2
        show joNervous at jo_std:
            linear 0.5 xalign 0.8

        "(The door flies open and the two of them immediately rush in.)"
        "(Desmond is unconscious, lying on the floor.)"
        "(Josephine begins checking for a pulse.)"
        e "... is he gonna be OK?"
        "(Josephine is quiet for a moment, then nods.)"

        hide joNervous
        show joFrown at jo_std:
            xalign 0.8
        
        j "He's still alive. We just need to get him out of here. Help me lift him up, Ellis."

        hide ellisCringe
        show ellisSad at ellis_std:
            xalign 0.2
        
        pause(0.1)

        show ellisSad at ellis_std:
            linear 1.0 xalign -0.8
        show joFrown at jo_std:
            linear 1.0 xalign -0.8

        "(The two of them each take one arm and begin helping their friend out.)"

        show blackScreen with fade
        jump theEnding
        return
    else:
        "(Strength Check failed!)"

        call ellisRAM
        
        "(The door doesn't budge, and Ellis knocks himself out.)"

        hide ellisAnnoyed

        "(He barely hears Josephine calling his name with alarm as he goes down.)"

        show blackScreen with fade
        jump theEnding
        return

label ellisRAM:
    hide ellisThinking2
    show ellisAnnoyed at ellis_std:
        xalign 0.2
    pause(0.01)
    show ellisAnnoyed at ellis_std:
        linear 0.3 xalign 0.3
    pause (0.25)
    show ellisAnnoyed at ellis_std:
        linear 0.1 xalign 0.35
    pause(0.2)
    show ellisAnnoyed at ellis_std:
        linear 0.1 xalign -1.5
    pause (0.1)
    show schoolInterior with hpunch