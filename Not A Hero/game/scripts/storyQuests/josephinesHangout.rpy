### DAY 2
# Optional Story Quest

#scene = city

label jhrStart:
    scene plaza with fade

    show ellisNeutral at ellis_std with dissolve:
        xalign 0.82

    "NORMINGTON ASSOCIATION OF HEROES HEADQUARTERS (Outside)"

    d "You wanted to meet up, Josephine?"

    j "Yeah!"

    d "*gestures at Ellis* Well, we're both here, so..."

    j "I was just thinking... since Ellis is new, and we haven't been able to properly get to know him... we could go for a walk in the park! You two are free, right?"

    d "*shrugs* Free enough, I get."

    e "U-um... yeah, I... I'm free."

    j "*beams* Great! C'mon, let's go!"

    show blackScreen with fade

    "10 minutes later"

    pause (0.8)

    scene park with dissolve

    "NORMINGTON PARK"

    "Normington Park is picturesque at this time of day, the sun shining down over it like a blessing. A fountain pours endlessly in the center of a long curved pathway of crushed gravel that winds through the park."

    "Flowering trees provide some welcome shade overhead, and a light breeze sends leaves and petals fluttering down. Some children with a kite run past the trio as they step onto the path."

    j "Great weather for a walk, isn't it."

    d "Eh, we got lucky. Forecast said it was going to rain today."

    j "I was wondering why you brought an umbrella to HQ this morning..."

    j "*clasps her hands together* So! Ellis, what made you want to be a HERO?"

    e "Um... well..."

    j "Was it the prestige? The sense of helping your community? The pretty and friendly android mentors?"

    menu:
        "Make something up":
            jump jhrMakeUp
        "Tell the truth":
            jump jhrTellTruth

label jhrMakeUp:
    e "Y-yeah! That- that last one. (What did she say again?)"

    j "Oooh- haha! Wouldn't have expected that from you, Ellis"

    e "*flushes* (Did I say something wrong?)"

    d "{i}Josephine.{\i}"

    j "*laughs* I'm kidding, I'm kidding! Yeah... we can't date any of the androids... It's against policy. Really is a shame though-- some of the androids working at the association really are cute."

    e "(D-date?!)"

    jump jhrCont

label jhrTellTruth:
    e "Actually, it was... kind of an accident."

    d "An accident?"

    e "It's not really that interesting... You're not going to believe this, but I used to be roommates with another guy named Ellis."

    j "*eyes widen* For real? Ellis, you've either seen everything, or nothing fazes you."

    e "*laughs* I'm pretty sure the association was looking for him, but... he kind of moved out on short notice."

    d "Why did you take the job then?"

    jump jhrCont

label jhrCont:
    e "*helplessly* I don't know."

    e "DELTA seemed really surprised too, and he asked me to give him a week while the association figured something out."

    e "I guess... I guess I would've felt bad if I just left him hanging."

    d "That's pretty generous of you."

    d "Are you going to stay being a HERO then? Of you weren't the one signing up for the job in the first place, I mean..."

    menu:
        "Yeah":
            jump jhrYes
        "I don't know":
            jump jhrNo

label jhrYes:
    e "Yeah, I... I think so."

    e "I can't explain it, but being a HERO... even if it's only been a day or two, I feel like this is helping me as much as it's helping others."

    j "Oh? Some kind of epic quest of self-improvement?"

    e "Aha... ha... um... kind of?"

    jump jhrCont2

label jhrNo:
    e "I don't know. I'm still thinking about it. I mean, I haven't been doing this for a week yet, even."

    d " That's fair. Not everyone stays. Usually most people decide whether or not they want to keep doing this after a week or two."

    j "Awww. Well, I hope we can convince you to stay, Ellis. You seem like a good guy to work with. *smiles*"

    e "*flushes* Th-thanks."

    jump jhrCont2

label jhrCont2:
    "They walk by the fountain. Josephine stops by its edge and waves over at the other two."

    j "They make wishes here by tossing coins into the fountain. I always keep a couple pennies on hand with this. *holds out a palm of pennies*"

    d "You keep pennies on hand to clog the local fountain every time you come to the park? *takes a penny*"

    j "Desmond!"

    e "*takes a penny* Um, it's probably okay... they clean the fountain every now and then. If not coins, they'd still have to clean it for twigs and stuff..."

    d "*shakes his head and tosses the coin in* Guess so."

    j "Wishing for another smooth week of commissions! *tosses her coin in*"

    d "Aren't you supposed to keep your wish a secret?"

    j "That's just for shooting stars and birthdays wishes. Don't be silly."

    e "..."

    menu:
        "I wish I could be left alone":
            jump jhrAlone
        "I wish I was more comfortable around people":
            jump jhrComft

label jhrAlone:
    e "(I wish I could be left alone...)"

    jump jhrCont3

label jhrComft:
    e "(I wish I was more comfortable around people...)"

    # ++ social points

    jump jhrCont3

label jhrCont3:
    "Ellis tosses the coin into the water. The three of them begin walking towards the exit of the park."

    j "*sighs* Ah, I wish we could stay a little longer."

    d "The day's not getting any younger, Josie. We can come again some other time. We should be getting started on the day's commissions. But it was nice meeting you, Ellis."

    j "Yeah! We should get together again some time! When are you all free?"

    e "Not sure... I think I'd have to check my schedule..."

    j "*gives him a thumbs up* Sure! Just let me know when you're available, OK? Desmond, you too!"

    d "Alright, I will."

    "The three part ways and say goodbye."

    show blackScreen with fade

    ### end of quest

        
        
        


