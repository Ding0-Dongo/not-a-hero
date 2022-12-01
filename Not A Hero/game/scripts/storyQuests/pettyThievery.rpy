### start of Petty Thievery story quest
### DAY 4

label ptStart:
    
    ##Scene = city
    show alleyway with fade

    show screen StatUI

    "Ellis is wandering around in the downtown areas of Normington City when he sees a trash can rattling around, and a concerned looking woman standing nearby it with a trash bag in hand."

    #show ellis
    show ellisNeutral with moveinleft:
        zoom 0.45
        xalign 0.5
        yalign -1.5

    e "Um... ma'am?"

    "Ellis waves to get her attention."

    show ellisAsk:
        xalign 0.5
        yalign -1.5

    e "Ma'am, do you... need any help?"

    show ellisNeutral:
        xalign 0.5
        yalign -1.5

    "The woman looks relieved to see him."

    woman "Oh yes, please, I think there's an animal in my garbage. Could you scare it off for me, dear?"

    show ellisThinking:
        xalign 0.5
        yalign -1.5

    e "Sure, I... yeah, I can do that."

    show ellisNeutral:
        xalign 0.5
        yalign -1.5

    "Ellis grabs the handles of the trash can and gives it a tentative shake."

    pause(0.3)

    show ellisSurprised:
        xalign 0.5
        yalign -1.5

    "After a moment, a raccoon pops its head out of the can, blinking in the sunlight."

    show ellisNeutral:
        xalign 0.5
        yalign -1.5

    show ellisNeutral:
        linear 0.8 xpos 0.35
        yalign -1.5

    #show SHIFTY THE MAIN MAN

    show shifty with moveinright:
        xalign 0.65
        yalign 0.8

    e "Oh. Hello there."

    #increment stress?
    show screen StatUI with vpunch
    $ stress += 1

    show ellisSurprised:
        xalign 0.35
        yalign -1.5

    "The raccoon lets out a sort of bark at Ellis and then leaps out of the trash can and disappears into the alley."

    show shifty with hpunch:
        xalign 0.65

    show shifty:
        linear 0.3 xpos 1.5

    #hide shifty GOODBYE DEAR FRIEND

    show ellisCry:
        xalign 0.35
        yalign -1.5

    pause(0.5)
    
    show ellisCry:
        linear 1.2 xpos 0.5
        yalign -1.5

    pause (1.0)

    e "(Maybe I should've just called pest control...)"

    "The woman puts her trash bag in the can."

    show ellisNeutral:
        xalign 0.35
        yalign -1.5

    show ellisNeutral:
        linear 1.2 xalign 0.5
        yalign -1.5
    
    woman "Thank you so much, dear, oh, what's your name?"

    show ellisNervous:
        xalign 0.5
        yalign -1.5

    e "*awkwardly* Um... I'm Ellis."

    woman "Well, thank you, Ellis! Ah, I'm sorry I don't have anything to give you as a sign of my gratitude."

    show ellisNeutral:
        xalign 0.5
        yalign -1.5

    woman "*laughs lightly* Those raccoons, really! The city couldn't be bothered to do anything about them."

    woman "I'm sure I could fix you a glass of iced tea or something. Won't you come inside?"

    show ellisCry2:
        xalign 0.5
        yalign -1.5

    e "Oh, ah, sorry... I'm on work."

    #INCREMENT STRESS YES
    show ellisCry2 with hpunch:
        xalign 0.5
        yalign -1.5
    
    $ stress += 1

    #show ellis nervous

    pause(1.0)

    show ellisCry:
        xalign 0.5
        yalign -1.5

    e "Thanks- thank you for the offer, though!"

    show ellisCringe:
        xalign 0.5
        yalign -1.5

    woman "That's unfortunate. Swing by any time, then!"

    "The woman goes back into her house."

    show ellisNeutral:
        xalign 0.5
        yalign -1.5

    e "..."

    show blackScreen with fade

    pause(2.0)

    "Shifty's Shop unlocked!\nYou can go there and buy energy drinks."

    jump start




