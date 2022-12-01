### start of Petty Thievery story quest
### DAY 4

label ptStart:
    
    ##Scene = city
    show alleyway with fade

    show screen StatUI

    "Ellis is wandering around in the downtown areas of Normington City when he sees a trash can rattling around, and a concerned looking woman standing nearby it with a trash bag in hand."

    #show ellis
    show ellisNeutral with moveinleft:
        xalign 0.5
        yalign 1.3

    e "Um... ma'am?"

    "Ellis waves to get her attention."

    e "Ma'am, do you... need any help?"

    "The woman looks relieved to see him."

    woman "Oh yes, please, I think there's an animal in my garbage. Could you scare it off for me, dear?"

    e "Sure, I... yeah, I can do that."

    "Ellis grabs the handles of the trash can and gives it a tentative shake."

    "After a moment, a raccoon pops its head out of the can, blinking in the sunlight."

    #show SHIFTY THE MAIN MAN

    e "Oh. Hello there."

    #increment stress?

    "The raccoon lets out a sort of bark at Ellis and then leaps out of the trash can and disappears into the alley."

    #hide shifty GOODBYE DEAR FRIEND

    e "(Maybe I should've just called pest control...)"

    "The woman puts her trash bag in the can."

    woman "Thank you so much, dear, oh, what's your name?"

    e "*awkwardly* Um... I'm Ellis."

    woman "Well, thank you, Ellis! Ah, I'm sorry I don't have anything to give you as a sign of my gratitude."

    woman "*laughs lightly* Those raccoons, really! The city couldn't be bothered to do anything about them."

    woman "I'm sure I could fix you a glass of iced tea or something. Won't you come inside?"

    e "Oh, ah, sorry... I'm on work."

    #INCREMENT STRESS YES
    #show ellis nervous

    e "Thanks- thank you for the offer, though!"

    woman "That's unfortunate. Swing by any time, then!"

    "The woman goes back into her house."

    e "..."

    #fade to black

    "Shifty's Shop unlocked!\nYou can go there and buy energy drinks."




