### start of Petty Thievery story quest
### DAY 4

label ptStart:
    
    ##Scene = city
    scene alleyway with fade

    show screen StatUI

    "Ellis is wandering around in the downtown areas of Normington City when he sees a trash can rattling around, and a concerned looking woman standing nearby it with a trash bag in hand."

    #show ellis
    show ellisNeutral at ellis_std with moveinleft:
        xalign 0.5

    e "Um... ma'am?"

    "Ellis waves to get her attention."

    hide ellisNeutral

    show ellisAsk at ellis_std:
        xalign 0.5

    e "Ma'am, do you... need any help?"

    hide ellisAsk

    show ellisNeutral at ellis_std:
        xalign 0.5

    "The woman looks relieved to see him."

    woman "Oh yes, please, I think there's an animal in my garbage. Could you scare it off for me, dear?"

    hide ellisNeutral

    show ellisThinking at ellis_std:
        xalign 0.5

    e "Sure, I... yeah, I can do that."

    hide ellisThinking

    show ellisNeutral at ellis_std:
        xalign 0.5

    "Ellis grabs the handles of the trash can and gives it a tentative shake."

    pause(0.3)

    hide ellisNeutral

    show ellisSurprised at ellis_std with vpunch:
        xalign 0.5

    "After a moment, a raccoon pops its head out of the can, blinking in the sunlight."

    hide ellisSurprised

    show ellisNeutral at ellis_std:
        xalign 0.5

    show ellisNeutral at ellis_std:
        linear 0.8 xpos 0.35

    #show SHIFTY THE MAIN MAN

    show shifty with moveinright:
        xalign 0.65
        yalign 0.8

    e "Oh. Hello there."

    #increment stress?
    show screen StatUI with vpunch
    $ stress += 1

    hide ellisNeutral

    show ellisSurprised at ellis_std:
        xalign 0.35

    "The raccoon lets out a sort of bark at Ellis and then leaps out of the trash can and disappears into the alley."

    show shifty with hpunch:
        xalign 0.65

    show shifty:
        linear 0.3 xpos 1.5

    #hide shifty GOODBYE DEAR FRIEND

    hide ellisSurprised

    show ellisCry at ellis_std:
        xalign 0.35

    pause(0.5)
    
    show ellisCry at ellis_std:
        linear 1.2 xalign 0.5
        yalign -1.5

    pause (1.0)

    e "(Maybe I should've just called pest control...)"

    "The woman puts her trash bag in the can."
    
    woman "Thank you so much, dear, oh, what's your name?"

    hide ellisCry

    show ellisNervous at ellis_std:
        xalign 0.5

    e "*awkwardly* Um... I'm Ellis."

    woman "Well, thank you, Ellis! Ah, I'm sorry I don't have anything to give you as a sign of my gratitude."

    hide ellisNervous

    show ellisNeutral at ellis_std:
        xalign 0.5

    woman "*laughs lightly* Those raccoons, really! The city couldn't be bothered to do anything about them."

    woman "I'm sure I could fix you a glass of iced tea or something. Won't you come inside?"

    hide ellisNeutral

    show ellisCry2 at ellis_std:
        xalign 0.5

    e "Oh, ah, sorry... I'm on work."

    hide ellisCry2

    #INCREMENT STRESS YES
    show ellisCry2 at ellis_std with hpunch:
        xalign 0.5
    
    $ stress += 1

    #show ellis nervous

    pause(1.0)

    show ellisCry at ellis_std:
        xalign 0.5

    e "Thanks- thank you for the offer, though!"

    hide ellisCry

    show ellisCringe at ellis_std:
        xalign 0.5

    woman "That's unfortunate. Swing by any time, then!"

    "The woman goes back into her house."

    e "..."

    hide screen StatUI

    show blackScreen with fade

    pause(2.0)

    "Shifty's Shop unlocked!\nYou can go there and buy energy drinks."

    jump start




