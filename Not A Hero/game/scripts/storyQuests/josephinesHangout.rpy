### DAY 2
# Optional Story Quest

#scene = city

label jhrStart:
    scene plaza with fade

    show screen StatUI

    "NORMINGTON ASSOCIATION OF HEROES HEADQUARTERS (Outside)"

    show ellisNeutral at ellis_std with dissolve:
        xalign 0.55

    show joNeutral at jo_std with dissolve:
        xalign 1.1

    pause(0.8)

    show desNeutral at ellis_std with moveinleft:
        xalign -0.05

    d "You wanted to meet up, Josephine?"

    hide joNeutral
    show joExclaim at jo_std:
        xalign 1.1

    j "Yeah!"

    hide desNeutral

    show desDrowsy at ellis_std:
        xalign -0.05

    d "*gestures at Ellis* Well, we're both here, so..."

    hide joExclaim
    show joFrown at jo_std:
        xalign 1.1

    j "I was just thinking... since Ellis is new, and we haven't been able to properly get to know him... we could go for a walk in the park! You two are free, right?"

    hide desDrowsy

    show desChuckle at ellis_std:
        xalign -0.05

    d "*shrugs* Free enough, I get."

    hide ellisNeutral

    show ellisNervous at ellis_std:
        xalign 0.55

    e "U-um... yeah, I... I'm free."

    hide joFrown
    show joExclaim at jo_std:
        xalign 1.1

    j "*beams* Great! C'mon, let's go!"

    show blackScreen with fade

    "10 minutes later"

    pause (0.8)

    scene park with dissolve

    show screen StatUI

    "NORMINGTON PARK"

    "Normington Park is picturesque at this time of day, the sun shining down over it like a blessing. A fountain pours endlessly in the center of a long curved pathway of crushed gravel that winds through the park."

    "Flowering trees provide some welcome shade overhead, and a light breeze sends leaves and petals fluttering down. Some children with a kite run past the trio as they step onto the path."

    show ellisNeutral at ellis_std with moveinright:
        xalign 0.55

    show joNeutral at jo_std with moveinright:
        xalign 1.1
    
    show desNeutral at ellis_std with moveinright:
        xalign -0.05

    hide joNeutral
    show joClosed at jo_std:
        xalign 1.1
    
    j "Great weather for a walk, isn't it."

    hide desNeutral

    show desChuckle at ellis_std:
        xalign -0.05

    d "Eh, we got lucky. Forecast said it was going to rain today."

    hide desChuckle

    show desNeutral at ellis_std:
        xalign -0.05

    hide joClosed
    show joFrown2 at jo_std:
        xalign 1.1

    j "I was wondering why you brought an umbrella to HQ this morning..."

    hide joFrown2
    show joClosed at jo_std:
        xalign 1.1

    j "*clasps her hands together* So! Ellis, what made you want to be a HERO?"

    hide ellisNeutral

    show ellisNervous at ellis_std:
        xalign 0.55

    e "Um... well..."

    hide joClosed
    show joExclaim at jo_std:
        xalign 1.1

    j "Was it the prestige? The sense of helping your community? The pretty and friendly android mentors?"

    menu:
        "Make something up":
            jump jhrMakeUp
        "Tell the truth":
            jump jhrTellTruth

label jhrMakeUp:
    hide ellisNervous

    show ellisCringe at ellis_std:
        xalign 0.55 

    e "Y-yeah! That- that last one. (What did she say again?)"

    hide joExclaim
    show joClosed at jo_std:
        xalign 1.1

    j "Oooh- haha! Wouldn't have expected that from you, Ellis"

    hide ellisCringe

    show ellisNervous at ellis_std:
        xalign 0.55

    e "*flushes* (Did I say something wrong?)"

    hide desNeutral
    show desFrown at ellis_std:
        xalign -0.05

    d "{i}Josephine.{\i}"

    hide joClosed
    show joNeutral at jo_std:
        xalign 1.1

    j "*laughs* I'm kidding, I'm kidding! Yeah... we can't date any of the androids... It's against policy. Really is a shame though-- some of the androids working at the association really are cute."

    hide ellisNervous

    show ellisSurprised at ellis_std:
        xalign 0.55

    e "(D-date?!)"

    hide ellisSurprised
    hide desFrown
    hide joNeutral

    jump jhrCont

label jhrTellTruth:
    hide ellisNervous

    show ellisThinking at ellis_std:
        xalign 0.55

    e "Actually, it was... kind of an accident."

    hide desNeutral
    show desFrown at ellis_std:
        xalign -0.05

    d "An accident?"

    hide ellisThinking

    show ellisNervous at ellis_std:
        xalign 0.55

    e "It's not really that interesting... You're not going to believe this, but I used to be roommates with another guy named Ellis."

    hide joExclaim
    show joNeutral at jo_std:
        xalign 1.1

    j "*eyes widen* For real? Ellis, you've either seen everything, or nothing fazes you."

    hide ellisNervous

    show ellisHappy at ellis_std:
        xalign 0.55

    e "*laughs* I'm pretty sure the association was looking for him, but... he kind of moved out on short notice."

    hide desFrown
    show desNeutral at ellis_std:
        xalign -0.05

    d "Why did you take the job then?"

    hide ellisHappy
    hide desNeutral
    hide joNeutral

    jump jhrCont

label jhrCont:

    show ellisAnnoyed at ellis_std:
        xalign 0.55

    show desNeutral at ellis_std:
        xalign -0.05

    show joNeutral at jo_std:
        xalign 1.1

    e "*helplessly* I don't know."

    e "DELTA seemed really surprised too, and he asked me to give him a week while the association figured something out."

    hide ellisAnnoyed

    show ellisThinking2 at ellis_std:
        xalign 0.55

    e "I guess... I guess I would've felt bad if I just left him hanging."

    hide desNeutral
    show desDrowsy at ellis_std:
        xalign -0.05

    d "That's pretty generous of you."

    hide desDrowsy
    show desNeutral at ellis_std:
        xalign -0.05

    d "Are you going to stay being a HERO then? Of you weren't the one signing up for the job in the first place, I mean..."

    menu:
        "Yeah":
            jump jhrYes
        "I don't know":
            jump jhrNo

label jhrYes:
    hide ellisThinking2

    show ellisNervous at ellis_std:
        xalign 0.55

    e "Yeah, I... I think so."

    e "I can't explain it, but being a HERO... even if it's only been a day or two, I feel like this is helping me as much as it's helping others."

    hide joNeutral
    show joExclaim at jo_std:
        xalign 1.1

    j "Oh? Some kind of epic quest of self-improvement?"

    hide ellisNervous

    show ellisCringe at ellis_std:
        xalign 0.55

    e "Aha... ha... um... kind of?"

    hide ellisCringe

    hide joExclaim

    jump jhrCont2

label jhrNo:
    hide ellisThinking2

    show ellisThinking at ellis_std:
        xalign 0.55

    e "I don't know. I'm still thinking about it. I mean, I haven't been doing this for a week yet, even."

    hide desNeutral
    show desChuckle at ellis_std:
        xalign -0.05

    d " That's fair. Not everyone stays. Usually most people decide whether or not they want to keep doing this after a week or two."

    hide joExclaim
    show joClosed at jo_std:
        xalign 1.1

    j "Awww. Well, I hope we can convince you to stay, Ellis. You seem like a good guy to work with. *smiles*"

    hide ellisThinking

    show ellisNervous at ellis_std:
        xalign 0.55

    e "*flushes* Th-thanks."

    hide ellisNervous

    hide desChuckle

    hide joClosed

    jump jhrCont2

label jhrCont2:

    show ellisNeutral at ellis_std:
        xalign 0.55

    show desNeutral at ellis_std:
        xalign -0.05

    show joNeutral at jo_std:
        xalign 1.1

    "They walk by the fountain. Josephine stops by its edge and waves over at the other two."

    hide joNeutral
    show joExclaim at jo_std:
        xalign 1.1

    j "They make wishes here by tossing coins into the fountain. I always keep a couple pennies on hand with this. *holds out a palm of pennies*"

    hide desNeutral
    show desFrown at ellis_std:
        xalign -0.05

    d "You keep pennies on hand to clog the local fountain every time you come to the park? *takes a penny*"

    hide joExclaim
    show joFrown at jo_std:
        xalign 1.1

    j "Desmond!"

    hide ellisNeutral

    show ellisAsk at ellis_std:
        xalign 0.55

    e "*takes a penny* Um, it's probably okay... they clean the fountain every now and then. If not coins, they'd still have to clean it for twigs and stuff..."

    hide desFrown
    show desDrowsy at ellis_std:
        xalign -0.05

    d "*shakes his head and tosses the coin in* Guess so."

    hide ellisAsk

    show ellisNeutral at ellis_std:
        xalign 0.55
    
    hide joFrown
    show joExclaim at jo_std:
        xalign 1.1

    j "Wishing for another smooth week of commissions! *tosses her coin in*"

    hide desDrowsy
    show desNeutral at ellis_std:
        xalign -0.05

    d "Aren't you supposed to keep your wish a secret?"

    hide joExclaim
    show joNeutral at jo_std:
        xalign 1.1

    j "That's just for shooting stars and birthdays wishes. Don't be silly."

    hide ellisNeutral

    show ellisThinking at ellis_std:
        xalign 0.55

    e "..."

    menu:
        "I wish I could be left alone":
            jump jhrAlone
        "I wish I was more comfortable around people":
            jump jhrComft

label jhrAlone:
    hide ellisThinking

    show ellisNervous at ellis_std:
        xalign 0.55

    e "(I wish I could be left alone...)"

    hide ellisNervous

    jump jhrCont3

label jhrComft:
    hide ellisThinking

    show ellisNervous at ellis_std:
        xalign 0.55

    e "(I wish I was more comfortable around people...)"

    $ social += 2
    if social >= socialMax:
        call SocialLevelUp

    hide ellisNervous

    jump jhrCont3

label jhrCont3:
    show ellisNeutral at ellis_std:
        xalign 0.55

    "Ellis tosses the coin into the water. The three of them begin walking towards the exit of the park."

    hide joNeutral
    show joFrown2 at jo_std:
        xalign 1.1

    j "*sighs* Ah, I wish we could stay a little longer."

    hide desNeutral
    show desDrowsy at ellis_std:
        xalign -0.05

    d "The day's not getting any younger, Josie. We can come again some other time. We should be getting started on the day's commissions. But it was nice meeting you, Ellis."

    hide desDrowsy
    show desNeutral at ellis_std:
        xalign -0.05

    hide joFrown2
    show joExclaim at jo_std:
        xalign 1.1

    j "Yeah! We should get together again some time! When are you all free?"

    hide ellisNeutral

    show ellisNervous at ellis_std:
        xalign 0.55

    e "Not sure... I think I'd have to check my schedule..."

    hide ellisNervous

    show ellisNeutral at ellis_std:
        xalign 0.55
    
    hide joExclaim
    show joClosed at jo_std:
        xalign 1.1

    j "*gives him a thumbs up* Sure! Just let me know when you're available, OK? Desmond, you too!"

    hide desNeutral
    show desChuckle at ellis_std:
        xalign -0.05

    d "Alright, I will."

    hide desChuckle
    show desNeutral at ellis_std:
        xalign -0.05

    "The three part ways and say goodbye."

    show blackScreen with fade

    ### end of quest

        
        
        


