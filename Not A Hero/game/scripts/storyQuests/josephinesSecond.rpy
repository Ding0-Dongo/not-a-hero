### DAY 5
### Setting = Normington Coffee

label jshrStart:
    
    #scene =  HQ
    scene hq with fade

    show screen StatUI

    #show ellis
    show ellisThinking2 at ellis_std with dissolve:
        xalign 1.1

    #move josephine and desmond in from left
    show desNeutral at ellis_std with moveinleft:
        xalign -0.05

    show joNeutral at jo_std with moveinleft:
        xalign 0.55

    "Josephine and Desmond walk in."

    hide joNeutral
    show joExclaim at jo_std:
        xalign 0.55

    j "Hey, Ellis? Oh, you're in here! Good."

    hide ellisThinking2

    show ellisSurprised at ellis_std:
        xalign 1.1

    e "*looks up* Huh?"

    hide ellisSurprised

    show ellisNeutral at ellis_std:
        xalign 1.1

    e "Oh, Josephine. Um... hi."

    hide desNeutral

    show desChuckle at ellis_std:
        xalign -0.05

    hide joExclaim
    show joNeutral at jo_std:
        xalign 0.55

    d "We were thinking on going to a cafe. Come with?"

    hide ellisNeutral

    show ellisNervous at ellis_std:
        xalign 1.1

    e "I'm... but I'm not done with my work for today..."

    hide desChuckle

    show desNeutral at ellis_std:
        xalign -0.05

    hide joNeutral
    show joClosed at jo_std:
        xalign 0.55

    j "Aw, don't worry, we won't be long!"

    hide joClosed
    show joExclaim at jo_std:
        xalign 0.55

    j "Even heroes need to take breaks sometimes!"

    hide joExclaim

    if josephineHangoutDone == True:
        jump jshrYes
    else:
        jump jshrNo

label jshrYes:

    show joNeutral at jo_std:
        xalign 0.55

    j "It'll just be like last time! Maybe just an hour or two. And if you're tight on time, we can always give you a hand!"
    jump jshrCont

label jshrNo:

    show joFrown at jo_std:
        xalign 0.55

    j "You didn't go with us last time, c'mon! Have you had brunch?"

    hide joFrown

    jump jshrCont

label jshrCont:

    show joNeutral at jo_std:
        xalign 0.55

    e "Well..."

    hide ellisNervous

    show ellisAsk at ellis_std:
        xalign 1.1

    e "Where are we going?"

    hide desNeutral

    show desChuckle at ellis_std:
        xalign -0.05

    d "Normington Coffee. It's a little shop just two blocks down. Have you been there before?"

    hide ellisAsk

    show ellisNeutral at ellis_std:
        xalign 1.1

    e "No, but I think I've heard of it."

    hide ellisNeutral

    show ellisNervous at ellis_std:
        xalign 1.1
    
    hide joNeutral
    show joExclaim at jo_std:
        xalign 0.55

    j "You've never been there? Oh my gosh, we have to go now. Their ice cream is so good!"

    "The three of them leave HQ and begin walking towards the cafe."

    show blackscreen with fade

    pause(0.4)

    #scene city
    scene plaza with dissolve

    show screen StatUI

    show ellisNeutral at ellis_std:
        xalign 1.1

    hide desChuckle

    show desNeutral at ellis_std:
        xalign -0.05

    show joNeutral at jo_std:
        xalign 0.55

    d "So how have your commisions been going? Going well, I hope?"

    hide ellisNeutral

    show ellisNervous at ellis_std:
        xalign 1.1

    e "Um... I think they're fine. Not so bad so far, anyways..."

    hide ellisNervous

    show ellisNeutral at ellis_std:
        xalign 1.1

    hide joNeutral
    show joFrown2 at jo_std:
        xalign 0.55

    j "*rolls eyes* The two of you really want to talk about HERO work on break?"

    hide desNeutral

    show desChuckle at ellis_std:
        xalign -0.05

    d "*laughs* Then what do you want to talk about, Josephine?"

    "Josephine throws up her hands."

    hide joFrown2
    show joFrown at jo_std:
        xalign 0.55

    j "Literally anything else, Desmond. You're such a square!"

    "The trio pauses at the intersection. Desmond presses the button for the walk signal."

    hide desChuckle

    show desNeutral at ellis_std:
        xalign -0.05

    if josephineHangoutDone == True:
        jump jhrYes2
    else:
        jump jhrNo2
    
label jhrYes2:
    hide joFrown
    show joClosed at jo_std:
        xalign 0.55

    j "Why don't we take this time to get to know each other better?"
    jump jshrCont2

label jhrNo2:
    hide joFrown
    show joClosed at jo_std:
        xalign 0.55

    j "I mean, we haven't even properly gotten to know Ellis yet!"
    jump jshrCont2

label jshrCont2:
    hide ellisNeutral

    show ellisThinking at ellis_std:
        xalign 1.1

    e "Haha, well... uh... what do you want to know?"

    hide joClosed
    show joNeutral at jo_std:
        xalign 0.55

    j "Anything! Things like... where were you born? Do you have any pets? Why did you become a HERO?"

    hide desNeutral

    show desChuckle at ellis_std:
        xalign -0.05

    d "You sound like you're asking him for his three security questions, Josephine."

    hide joNeutral
    show joClosed at jo_std:
        xalign 0.55

    j "Oh, hush!"

    hide desChuckle

    show desNeutral at ellis_std:
        xalign -0.05

    "The light turns and they begin crossing the street."

    hide ellisThinking

    show ellisThinking2 at ellis_std:
        xalign 1.1

    e "Well, I was born here actually, in Normington City. I've... um, pretty much lived here my whole life. It used to be called Borington, actually, up until about a decade ago-- I think."

    hide ellisThinking2

    show ellisNeutral at ellis_std:
        xalign 1.1

    hide joClosed
    show joNervous at jo_std:
        xalign 0.55

    j "'Boring Town'? That's such a weird Name. No wonder they changed it!"

    hide desNeutral

    show desDrowsy at ellis_std:
        xalign -0.05

    d "*nods* Apparently the city used to be a mining town, until the mines dried up. These days the mines are just tourist spots now."

    hide joNervous
    show joExclaim at jo_std:
        xalign 0.55

    j "Oh that's right, Desmond, you grew up in Normington too, didn't you?"

    hide desDrowsy

    show desNeutral at ellis_std:
        xalign -0.05

    hide joExclaim
    show joNeutral at jo_std:
        xalign 0.55

    d "Yeah. Moved out for a few years, but came back later."

    hide ellisNeutral

    show ellisAsk at ellis_std:
        xalign 1.1

    e "Really? Why? Normington isn't exactly the... the 'dream city'."

    hide desNeutral

    show desChuckle at ellis_std:
        xalign -0.05

    d "Eh, I guess I've always liked smaller towns better. You can get to know people more closely, and make some real friends."

    hide ellisAsk

    show ellisNeutral at ellis_std:
        xalign 1.1
    
    hide joNeutral
    show joExclaim at jo_std:
        xalign 0.55

    j "*teasing* You're secretly a {i}hopeless romantic{/i}, aren't you, Desmond?"

    hide desChuckle

    show desNeutral at ellis_std:
        xalign -0.05

    "Desmond coughs."

    d "What? No."

    hide ellisNeutral

    show ellisHappy at ellis_std:
        xalign 1.1

    e "*stifles a laugh* Um... so Josephine, did you grow up in Normington, too?"

    hide ellisHappy

    show ellisNeutral at ellis_std:
        xalign 1.1

    hide joExclaim
    show joNeutral at jo_std:
        xalign 0.55

    j "Oh no, I just moved here recently! Just about half a year ago."

    j "I finished up an internship and thought I'd move here, since I have a friend that lives here."

    hide ellisNeutral

    show ellisThinking2 at ellis_std:
        xalign 1.1

    e "Oh, that's um... cool?"

    hide ellisThinking2

    show ellisThinking at ellis_std:
        xalign 1.1

    e "So, then, is there anything you miss from your old home?"

    hide ellisThinking

    show ellisNeutral at ellis_std:
        xalign 1.1
    
    hide joNeutral
    show joExclaim at jo_std:
        xalign 0.55

    j "Probably the beach... there used to be a big rocky beach with this lighthouse just thirty minutes from my house."

    hide joExclaim
    show joClosed at jo_std:
        xalign 0.55

    j "It's not the sandy paradise-style beaches we have around here."

    hide joClosed
    show joExclaim at jo_std:
        xalign 0.55

    j " I don't think it's worse, but it's just... different!"

    stop music

    scene coffeeshop_inside with fade

    show screen StatUI

    play music CoffeeShopMusic volume 0.5

    play sound CafeChatterAudio volume 0.4

    show ellisNeutral at ellis_std:
        xalign 1.1

    show joNeutral at jo_std:
        xalign 0.55
    
    show desNeutral at ellis_std:
        xalign -0.05

    "They arrive at the cafe, and let themselves in. It's quite busy at this time of the day, the cafe filled with the warm smells of coffee and the sound of indistinct chatter. Fans spinning above keep the cafe cool."

    d "One of you want to sit down and save a table? I'll get in line to order."

    hide joNeutral
    show joExclaim at jo_std:
        xalign 0.55

    j "Sure, I'll find us a good spot! Desmond, can you get me my usual?"

    hide joExclaim
    show joNeutral at jo_std:
        xalign 0.55

    #move josephine off screen
    show joNeutral at jo_std:
        linear 1.5 xalign -1.8

        pause(1.2)
    
    # better center ellis and desmond
    show ellisNeutral at ellis_std:
        linear 0.8 xalign 0.75

    show desNeutral at ellis_std:
        linear 0.8 xalign 0.1

    "Desmond nods and Josephine waves at them. She then wanders off to find a free table."

    hide joNeutral

    hide ellisNeutral

    show ellisAsk at ellis_std:
        xalign 0.75

    e "Her usual? You guys go out to get coffee a lot then, I take it?"

    hide desNeutral

    show desChuckle at ellis_std:
        xalign 0.1

    d "Eh, not that often. Maybe every two weeks. She values her alone time too."

    hide ellisAsk

    show ellisSurprised at ellis_std:
        xalign 0.75

    e "Really?"

    hide desChuckle

    show desNeutral at ellis_std:
        xalign 0.1

    d "I mean, who doesn't? Heh, but I guess Josephine doesn't seem like your standard introvert."

    hide ellisSurprised

    show ellisCringe at ellis_std:
        xalign 0.75

    e "(Ouch...)"

    hide ellisCringe

    show ellisNeutral at ellis_std:
        xalign 0.75

    d "I think she's more of an ambivert: sometimes she'll be pretty excited to hang out, other times she wants to be left alone."

    hide ellisNeutral

    show ellisThinking at ellis_std:
        xalign 0.75

    e "Oh, that... that makes a lot of sense, actually."

    hide desNeutral

    show desDrowsy at ellis_std:
        xalign 0.1

    d "You didn't notice?"

    hide ellisThinking

    show ellisSurprised at ellis_std:
        xalign 0.75

    "Before Ellis can respond, the barista calls them up."

    hide ellisSurprised

    show ellisNervous at ellis_std:
        xalign 0.75

    barista "Next guest! Hi, may I take your order?"

    hide desDrowsy

    show desNeutral at ellis_std:
        xalign 0.1

    d "*steps up to the counter* Hi. I'll get a pistachio affogato, a slice of raspberry cake, amd a medium espresso."

    barista "OK, and can I get a name for your order?"

    d "Not done yet, my friend has to order. *gestures at Ellis*"

    hide ellisNervous

    show ellisCringe at ellis_std:
        xalign 0.75

    e "A-ah... right... um... (I forgot to look at the menu...)"

    hide ellisCringe

    show ellisNervous at ellis_std:
        xalign 0.75

    e "*stammers* S-sorry! Give me a minute! *quickly looks up at the menu*"

    barista "It's also laminated on the counter, sir."

    hide ellisNervous

    show ellisCringe at ellis_std:
        xalign 0.75

    e "Right! Sorry! (Ahhhh, I'm being so dumb!)"

    d "Relax, take your time. It's your first time here, after all, isn't it?"

    hide ellisCringe

    show ellisNeutral at ellis_std:
        xalign 0.75

    "The barista offers a friendly smile."

    barista "First time? I'd suggest a matcha latte-- might help you calm down."

    "She leans closer and lowers her voice."

    barista "Also, it's really easy for me to make."

    hide ellisNeutral

    show ellisThinking2 at ellis_std:
        xalign 0.75

    e "Um, maybe, maybe I'll just get-"

    "An impatient customer behind them begins talking in a loud voice."

    hide ellisThinking2

    show ellisSurprised at ellis_std:
        xalign 0.75

    customer "Hey, what's taking so long?"

    "Ellis and Desmond turn around to see a red-faced man in a business suit tapping his foot."

    barista "Sorry, sir. If you'll just give these two gentlemen a moment-"

    customer "I've got places to be! If you're not ready to order, then you should let others who are ready go first!"

    "Customer service is hard."

    menu:
        "Stand up for yourself":
            jump jshrStandUp
        "Let Desmond handle it":
            jump jshrDontStand

label jshrStandUp:
    hide ellisSurprised

    hide desNeutral

    show desDrowsy at ellis_std:
        xalign 0.1

    show ellisObjection at ellis_std:
        xalign 0.75

    e "S-sorry, I've just... I've never been here before. I just need another minute, sorry."

    $ social += 3
    if social >= socialMax:
        call SocialLevelUp

    hide ellisObjection

    hide desDrowsy

    jump jshrCont3

label jshrDontStand:
    hide ellisSurprised

    hide ellisNeutral

    show desDrowsy at ellis_std:
        xalign 0.1

    show ellisAnnoyed at ellis_std:
        xalign 0.75

    "Desmond steps in."

    d "We were here first. Everyone in this line is waiting their turn."

    d "*gestures to Ellis* He's never been here before, so just give him some time."

    d "And if you have any recommendations... *shrugs*"

    hide ellisAnnoyed

    hide desDrowsy

    jump jshrCont3

label jshrCont3:
    show ellisNeutral at ellis_std:
        xalign 0.75
    
    show desNeutral at ellis_std:
        xalign 0.1

    "The businessman stares at Ellis, then grumbles and nods, going quiet."

    "Ellis and Desmond turn back to the counter."

    barista "Sorry about that. You were saying, sir?"

    hide ellisNeutral

    show ellisThinking at ellis_std:
        xalign 0.75

    e "It's... it's okay. And I'll get the drink you suggested, did you say it was a matcha latte?"

    barista "Yep, anything else?"

    hide ellisThinking

    show ellisThinking2 at ellis_std:
        xalign 0.75

    e "*quickly skims the menu again* A slice of lemon pound cake? That's- that's all for me, thanks."

    hide ellisThinking2

    show ellisNeutral at ellis_std:
        xalign 0.75

    "The barista rings up the order and begins writing names on cups."

    barista "Okay, and the name for the orders?"

    d "Desmond."

    "Desmond pays for the food."

    barista "Got it. It should be ready in fifteen minutes."

    "The barista gives them one last smile as they leave."

    show blackScreen with fade

    stop sound

    scene coffeeshop_inside with fade

    show screen StatUI

    play sound CafeChatterAudio volume 0.4

    show joNeutral at jo_std with dissolve:
        xalign 0.5

    show desNeutral at ellis_std:
        xalign 3.0

    show desNeutral at ellis_std:
        linear 1.5 xalign -0.05

    show ellisSad at ellis_std:
        xalign 3.0

    show ellisSad at ellis_std:
        linear 1.5 xalign 1.05

    pause(1.3)

    "It doesn't take long for the two of them to find Josephine at a table near the windows. The sunlight is slanting in over the floorboards, and the area is warm. Josephine has a look of concern on her face."
    
    hide joNeutral
    show joFrown at jo_std:
        xalign 0.5

    j "I saw what happened, are you guys alright?"

    hide desNeutral

    show desChuckle at ellis_std:
        xalign -0.05

    d "Nothing we couldn't handle."

    hide desChuckle

    show desNeutral at ellis_std:
        xalign -0.05

    "Ellis bobs his head in affirmation. He still feels overwhelmed."

    hide joFrown
    show joFrown2 at jo_std:
        xalign 0.5

    j "*sympathetic* You don't handle people too well, do you, Ellis?"

    hide ellisSad

    show ellisCry2 at ellis_std:
        xalign 1.05

    "Ellis turns red and puts his head in his arms on the table. He shakes his head."

    hide joFrown2
    show joFrown at jo_std:
        xalign 0.5

    j "Sorry to hear that, Ellis... I can help you out with that, if you ever want me too!"

    hide ellisCry2

    show ellisSad at ellis_std:
        xalign 1.05

    hide desNeutral

    show desDrowsy at ellis_std:
        xalign -0.05

    d "*playing with a sugar packet in his hands* Help him out how?"

    hide desDrowsy

    show desNeutral at ellis_std with vpunch:
        xalign -0.05
    
    hide joFrown
    show joClosed at jo_std:
        xalign 0.5

    j "*swats him* Desmond! Some people have anxiety!"

    hide ellisSad

    show ellisCringe at ellis_std:
        xalign 1.05

    e "*looks up* I- I don't have anxiety... (Well, not medically diagnosed, anyways...)"

    hide joClosed
    show joFrown2 at jo_std:
        xalign 0.5

    j "*half-serious* Don't listen to anything Desmond says, Ellis. He's one of those... bold, strong, extroverted types. He doesn't know what we go through."

    hide ellisCringe

    show ellisNeutral at ellis_std:
        xalign 1.05

    hide desNeutral

    show desChuckle at ellis_std:
        xalign -0.05

    d "What? You make me sound like a bad guy."

    hide joFrown2
    show joExclaim at jo_std:
        xalign 0.5

    j "*laughing* My point is that you're better with people!"

    hide joExclaim
    show joNeutral at jo_std:
        xalign 0.5

    "Josephine and Desmond continue to talk as they wait for their food. Ellis stays mostly quiet."

    hide ellisNeutral

    show ellisSad2 at ellis_std:
        xalign 1.05

    e "(I feel like I'm bringing them down... why did I agree to come here?)"

    hide desChuckle

    show desNeutral at ellis_std:
        xalign -0.05

    "Desmond's name is called. The food is ready."

    d "*gets up from his seat* I'll go get it."

    show desNeutral at ellis_std:
        linear 1.2 xalign 2.0

    hide joNeutral
    show joExclaim at jo_std:
        xalign 0.5

    pause(0.8)

    j "*calls after him* Don't forget to grab some napkins!"

    "After Desmond leaves, Josephine begins talking to Ellis again."

    hide joExclaim
    show joFrown at jo_std:
        xalign 0.5

    j "You feeling alright, Ellis? Introverted blues?"

    hide ellisSad2

    show ellisNervous at ellis_std:
        xalign 1.05

    e "... Y-yeah..."

    hide joFrown
    show joFrown2 at jo_std:
        xalign 0.5

    j "We can just get the food and leave, if you want?"

    hide ellisNervous

    show ellisHappy at ellis_std:
        xalign 1.05
    
    e "No, it's- it's fine. Really. *manages a smile*"

    hide ellisHappy

    show ellisNeutral at ellis_std:
        xalign 1.05

    hide joFrown2
    show joClosed at jo_std:
        xalign 0.5

    j "Really? If you're not comfortable, you shouldn't push yourself too far."

    hide joClosed
    show joFrown at jo_std:
        xalign 0.5

    j "I don't mean to lecture, of course- It's just that I used to struggle with that kind of thing too."

    "Josephine offers a gentle smile to Ellis."

    hide joFrown
    show joNeutral at jo_std:
        xalign 0.5

    j "Really, though. If you need any help, I'm always available."

    show ellisHappy at ellis_std:
        xalign 1.05

    e "... Thanks, Josephine."

    "Desmond return with the food."

    show desNeutral at ellis_std:
        linear 1.0 xalign -0.05

    hide ellisHappy

    show ellisNeutral at ellis_std:
        xalign 1.05

    pause(0.6)

    d "*sets down the food in front of Josephine* Pistachio affogato and raspberry cake..."

    show desChuckle at ellis_std:
        xalign -0.05

    d "*sets down the food in front of Ellis* Matcha latte and lemon pound cake."

    hide desChuckle

    show desDrowsy at ellis_std:
        xalign -0.05

    d "And... espresso."

    "Desmond puts a lid over his espresso and takes a careful sip of the hot beverage."

    "Josephine digs a plastic spoon into her affogato."

    hide joNeutral
    show joExclaim at jo_std:
        xalign 0.5

    j "So... do either of you have plans after this?"

    hide joExclaim
    show joNeutral at jo_std:
        xalign 0.5

    e "*pokes a fork into his cake* Um... probably just going to run commissions with DELTA..."

    d "*nods* Me too."

    hide desDrowsy

    show desNeutral at ellis_std:
        xalign -0.05

    d "But I was thinking on running a TEAM commission, if you two are free?"

    hide joNeutral
    show joClosed at jo_std:
        xalign 0.5

    j "Oh? Which one?"

    hide desNeutral

    show desChuckle at ellis_std:
        xalign -0.05

    d "I'm trying to fill my TEAM commission quota. If I can hit my quota by the end of this month, I'll be a full-fledged hero."

    d "There's a TEAM commission this week taking place at the Normington Cultural Event. It's all week, so if you two aren't available today, then maybe over the weekend?"

    hide joClosed
    show joExclaim at jo_std:
        xalign 0.5

    j "I'm definitely free over the weekend! What's the commission's details?"

    hide joExclaim
    show joNeutral at jo_std:
        xalign 0.5

    hide ellisNeutral

    show ellisNervous at ellis_std:
        xalign 1.05

    "Ellis fidgets nervously at the idea of such a strenuous social event. His stomach turns."

    e "Um... I'm not sure if I'm... uh..."

    hide desChuckle

    show desDrowsy at ellis_std:
        xalign -0.05

    d "It'll mostly be a lot of volunteer work: set-up, clean-up, helping out at stands, that kind of thing."

    hide ellisNervous

    show ellisAnnoyed2 at ellis_std:
        xalign 1.05

    d "I know some other TEAMs have already signed up, but there's only so many volunteers they can take..."

    hide joNeutral
    show joExclaim at jo_std:
        xalign 0.5

    j "Then defintely sign us up! We can't let them get to it before us!"

    hide desDrowsy

    show desNeutral at ellis_std:
        xalign -0.05

    "Ellis stands up so quickly his chair scoots back and nearly falls over."

    hide ellisAnnoyed2

    show ellisCringe at ellis_std with hpunch:
        xalign 1.05

    e "I- I have to go."

    hide joExclaim
    show joNeutral at jo_std:
        xalign 0.5

    "The others look up at him. Josephine seems to realize her mistake."

    hide joNeutral
    show joNervous at jo_std:
        xalign 0.5

    j "Oh-! Ellis, I didn't mean-"

    hide ellisCringe

    show ellisNervous at ellis_std:
        xalign 1.05

    e "I'll see you two later!"

    hide joNervous
    show joFrown at jo_std:
        xalign 0.5

    show ellisNervous at ellis_std:
        linear 1.6 xpos 1.6

        pause(1.2)

    "Ellis practically flees from the cafe, almost running down the businessman from earlier."

    d "... Did we say something wrong?"

    hide ellisNervous

    hide joFrown
    show joNervous at jo_std:
        xalign 0.5

    j "Puts a hand to her mouth* I have to go talk to him."

    show joNervous at jo_std:
        linear 1.5 xalign 2.1
    
    pause(0.8)

    stop sound

    stop music

    show blackScreen with fade

    play music MainMusic

    hide StatUI

    pause(1.2)

    "(Ellis was stressed out by the encounter.) (+1 stress)"
    $ stress += 1

    return

### If you're reading this, I need more coffee...
    




